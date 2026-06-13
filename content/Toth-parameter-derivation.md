---
title: Tóth Parameter Derivation for PEI Monolith (DAC)
tags: [DAC, PEI, toth, isotherm, TSA, TVSA, derivation]
date: 2026-06-03
status: estimate
---

# Tóth Parameter Derivation — PEI-Coated Honeycomb Monolith

> [!abstract] Purpose
> Derive the Tóth isotherm parameters used in the temperature-swing breakthrough
> model for our PEI-coated monolith. We **do not** have a measured isotherm for our
> sorbent. The strategy is: **borrow the isotherm *shape* from Liu et al. (2024),
> anchor the *magnitude* to our own measured capacity.** This is an engineering
> estimate, not a validated fit.

---

## 1. What we measured

From the collaborator's basic experiments (see `qe_calculation.ipynb`):

| Quantity | Symbol | Value | Unit |
|---|---|---|---|
| CO₂ capacity of the PEI | $c_\text{PEI}$ | 50 | mg CO₂ / g PEI |
| Areal PEI loading (3.78 % piece) | $\sigma_1$ | $5.949\times10^{-3}$ | kg PEI / m²·wall |

Convert the capacity to molar units ($M_{\text{CO}_2}=44.009$ g/mol):

$$
c_\text{PEI} = \frac{50\ \text{mg/g}}{44.009\ \text{g/mol}} = 1.1361\ \text{mmol/g}
\;\big(\equiv 1.1361\ \text{mol/kg}\big)
$$

The areal equilibrium loading actually used by the model:

$$
q_e^{\text{meas}} = \sigma_1 \, c_\text{PEI}
= 5.949\times10^{-3}\times1.1361 = 6.76\times10^{-3}\ \text{mol/m}^2
$$

> [!note] Single point, not an isotherm
> This is **one** number — the loading at the conditions the 50 mg/g was measured
> ($\sim$ 400 ppm, CO$_2 \sim$  25 °C). It carries no pressure or temperature dependence
> on its own. That dependence is what we borrow from Liu.

---

## 2. The model we are anchoring to

Tóth isotherm (Liu et al. 2024, Eqs. 3–6), mass basis:

$$
q_e^{\text{mmol/g}}(p,T) = n_s(T)\,\theta(p,T),
\qquad
\theta(p,T) = \frac{b(T)\,p}{\big[1+(b(T)\,p)^{t_T(T)}\big]^{1/t_T(T)}}
$$

with three temperature laws:

