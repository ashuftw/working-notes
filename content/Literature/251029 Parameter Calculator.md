---
title: Parameter Calculator
draft: true
tags:
date: 2025-10-29
---
## Dimensionless Numbers

### Eötvös Number (Eo) [^1]

The ratio of buoyancy forces to surface tension forces:



$$
\text{Eo} = \frac{g \cdot \Delta\rho \cdot d^2}{\sigma}
$$



Where ,
- $\Delta\rho = \rho_{\text{droplet}} - \rho_{\text{medium}}$
- $g\rightarrow$ Gravitational acceleration
- $d\rightarrow$ Droplet diameter
- $\sigma\rightarrow$ Surface Tension


### Morton Number (M)

The ratio of viscous forces to surface tension forces:



$$
\text{M} = \frac{g \cdot \mu_{\text{medium}}^4}{\rho_{\text{medium}} \cdot \sigma^3}
$$


### Viscosity Ratio
$$
\lambda = \frac{\mu_d}{\mu_m}
$$

Where:
- $\mu_d$ = droplet dynamic viscosity (Pa·s)
- $\mu_m$ = medium dynamic viscosity (Pa·s)

---

## Primary Calculations

### Density Difference
$$
\Delta\rho = \rho_d - \rho_m
$$

Where:
- $\rho_d$ = droplet density (kg/m³)
- $\rho_m$ = medium density (kg/m³)

### Droplet Diameter (from Eötvös Number)
Rearranging the Eötvös number equation to solve for diameter:

$$
d = \sqrt{\frac{Eo \cdot \sigma}{g \cdot \Delta\rho}}
$$

> [!note] Note
> This formula adjusts the droplet diameter to achieve the target Eötvös number while maintaining realistic water density (1000 kg/m³).


### Medium Viscosity (from Morton Number)
Rearranging the Morton number equation to solve for medium viscosity:

$$
\mu_m = \left(\frac{Mo \cdot \rho_m \cdot \sigma^3}{g}\right)^{1/4}
$$

### Droplet Viscosity
$$\boxed{
\mu_d = \lambda \cdot \mu_m
}$$

Where $\lambda$ is the viscosity ratio.

---

## Terminal Velocity Calculation

### Hadamard-Rybczynski Equation
For a spherical droplet with internal circulation:
$$
u_t = \frac{2 \cdot R^2 \cdot g \cdot (\rho_{\text{droplet}} - \rho_{\text{medium}}) \cdot (\mu_{\text{droplet}} + \mu_{\text{medium}})}{3 \cdot \mu_{\text{droplet}} \cdot (2\mu_{\text{droplet}} + 3\mu_{\text{medium}})}
$$
In terms of $d$
$$
u_{terminal} = \frac{g \cdot d^2 \cdot \Delta\rho \cdot (\mu_d + \mu_m)}{6 \cdot \mu_d \cdot (2\mu_d + 3\mu_m)}
$$

> [!warning] Assumptions
> - Spherical droplet shape
> - Low Reynolds number (Stokes flow regime)
> - Internal circulation allowed (unlike solid sphere)
> - No contamination at interface

---

## Verification Formulas

### Eötvös Number Verification
$$
Eo_{calc} = \frac{g \cdot \Delta\rho \cdot d^2}{\sigma}
$$

Should match input $Eo$ value.

### Morton Number Verification
$$
Mo_{calc} = \frac{g \cdot \mu_m^4}{\rho_m \cdot \sigma^3}
$$

Should match input $Mo$ value.

### Error Calculation
$$
\text{Error (\%)} = \left|\frac{X_{calculated} - X_{input}}{X_{input}}\right| \times 100
$$

---

## Additional Parameters

### Density Ratio
$$
\rho_{ratio} = \frac{\rho_d}{\rho_m}
$$

For water-air system: $\rho_{ratio} \approx 816$ (1000 kg/m³ / 1.225 kg/m³)

---

## Typical Values for Water-Air System

| Parameter | Symbol | Value | Units |
|-----------|--------|-------|-------|
| Surface Tension | $\sigma$ | 0.072 | N/m |
| Air Density | $\rho_m$ | 1.225 | kg/m³ |
| Water Density | $\rho_d$ | 1000 | kg/m³ |
| Gravity | $g$ | 9.81 | m/s² |
| Density Difference | $\Delta\rho$ | 998.775 | kg/m³ |

---

## Implementation Notes

> [!tip] Calculation Order
> 1. Calculate $\Delta\rho$ from densities
> 2. Calculate diameter $d$ from $Eo$
> 3. Calculate $\mu_m$ from $Mo$
> 4. Calculate $\mu_d$ from viscosity ratio
> 5. Calculate terminal velocity
> 6. Verify $Eo$ and $Mo$ match inputs

> [!example] Example Calculation
> **Inputs:**
> - $Eo = 16.2$
> - $Mo = 3.13 \times 10^{-5}$
> - $\lambda = 55.0$
>
> **Results:**
> - Droplet diameter adjusted to satisfy $Eo$ with realistic water density
> - All properties calculated to maintain dimensional consistency
> - Terminal velocity predicted from Hadamard-Rybczynski theory

---

## References

- **Hadamard-Rybczynski Theory**: Terminal velocity for fluid droplets with internal circulation
- **Eötvös Number**: Dimensionless parameter in two-phase flow
- **Morton Number**: Relates fluid properties in bubble/droplet dynamics
- Related to Grace diagram for bubble/droplet shape regimes



[^1]: https://en.wikipedia.org/wiki/E%C3%B6tv%C3%B6s_number