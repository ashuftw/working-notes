# Proposal: explicit vacuum factor (`P_ratio`) for TVSA

**Status:** proposal / not implemented. Behaviour is unchanged until a desorption
value is set.

## Goal

Turn the current temperature-swing (TSA) model into a temperature–vacuum swing
(TVSA) by adding a single dimensionless knob, `P_ratio = P_vac / P_atm`, that
lowers the CO₂ partial pressure the sorbent equilibrates against during
desorption. `P_ratio = 1.0` reproduces today's behaviour; `P_ratio = 0.1`
models a 0.1 bar vacuum.

## Physics

The Tóth isotherm sets the equilibrium loading through the product `b·p`:

    q_e = ns·(b·p) / (1 + (b·p)^tT)^(1/tT)

`p` is the CO₂ *partial* pressure. A vacuum lowers it, which shrinks `q_e`,
which widens the desorption driving force in the LDF term `k_s·(q_e − q_wall)`.

At the desorption temperature (373 K) the affinity `b` is already tiny (the
210 kJ/mol heat collapses it), so `b·p ≪ 1` and the isotherm is in its **linear**
limit `q_e ≈ ns·b·p`. There `q_e` scales directly with `P_ratio`, so e.g.
`P_ratio = 0.1` cuts the residual ("heel") loading ~10×. Temperature does the
bulk of the swing; vacuum cleans out the tail.

## Honest caveat

This is a **lumped proxy, not a rigorous pressure solve.** Partial pressure
already equals `Ca·R·T`, so in principle a real vacuum should show up as `Ca`
dropping through the transport terms, not as a multiplier. The multiplier is
justified because the model's desorption transport (purge at `u_max_des` +
diffusion) under-resolves how fast a real vacuum evacuates the channel.
`P_ratio` is a stand-in for that missing evacuation — it captures the
*equilibrium* effect of reduced total pressure without solving pressure-driven
flow. If true coupling is ever needed (real pressure gradients, gas actually
pulled out), that is a separate, larger change (a momentum/Ergun field).

## Implementation

`P_ratio` threads through exactly like the existing TSA params: it is appended
to the `tsa_args` bundle, carried through every solver signature, and consumed
in `toth_q_e`. It is `1.0` in the adsorption phase and `P_des_ratio` in the
desorption phase.

### 1. `solvers.py` — `toth_q_e`

Add the parameter (defaulted to 1.0 so existing callers are unaffected) and
apply it to the partial pressure:

```python
def toth_q_e(Ca_wall, T, T0, b0, ns0, tT0, dH0, chi, alpha, rho_s, P_ratio=1.0):
    ...
    Ca_clamp = np.maximum(Ca_wall, 0.0)
    p_kPa = Ca_clamp * R_GAS * T / 1000.0 * P_ratio   # <-- * P_ratio added
```

### 2. `solvers.py` — thread through the solver signatures

In all four solvers (`solve_adv_diff`, `solve_thin_duct_Cartesian`,
`solve_thin_duct_Radial`, `solve_adv_diff_Radial`) and in
`apply_boundary_conditions`, insert `P_ratio` between `rho_s` and `tsa_enabled`
in the signature, and forward it in the `apply_boundary_conditions(...)` call.

In `apply_boundary_conditions`, pass it to the isotherm call (`solvers.py:128`):

```python
q_e_eff = toth_q_e(Ca[-2, 1:-1], T, T0, b0, ns0, tT0, dH0, chi, alpha, rho_s, P_ratio)
```

### 3. `simulation.py` — read it and split adsorption vs desorption

Read both ratios from the `tsa` dict (defaulting to 1.0):

```python
P_ads_ratio = tsa.get('P_ads_ratio', 1.0)
P_des_ratio = tsa.get('P_des_ratio', 1.0)
```

`q_e_ref` (the clip ceiling, `simulation.py:53`) is an *adsorption*-condition
reference, so pass `P_ads_ratio` there:

```python
q_e_ref = float(toth_q_e(np.array([float(iC)]), T, T0, b0, ns0, tT0,
                         dH0, chi, alpha, rho_s, P_ads_ratio)[0])
```

Insert `P_ratio` into both arg bundles, mirroring the signature order
(between `rho_s` and `tsa_enabled`):

```python
# adsorption (simulation.py:106)
tsa_args     = [T,     k_s_ref, q_e_ref, T0, b0, ns0, tT0, dH0, chi, alpha, rho_s, P_ads_ratio, tsa_enabled]
# desorption  (simulation.py:194)
tsa_args_des = [T_des, k_s_ref, q_e_ref, T0, b0, ns0, tT0, dH0, chi, alpha, rho_s, P_des_ratio, tsa_enabled]
```

### 4. `main-pei-tsa.py` — expose the knob

Add to the `tsa` dict (alongside `T_des`, `u_max_des`, etc.):

```python
'P_ads_ratio': 1.0,   # adsorption at atmospheric total pressure
'P_des_ratio': 0.1,   # desorption under 0.1 bar vacuum (TVSA); 1.0 = pure TSA
```

## Effect / how to verify

- `P_des_ratio = 1.0` → byte-identical to current TSA output (regression check).
- `P_des_ratio < 1.0` → lower residual wall loading at end of desorption and a
  faster approach to `des_threshold`. Compare the desorption tail in
  `PEI-TSA/desorption.txt` across `P_des_ratio ∈ {1.0, 0.3, 0.1}`.
- The adsorption-phase breakthrough is unchanged (it uses `P_ads_ratio = 1.0`).

## Scope notes

- Touches only the equilibrium term; `k_s` is still held constant across phases
  (the no-Arrhenius assumption already flagged in `RUNDOWN.md`). Vacuum here
  affects *thermodynamics*, not kinetics.
- 373 K is already outside Liu's 308–328 K fit window, so the desorption
  isotherm is extrapolated; `P_ratio` multiplies an already-extrapolated `q_e`.
