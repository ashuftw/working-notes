---
tags: [DAC, adsorption, modeling, TSA, derivation]
source: "Liu et al. (2024) - Minimal Kinetic Model of DAC of CO2 by Supported Amine Sorbents"
---

# Temperature-Dependent Adsorption Equilibrium and Kinetics

## 1. Equilibrium Adsorption Capacity $q_e$

### 1.1 The Toth Isotherm

The equilibrium adsorption capacity $q_e$ is given by the **Toth isotherm**:

$$q_e = \frac{n_s \, b \, p}{\left(1 + (b p)^{t_T}\right)^{1/t_T}}$$

**Terms:**
- $q_e$ — equilibrium adsorption capacity [mmol/g]: the amount of CO₂ adsorbed per gram of sorbent when the gas and solid phases are in equilibrium at a given temperature and pressure
- $n_s$ — saturation adsorption capacity [mmol/g]: the maximum amount of CO₂ the sorbent can hold when fully saturated; sets the upper bound of $q_e$
- $b$ — adsorption affinity [atm⁻¹ or kPa⁻¹]: describes how strongly CO₂ binds to the sorbent; a larger $b$ means stronger binding and higher $q_e$ at the same pressure
- $p$ — partial pressure of CO₂ in the gas phase [atm or kPa]: the thermodynamic driving force for adsorption; related to molar concentration by the ideal gas law $p = C_A R T$
- $t_T$ — Toth heterogeneity exponent [dimensionless]: accounts for energetic heterogeneity of the sorbent surface; when $t_T = 1$ the Toth isotherm reduces to the Langmuir isotherm; smaller $t_T$ means more heterogeneous surface

