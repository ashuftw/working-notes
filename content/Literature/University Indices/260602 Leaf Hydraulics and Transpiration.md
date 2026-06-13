---
title: Leaf Hydraulics and Transpiration
draft: true
tags:
date: 2026-06-02
---
![[../../Files/Pasted image 20260602115031.png]]
Things that influence the degree of opening of the Guard cells 
- CO2 
- Water vapour 
- Sunlight 
- Wind-speed at the leaf surface (in relation the boundary layer) also has an impact 


![[../../Files/Pasted image 20260602115543.png|250|center]]
- Stomata opens up also to other gases
- The opening mechanism is due to hormones. Exact mechanism isn't known 

![[../../Files/Pasted image 20260602120011.png|center|400]]
$C_i$ - 
![[../../Files/Pasted image 20260602120833.png]]
Number between: 1.6 comes appears as a conversion factor between conductance

![[../../Files/Pasted image 20260602121016.png]]
s-> stem 
L-> leaf
E -> transpiration

Note: When the conditions are dry embolism happens ?? 

![[../../Files/Pasted image 20260602122703.png]]
- not suitable for low carbon uptake 
![[../../Files/Pasted image 20260602122900.png]]
An- carbon assimilation rate 
VPD - vapour pressure deficit 

Are stomata really optimising?
- we don't know 



 The model you're anchoring to

  Tóth, mass basis:

  $$q_e^{\text{mmol/g}}(p,T) = n_s(T)\cdot\underbrace{\frac{b(T),p}{\left[1+(b(T),p)^{t_T(T)}\
  right]^{1/t_T(T)}}}_{\equiv;\theta(p,T)\ \text{(dimensionless, 0–1)}}$$

  with the three temperature laws:

  $$b(T)=b_0\exp!\Big[\tfrac{\Delta H_0}{RT_0}\big(\tfrac{T_0}{T}-1\big)\Big],\quad
  n_s(T)=n_{s0},\underbrace{\exp!\big[\chi(1-\tfrac{T}{T_0})\big]}{\equiv,f{ns}(T)},\quad
  t_T(T)=t_{T0}+\alpha\big(1-\tfrac{T_0}{T}\big)$$

  The key insight

  ns0 appears linearly out front — it's a pure magnitude scale on the whole curve. So you
  don't fit anything. Given one measured point $q_e^*$ at $(p^*,T^*)$, you solve for ns0 in 
  one step:

  $$\boxed{,n_{s0}=\frac{c_{\text{PEI}}}{f_{ns}(T^*);\theta(p^*,T^*)},}$$

  where $c_{\text{PEI}} = 1.136\ \text{mol/kg} = 1.136\ \text{mmol/g}$ is your collaborator's
  measured capacity (note: numerically mmol/g = mol/kg, so this equates at the per-mass level
  and rho_s cancels out — rho_s = sigma stays exactly as the notebook has it).

  Liu supplies $b_0, t_{T0}, \Delta H_0, \chi, \alpha, T_0$ → the shape. Your data supplies
  the height.

  What you actually compute (5 steps)

  ┌──────┬──────────┬─────────────────────────────────────────────────────────┬───────┐
  │ Step │ Quantity │                         Formula                         │ Needs │
  ├──────┼──────────┼─────────────────────────────────────────────────────────┼───────┤
  │ 1    │ b*       │ $b_0\exp[\tfrac{\Delta H_0}{RT_0}(\tfrac{T_0}{T^*}-1)]$ │ $T^*$ │
  ├──────┼──────────┼─────────────────────────────────────────────────────────┼───────┤
  │ 2    │ tT*      │ $t_{T0}+\alpha(1-\tfrac{T_0}{T^*})$                     │ $T^*$ │
  ├──────┼──────────┼─────────────────────────────────────────────────────────┼───────┤
  │ 3    │ f_ns*    │ $\exp[\chi(1-\tfrac{T^*}{T_0})]$                        │ $T^*$ │
  ├──────┼──────────┼─────────────────────────────────────────────────────────┼───────┤
  │ 4    │ θ*       │ $b^*p^*/[1+(b^*p^*)^{t_T^*}]^{1/t_T^*}$                 │ $p^*$ │
  ├──────┼──────────┼─────────────────────────────────────────────────────────┼───────┤
  │ 5    │ ns0      │ $c_{\text{PEI}}/(f_{ns}^*,\theta^*)$                    │ —     │
  └──────┴──────────┴─────────────────────────────────────────────────────────┴───────┘

  The two inputs you're missing

  Everything above needs $T^*$ and $p^*$ — the temperature and CO₂ partial pressure at which 
  the 50 mg/g was measured. That's the whole ballgame. Worked example at $T^*=T_0=308$ K (= 35
  °C, bottom of Liu's range, so steps 1–3 reduce to $b^*=b_0$, $t_T^*=0.40$, $f_{ns}^*=1$):

  - If measured at 15 % CO₂, 1 atm → $p^*=15.2$ kPa: $b^*p^*=9.4\times10^4$,
  $\theta^*\approx0.975$ → ns0 ≈ 1.17 mmol/g
  - If measured at 400 ppm → $p^*=0.041$ kPa: $b^*p^*=251$, $\theta^*\approx0.770$ → ns0 ≈ 
  1.48 mmol/g

  Same measured capacity, 26 % different ns0 depending only on the pressure it was taken at.
  That's why I keep flagging the measurement condition — it's not a formality.

  The check that the calculation surfaces

  Step 2 has a trap. If your measurement was at 25 °C (298 K), below Liu's $T_0$ = 308 K,
  then:

  $$t_T^* = 0.40 + 10.8,(1-\tfrac{308}{298.15}) = 0.40 - 0.357 \approx 0.043$$

  A Tóth exponent near 0.04 makes $[1+(bp)^{t_T}]^{1/t_T}$ explode, $\theta^*\to10^{-6}$, and
  ns0 blows up to absurd values ($\sim10^5$). Liu's $\alpha$ is only valid for $T \ge T_0$
  (their fit was 308–328 K). So:

  - if $T^* \ge 308$ K → the calc is clean, use it directly;
  - if $T^* < 308$ K → don't extrapolate $\alpha$ below $T_0$; cap $t_T$ at $t_{T0}$ (and
  $\chi$ similarly), or anchor at a condition inside the fit range.

  This is the same "extrapolation outside Liu's window" issue as the 373 K desorption end — it
  just bites at the cold end too.

  Consistency check (free validation)

  After computing ns0, evaluate toth_q_e(p*, T*) — it must return your collaborator's $q_e^*$
  ($6.76\times10^{-3}$ mol/m² for the 3.78 % piece) to machine precision. If it doesn't, the
  anchoring is wrong.

  ---
  So the only things I need from you to make this concrete: what temperature and CO₂ partial
  pressure was the 50 mg/g measured at? Give me those two and I'll compute ns0 and wire it in
  (replacing the current ns0 = 0.81 double-count), with the sub-$T_0$ guard if needed.

✻ Churned for 2m 32s

