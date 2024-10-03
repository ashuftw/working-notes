---
title: Reynolds Averaged Navier Stokes (RANS)
draft: false
date: 2024-08-13
---

## Use case 
It is  a method of turbulence modeling where the Time Averaged Navier-Stokes equations are used. 
![[Pasted image 20240813114101.png|center|500]]
This means that any property $f$ is split into its *averaged* and *fluctuating* components. 

$$
f(\vec{x}, t)=\bar{f}(\vec{x})+f^{\prime}(\vec{x}, t)
$$

Rearranging and taking integral

$$
\bar{f}(\vec{x})=\lim _{\Delta T \rightarrow \infty} \frac{1}{\Delta T} \int_{-\Delta T / 2}^{\Delta T / 2} f(\vec{x}, t) d t
$$

The **RANS** Equations are formulated taking the [[240424 Time Averaged Navier-Stokes Equations|Time Average of the Navier Stokes Equations]]
- **Continuity Equation**

$$
\boxed{\frac{\partial \bar{u}_j}{\partial x_j}=0 }
$$

- **Momentum Equations**
 
$$
\frac{\partial \bar{u}_i}{\partial t}+\frac{\partial \bar{u}_i \bar{u}_j}{\partial x_j}+\frac{\partial \overline{u_i^{\prime} u_j^{\prime}}}{\partial x_j}=-\frac{1}{\rho} \frac{\partial \bar{p}}{\partial x_i}+v \frac{\partial^2 \bar{u}_i}{\partial x_j^2}
$$

 Rearranging

$$
\boxed{
\frac{\partial \bar{u}_i}{\partial t}+\frac{\partial \bar{u}_i \bar{u}_j}{\partial x_j}=-\frac{1}{\rho} \frac{\partial \bar{p}}{\partial x_i}+\frac{\partial}{\partial x_j}\left[v \frac{\partial\bar u_i}{\partial x_j}+\tau_{i j}^{t u r b}\right]}
$$

where $\tau_{i j}^{t u r b} = -\overline{u_i' u_j'}$  represents the [[240813 Reynolds Stress Tensor and Turbulent Shear Stress|Reynolds Stresses]]




---
# References
**Pg. 698** The Finite Volume Method - Moukalled