$$
b(T)=b_0\exp\!\Big[\tfrac{\Delta H_0}{R T_0}\big(\tfrac{T_0}{T}-1\big)\Big]
\qquad\text{(van 't Hoff — affinity)}
$$

$$
n_s(T)=n_{s0}\,\underbrace{\exp\!\big[\chi(1-\tfrac{T}{T_0})\big]}_{f_{ns}(T)}
\qquad
t_T(T)=t_{T0}+\alpha\big(1-\tfrac{T_0}{T}\big)
\qquad\text{(empirical)}
$$

**Liu's "shape" parameters** (fit to Sujan PEI/silica fibre, §3.4):

| Symbol       | Value             | Unit    | Role                   |
| ------------ | ----------------- | ------- | ---------------------- |
| $T_0$        | 308               | K       | reference temperature  |
| $b_0$        | $6.2\times10^{3}$ | kPa⁻¹   | affinity at $T_0$      |
| $t_{T0}$     | 0.40              | –       | Tóth exponent at $T_0$ |
| $\Delta H_0$ | $210\times10^{3}$ | J/mol   | heat of adsorption     |
| $\chi$       | 6.6               | –       | $n_s(T)$ coefficient   |
| $\alpha$     | 10.8              | –       | $t_T(T)$ coefficient   |
| $R$          | 8.314             | J/mol·K | gas constant           |

The areal conversion to the model's units ($\rho_s = \sigma$, kg PEI/m²):

$$
q_e\,[\text{mol/m}^2] = q_e^{\text{mmol/g}}\times \rho_s
\qquad(\text{since } \text{mmol/g}=\text{mol/kg numerically})
$$

---

## 3. Anchoring $n_{s0}$ — the derivation

> [!tip] Key observation
> $n_s$ enters the Tóth equation as a **linear prefactor**. So given one measured
> point $q_e^{\text{meas}}$ at a known condition $(p^*,T^*)$, we solve for $n_{s0}$
> in **one step** — no curve fitting required.

Set the model equal to the measurement at the measurement condition:

$$
c_\text{PEI} = q_e^{\text{mmol/g}}(p^*,T^*) = n_{s0}\,f_{ns}(T^*)\,\theta(p^*,T^*)
$$

Solve:

$$
\boxed{\,n_{s0} = \dfrac{c_\text{PEI}}{f_{ns}(T^*)\,\theta(p^*,T^*)}\,}
$$

Liu supplies $b_0,t_{T0},\Delta H_0,\chi,\alpha$ → the **shape**.
Our experiment supplies $c_\text{PEI}$ → the **height**.

### Measurement condition

Standard atmosphere, ambient CO₂:

$$
T^* = 298.15\ \text{K} \ (25\,°\text{C}),
\qquad
p^* = y_{\text{CO}_2}\,P_\text{tot} = (400\times10^{-6})(101.325) = 0.04053\ \text{kPa}
$$

---

## 4. Worked numbers

Evaluate the temperature laws at $T^* = 298.15$ K.

**Affinity** (with $\Delta H_0/(R T_0) = 82.01$):

$$
b^* = 6.2\times10^{3}\exp\!\big[82.01\,(\tfrac{308}{298.15}-1)\big]
= 6.2\times10^{3}\times e^{2.710}
= 9.31\times10^{4}\ \text{kPa}^{-1}
$$

**Shape and capacity factors** — here the guard applies (see §5): since $T^*<T_0$,

$$
t_T^* = t_{T0} = 0.40, \qquad f_{ns}^* = 1
$$

**Dimensionless loading**:

$$
b^*p^* = 9.31\times10^{4}\times0.04053 = 3774
\quad\Rightarrow\quad
\theta^* = \frac{3774}{\big[1+3774^{0.40}\big]^{2.5}} = \frac{3774}{4133} = 0.913
$$

**Result**:

$$
n_{s0} = \frac{1.1361}{1\times0.913} = \mathbf{1.244\ \text{mmol/g}}
$$

> [!success] Verification
> Back-substitute: $q_e = n_{s0} f_{ns}^* \theta^* \rho_s
> = 1.244\times1\times0.913\times5.949\times10^{-3}
> = 6.76\times10^{-3}\ \text{mol/m}^2$
> — reproduces $q_e^{\text{meas}}$ exactly (rel. error $0$). The anchor holds by construction.

---

## 5. The sub-$T_0$ guard

> [!warning] Why the guard exists
> $\chi$ and $\alpha$ are **empirical** fits valid only over Liu's data range
> (308–328 K). Below $T_0 = 308$ K they must **not** be extrapolated.

If $\alpha$ is naively applied at 298 K:

$$
t_T = 0.40 + 10.8\big(1-\tfrac{308}{298.15}\big) = 0.40 - 0.357 \approx 0.043
$$

A near-zero Tóth exponent makes $\big[1+(bp)^{t_T}\big]^{1/t_T}$ explode (you raise a
number to the power $1/0.043\approx23$), so $\theta\to10^{-6}$ and $n_{s0}$ blows up to
$\sim10^{5}$ — pure extrapolation artifact.

**Guard rule:** for $T<T_0$, freeze the empirical laws at their reference values:

$$
t_T = t_{T0},\qquad f_{ns}=1
$$

The thermodynamic $b(T)$ (van 't Hoff) is **left untouched** — extrapolating it
modestly is physically defensible, which is why $b^*$ still rises to $9.31\times10^4$.

---

## 6. The estimate simplification ($\chi=\alpha=0$)

For a first estimate we go one step further and **drop the empirical temperature
laws entirely**:

$$
\chi = 0,\qquad \alpha = 0
\quad\Longrightarrow\quad
n_s(T)=n_{s0}\ \text{(const)},\quad t_T(T)=t_{T0}\ \text{(const)}
$$

> [!note] What this costs — almost nothing
> - The **temperature swing survives**: it is carried by $b(T)$ through
>   $\Delta H_0 = 210$ kJ/mol (van 't Hoff). At 373 K, $b$ collapses by orders of
>   magnitude regardless of $\chi,\alpha$.
> - $\chi,\alpha$ only added the *secondary* temperature drift of capacity/shape —
>   noise at the estimate level.
> - With $\chi=\alpha=0$, the guard is moot, $T_0$ is irrelevant, and the 298 K
>   degeneracy never arises.

**Plain-language assumption:** *our PEI has Liu's isotherm shape and heat of
adsorption, scaled to our measured capacity.*

### Final parameter set (model input)

| Parameter | Value | Source |
|---|---|---|
| $n_{s0}$ | **1.244 mmol/g** | anchored to our measurement (§4) |
| $b_0$ | $6.2\times10^3$ kPa⁻¹ | Liu (shape) |
| $t_{T0}$ | 0.40 | Liu (shape) |
| $\Delta H_0$ | $210\times10^3$ J/mol | Liu — drives the swing |
| $T_0$ | 308 K | Liu (irrelevant while $\chi=\alpha=0$) |
| $\chi$ | 0 | dropped |
| $\alpha$ | 0 | dropped |
| $\rho_s$ | $5.949\times10^{-3}$ kg/m² | our areal loading $\sigma_1$ |

---

## 7. Role of pressure

> [!info] Pressure is not an independent variable in this model
> It enters **only** as the CO₂ *partial* pressure inside the isotherm:
> $$ p\,[\text{kPa}] = \frac{C\,R\,T}{1000} $$
> derived from the local gas concentration $C$ via ideal gas. There is no
> total-pressure field, no momentum/Ergun equation.

Consequences:
- Pressure moves $q_e$ along the $b\!\cdot\!p$ axis of the isotherm.
- **Lowering** partial pressure → lower $q_e$ → larger driving force
  $k_s(q_e - q_\text{wall})$ → drives **desorption**.
- The existing desorption purge (`desorption_iC = 0`, `u_max_des`) is already a
  *concentration*-swing analog of vacuum.

---

## 8. TVSA possibility — the vacuum factor

To make this a temperature–**vacuum** swing, add one dimensionless knob
$P_\text{ratio} = P_\text{vac}/P_\text{atm}$ that scales the partial pressure during
desorption:

$$
p\,[\text{kPa}] = \frac{C\,R\,T}{1000}\times P_\text{ratio}
$$

- At $T_\text{des}=100\,°$C, $b$ is tiny → $b p \ll 1$ → isotherm is in its **linear**
  limit $q_e \approx n_s b p$. There $q_e$ scales **directly** with $P_\text{ratio}$,
  so e.g. $P_\text{ratio}=0.1$ (0.1 bar) cuts the residual heel $\sim$10×.
- $P_\text{ratio}=1$ during adsorption (atmospheric) leaves the breakthrough curve
  unchanged.

> [!warning] Honest caveat
> $P_\text{ratio}$ is a **lumped equilibrium proxy** for the extra evacuation that
> the simplified desorption transport does not resolve — not a true pressure solve.
> A rigorous version needs a momentum/Ergun field. See `vacuum-factor-proposal.md`.

---

## 9. Assumptions ledger

> [!caution] What is assumed (not measured/fit for our sorbent)
> 1. **Liu's isotherm shape transfers** to our PEI ($b_0, t_{T0}, \Delta H_0$).
> 2. **$\chi=\alpha=0$** — no empirical temperature drift of capacity/shape.
> 3. The **temperature swing magnitude rests entirely on $\Delta H_0$** (Liu), which
>    cannot be validated from a single capacity point.
> 4. The 50 mg/g was measured at **$\sim$400 ppm, 25 °C** (confirm with collaborator;
>    35 °C would give $n_{s0}\approx1.47$ instead).
> 5. $T_\text{des}=100\,°$C is **outside Liu's 308–328 K fit window** — extrapolated.
> 6. Kinetics ($k_s$) are borrowed and held constant across temperature (no Arrhenius).

---

## References

- Liu, Lin, Dai, Jiang. *Minimal Kinetic Model of Direct Air Capture of CO₂ by
  Supported Amine Sorbents in Dry and Humid Conditions.* Ind. Eng. Chem. Res. 2024,
  63, 5871–5879. (Tóth parameters: §3.4)
- Sujan et al. 2019 — PEI-loaded polymer/silica fibre sorbents (Liu's fit target).
- Local: `qe_calculation.ipynb` (§9), `vacuum-factor-proposal.md`,
  `code/main-pei-tsa.py`.
