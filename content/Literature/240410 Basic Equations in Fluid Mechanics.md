---
title: Basic Equations in Fluid Mechanics
draft: false
tags:
---
## Continuity
$$
\frac{\partial u_j}{\partial x_j}=0
$$

## Momentum in $i$
$$
\overbrace{\frac{\partial u_i}{\partial t}}^{\text {Temporal Acceleration }}+\underbrace{u_j \frac{\partial u_i}{\partial x_j}}_{\text {Convective Acceleration }}=-\overbrace{\frac{1}{\rho} \frac{\partial p}{\partial x_i}}^{\text {Pressure}}+\underbrace{\nu \frac{\partial^2 u_i}{\partial x_j^2}}_{\text {Viscous Diffusion }}+\overbrace{g_i}^{\text {Body Force }}
$$
$$\frac{\partial \vec{u}}{\partial t}+\vec{u} \cdot \nabla \vec{u}=-\frac{1}{\rho} \nabla p+\nu \nabla^2 \vec{u}+\vec{g}$$


## Kinetic energy
$$
\frac{\partial e}{\partial t}+u_j \frac{\partial e}{\partial x_j}=-\frac{1}{\rho} u_j \frac{\partial p}{\partial x_j}+v \frac{\partial^2 e}{\partial x_j^2}+v \frac{\partial^2\left(u_i u_j\right)}{\partial x_i \partial x_j}-2 v S_{i j}^2+u_i g_i
$$

## Vorticity in $i$ 
$$
\frac{\partial \omega_i}{\partial t}+u_j \frac{\partial \omega_i}{\partial x_j}=\omega_j \frac{\partial u_i}{\partial x_j}+v \frac{\partial^2 \omega_i}{\partial x_j^2}
$$

## Poisson's equation for pressure
$$
-\frac{1}{\rho} \frac{\partial^2 p}{\partial x_i^2}=S_{i j}^2-d
$$
where,
- $S_{i j}=\frac{1}{2}\left(\frac{\partial u_i}{\partial x_j}+\frac{\partial u_j}{\partial x_i}\right)$ is the Strain Rate Tensor
- $d$ is the Dissipation rate of Turbulent Kinetic Energy
 
> Note: $d$ is different from $k$ which is the Turbulent Kinetic Energy per unit mass in the system. 

 