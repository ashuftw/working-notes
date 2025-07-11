---
title: DAC Parameter Calculation
draft: true
tags: 
date: 2024-11-13
---
Starting with $400 \text{ ppm}$ of $\text{CO2}$ in air => $400 \times 10^{-6}$ mole fraction

**Ideal Gas Law** 
$$
PV = nRT
$$

 where,
- $P$ = Pressure $\text{[atm]}$
- $V$ = Volume $\text{[L]}$
- $n$ = Number of moles $\text{[mol]}$
- $R$ = Universal gas constant $0.08206\frac{\text{L}\cdot\text{atm}}{\text{mol}\cdot\text{K}}$ [^1]
- $T$ = Temperature $\text{[K]}$

**Converting to Concentration** 
$$
C = \frac{n}{V} = \frac{P}{RT}
$$


**Substituting Values** 
$$
C = \frac{1 \times 400 \times 10^{-6}}{0.08206 \times 298.15}
$$



$$
C = \frac{0.0004}{0.08206 \times 298.15} = 1.63 \times 10^{-5} \text{mol}\, \text{L}^{-1}
$$


**Converting to m³** 


$$
C = 0.0163\, \text{mol}\, \text{m}^{-3}
$$


This final value of $0.0163 \frac{\text{mol}}{\text{m}^3}$ is the molar concentration of $\text{CO2}$ that can be used as $C_A$ in the mass transfer equations.

### Equilibrium Adsorption Capacity

Starting with experimental value: 2.37[^2] $\text{mmol g}^{-1}$ of adsorbent

**Converting to surface concentration** Using BET surface area = 894 m²/g


$$
q_e = \frac{2.37 \times 10^{-3} \text{ mol}\cdot\text{g}^{-1}}{894 \text{ m}^2\cdot\text{g}^{-1}} = 2.65 \times 10^{-6} \text{ mol}\cdot\text{m}^{-2}
$$


The final value $q_e = 2.65 \times 10^{-6} \text{ mol}\cdot\text{m}^{-2}$ represents the equilibrium surface concentration of CO2 per unit area of adsorbent which an be plugged into


$$
\dot{q}(t) = k_s(q_e - q)
$$


where:
- $q_e$ = equilibrium surface concentration $[\text{mol}\cdot\text{m}^{-2}]$
- $q$ = instantaneous surface concentration $[\text{mol}\cdot\text{m}^{-2}]$
- $k_s$ = adsorption kinetics constant $[\text{m}\cdot\text{s}^{-1}]$
- $\dot{q}(t)$ = molar flux through adsorbent surface $[\text{mol}\cdot\text{m}^{-2}\cdot\text{s}^{-1}]$

[^1]: https://en.wikipedia.org/wiki/Gas_constant
[^2]: [[Darunte et al. (2017)]]