> [!note] Physical interpretation of Toth
> The Toth model generalises the Langmuir isotherm to account for the fact that real amine sorbent surfaces are not energetically uniform — different amine sites bind CO₂ with different strengths. The exponent $t_T$ captures this heterogeneity. As $bp \to 0$ (dilute, DAC-relevant conditions), $q_e \approx n_s b p$, i.e. a linear (Henry's law) regime.

---

### 1.2 Temperature Dependence of $b(T)$ — the Van't Hoff equation

The adsorption affinity depends on temperature via the **Van't Hoff equation**:

$$b(T) = b_0 \exp\!\left[\frac{\Delta H_0}{R T_0}\!\left(\frac{T_0}{T} - 1\right)\right]$$

which is equivalently written in standard Van't Hoff form as:

$$b(T) = b_0 \exp\!\left[\frac{\Delta H_0}{R}\!\left(\frac{1}{T} - \frac{1}{T_0}\right)\right]$$

**Terms:**
- $b_0$ — adsorption affinity at the reference temperature $T_0$ [atm⁻¹ or kPa⁻¹]
- $\Delta H_0$ — isosteric heat of adsorption at near-zero loading [J/mol]: the energy released when one mole of CO₂ binds to the sorbent; defined here as a **positive** quantity (exothermic convention used in the paper); typical values for amine sorbents are 50–210 kJ/mol
- $R$ — universal gas constant = 8.314 J/(mol·K)
- $T_0$ — reference temperature [K]: the temperature at which the isotherm parameters were originally fitted
- $T$ — operating temperature [K]

> [!important] Physical interpretation
> Since adsorption is exothermic ($\Delta H_0 > 0$ as defined), the exponential factor decreases as $T$ increases. Therefore:
> - **Low T** → large $b(T)$ → strong binding → large $q_e$ → **adsorption favoured** ✓  
> - **High T** → small $b(T)$ → weak binding → small $q_e$ → **desorption favoured** ✓  
>
> This is the thermodynamic basis of Temperature Swing Adsorption (TSA).

**Derivation from thermodynamics:** The Van't Hoff equation follows directly from the Gibbs-Helmholtz equation applied to adsorption equilibrium:
$$\frac{d \ln b}{d(1/T)} = \frac{\Delta H_0}{R}$$
Integrating from $T_0$ to $T$ yields the expression above.

---

### 1.3 Temperature Dependence of $n_s(T)$

The saturation capacity declines with temperature:

$$n_s(T) = n_{s0} \exp\!\left[\chi\!\left(1 - \frac{T}{T_0}\right)\right]$$

**Terms:**
- $n_{s0}$ — saturation capacity at reference temperature $T_0$ [mmol/g]
- $\chi$ — empirical decay parameter [dimensionless]: controls how rapidly $n_s$ decreases with increasing temperature; physically reflects the loss of accessible amine sites at high temperature (e.g. due to amine aggregation or pore blocking)

> [!note]
> When $T = T_0$, the exponential equals 1 and $n_s = n_{s0}$. For $T > T_0$, the argument $(1 - T/T_0)$ becomes negative, so $n_s < n_{s0}$. The capacity decreases monotonically with temperature.

---

### 1.4 Temperature Dependence of $t_T(T)$

The heterogeneity exponent varies linearly with temperature:

$$t_T(T) = t_{T0} + \alpha\!\left(1 - \frac{T_0}{T}\right)$$

**Terms:**
- $t_{T0}$ — Toth exponent at reference temperature $T_0$ [dimensionless]
- $\alpha$ — empirical parameter [dimensionless]: controls the sensitivity of the surface heterogeneity to temperature; a non-zero $\alpha$ means the shape of the isotherm itself changes with temperature

> [!note]
> When $T = T_0$, $t_T = t_{T0}$. This term is a small correction but matters when fitting isotherm data across a wide temperature range, especially for strongly heterogeneous amine sorbents.

---

### 1.5 Full Expression for $q_e(T, p)$

Combining all three temperature-dependent parameters, the complete equilibrium capacity as a function of temperature and CO₂ partial pressure is:

$$\boxed{q_e(T,p) = \frac{n_s(T) \cdot b(T) \cdot p}{\left(1 + \left(b(T)\, p\right)^{t_T(T)}\right)^{1/t_T(T)}}}$$

where:

$$b(T) = b_0 \exp\!\left[\frac{\Delta H_0}{R}\!\left(\frac{1}{T} - \frac{1}{T_0}\right)\right]$$

$$n_s(T) = n_{s0} \exp\!\left[\chi\!\left(1 - \frac{T}{T_0}\right)\right]$$

$$t_T(T) = t_{T0} + \alpha\!\left(1 - \frac{T_0}{T}\right)$$

**Fitted parameters for PEI-silica fiber sorbents** (from Table in Section 3.4 of the paper, validated against DAC breakthrough experiments at 380 ppm CO₂):

| Parameter | Value | Units |
|-----------|-------|-------|
| $T_0$ | 308 | K (35°C) |
| $n_{s0}$ | 0.81 | mmol/g |
| $b_0$ | 6.2 × 10³ | kPa⁻¹ |
| $\Delta H_0$ | 210 | kJ/mol |
| $t_{T0}$ | 0.40 | — |
| $\chi$ | 6.6 | — |
| $\alpha$ | 10.8 | — |

---

## 2. Kinetic Rate Constant $k_s(T)$

### 2.1 The LDF Kinetic Model

The rate of adsorption is described by the **Linear Driving Force (LDF)** model:

$$\frac{dq}{dt} = k_s \left(q_e - q\right)$$

**Terms:**
- $dq/dt$ — rate of change of adsorbed CO₂ [mmol/(g·s)]: how fast the sorbent is taking up (or releasing) CO₂
- $k_s$ — LDF mass transfer coefficient [s⁻¹]: a lumped kinetic parameter that combines all mass transfer resistances (external film diffusion, macropore diffusion, micropore diffusion, and surface reaction) into a single constant
- $q_e$ — equilibrium adsorption capacity [mmol/g]: the value the system is driving toward (defined in Section 1)
- $q$ — instantaneous adsorbed loading [mmol/g]: the current amount of CO₂ on the sorbent

> [!important] Physical interpretation
> The LDF model says the adsorption rate is proportional to how far the system is from equilibrium $(q_e - q)$:
> - When $q < q_e$: the driving force is positive → **adsorption** occurs
> - When $q > q_e$: the driving force is negative → **desorption** occurs automatically
>
> This means that during TSA, raising T lowers $q_e(T)$ below the current $q$, reversing the sign of the flux and causing desorption — **no separate desorption equation is needed**.

---

### 2.2 Temperature Dependence of $k_s(T)$ — Arrhenius equation

The uptake rate constant follows an **Arrhenius** relationship:

$$k_s(T) = k_{s,\text{ref}} \exp\!\left[\frac{-E_a}{R}\!\left(\frac{1}{T} - \frac{1}{T_\text{ref}}\right)\right]$$

**Terms:**
- $k_{s,\text{ref}}$ — LDF rate constant at reference temperature $T_\text{ref}$ [s⁻¹]: fitted from breakthrough experiments at a known temperature
- $E_a$ — activation energy for adsorption [J/mol]: the energy barrier CO₂ molecules must overcome to diffuse through the amine layer and bind; for PEI-silica sorbents the paper reports $E_a = 38 \pm 14$ kJ/mol
- $R$ — universal gas constant = 8.314 J/(mol·K)
- $T_\text{ref}$ — reference temperature [K]: the temperature at which $k_{s,\text{ref}}$ was determined

> [!note] Physical interpretation
> Unlike $q_e$, which **decreases** with temperature (thermodynamic effect), $k_s$ **increases** with temperature (kinetic effect). These two effects compete during TSA:
> - Higher T → faster kinetics (larger $k_s$) → steeper breakthrough
> - Higher T → lower capacity (smaller $q_e$) → earlier breakthrough
>
> The paper confirms both effects: at 55°C, the rate constant is 0.1 min⁻¹ vs. 0.04 min⁻¹ at 35°C, while $q_e$ at 55°C is roughly half that at 35°C.

**Derivation:** The Arrhenius equation comes from transition state theory. Taking the natural log:
$$\ln k_s = \ln k_{s,\text{ref}} - \frac{E_a}{R}\!\left(\frac{1}{T} - \frac{1}{T_\text{ref}}\right)$$
This is linear in $1/T$, so $E_a$ can be obtained from the slope of an Arrhenius plot ($\ln k_s$ vs. $1/T$) fitted to breakthrough experiments at multiple temperatures.

---

## 3. Summary

| Quantity | Equation | Physical meaning |
|----------|----------|-----------------|
| $q_e(T,p)$ | Toth isotherm with T-dependent $b$, $n_s$, $t_T$ | How much CO₂ the sorbent *can* hold at equilibrium |
| $b(T)$ | Van't Hoff: decreases with T | Binding strength decreases at high T |
| $n_s(T)$ | Exponential decay with T | Active sites lost at high T |
| $t_T(T)$ | Linear in $T_0/T$ | Surface heterogeneity changes with T |
| $k_s(T)$ | Arrhenius: increases with T | Faster diffusion at high T |
| $dq/dt$ | $k_s(q_e - q)$ | Net adsorption rate; negative = desorption |

> [!summary] Key insight for TSA
> During **adsorption** (low T): $q_e$ is large, $k_s$ is small — slow but high-capacity uptake.  
> During **desorption** (high T): $q_e$ drops below $q$, the LDF driving force reverses, and $k_s$ is large — fast release of concentrated CO₂.