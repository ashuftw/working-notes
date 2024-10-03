---
title: Law of the Wall and Wall Units
draft: false
date: 2024-06-13
---

![[Pasted image 20240617115121.png|center|600]]

## Assumption
The turbulence near the a wall/solid boundary is only affected by the flow conditions at the wall and is independent of the flow conditions far away. 

$$
\text {or}
$$

In the Outer Layer, the Turbulence is not affected by the the turbulence in the inner layer due to the huge difference in the Length scales ($\delta$)
## Wall Units / Plus Values
Using the above assumption, a few flow variables are identified. 
- $y\rightarrow$ distance from the wall $[L]$.
- $\bar{u}(y)\rightarrow$  Mean velocity (or velocity profile) $[L / T]$.
- $\tau_W\rightarrow$ Shear stress at the wall $\left[M / L T^2\right]$.
- $\rho\rightarrow$ Fluid Density $\left[M / L^3\right]$.
- $\nu \rightarrow$ Fluid kinematic viscosity $\left[L^2 / T\right]$.
After performing dimensional analysis we derive two new dimensionless quantities
## Dimensionless Distance $y+$

$$
\boxed{
y^{+} \equiv \frac y \nu \sqrt{\frac{\tau_W}{\rho}} = \frac{y u_\tau}{\nu}=\frac{y}{\delta_v}
}
$$

Easier to remember 

$$
\boxed{
y^{+} =\frac{y}{\delta_v} =  \frac{y u_\tau}{\nu}= \frac y \nu \sqrt{\frac{\tau_W}{\rho}}
}
$$

## Dimensionless Velocity $u+$

$$
\boxed{u^{+} \equiv \frac{u}{u_\tau}}
$$


Where, 
- $y\rightarrow$ Distance from the wall
- $u_\tau = \sqrt{\tau/\rho} \rightarrow$ Friction Velocity 
- $\delta_v\rightarrow$ Length Scale in the Inner layer 

> Note: In theory, the $u^+$ is only a function of $y+$, i.e, the assumption. 

---
# References
1. http://brennen.caltech.edu/fluidbook/basicfluiddynamics/turbulence/lawofthewall.pdf