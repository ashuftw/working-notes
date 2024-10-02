---
title: Governing Equations
draft: true
tags: 
date: 2024-10-01
---
## First Law of Thermodynamics[^1]
$$ \dot E = \dot{W} + \dot{Q} $$

Where,
- $\dot E\rightarrow$  rate of change of Internal Energy
- $\dot{W}\rightarrow$ rate of work done by external forces
- $\dot{Q}\rightarrow$  rate of heat addition

Using this, one can derive the Conservation of Species. Details. [^2]
## Conservation of Species in a 2D Binary Mixture
Derivation[^3]
$$
\frac{\partial C_A}{\partial t}+u \frac{\partial C_A}{\partial x}+v \frac{\partial C_A}{\partial y}=D_{A B}\left(\frac{\partial^2 C_A}{\partial x^2}+\frac{\partial^2 C_A}{\partial y^2}\right)
$$
where,
- $C_A(x, y, t)\rightarrow$molar concentration of $\mathrm{CO}_2$
- $C_B(x, y, t)\rightarrow$molar concentration of air
- $u(x, y, t),\, v(x, y, t)\rightarrow$velocities in $x$ and $y$
- $D_{A B}$ is the mass diffusivity of the A-B mixture or the Binary Diffusion Coefficient. 

**Note:**
- LHS -> Net Transport of Species $A$ due to advection (bulk fluid motion).
- RHS -> Inflow due to diffusion and production due to chemical reaction (Edit: check the presence of $\dot N$ as shown in [[Fundamentals of heat and mass transfer|Incorpera]])

## Transformation into Cylindrical Coordinates

Assuming fully developed laminar flow within each cell. (Eqn. 1) becomes
$$
\frac{\partial C_A}{\partial t}+u_d \frac{\partial C_A}{\partial x}=D_{A B} \frac{1}{r} \frac{\partial}{\partial r}\left(r \frac{\partial C_A}{\partial r}\right)
$$

where, 
- $u_d=u_m\left(1-\left(\frac{r}{R}\right)^2\right)$ parabolic velocity profile in each cell of diameter $R$ 
- $u_m\rightarrow$ maximum velocity
- $r\rightarrow$ radial coordinate
---
Note that in steady state, Eq. 2 reduces to the thin duct equation
$$
u_d \frac{\partial C_A}{\partial x}=D_{A B} \frac{1}{r} \frac{\partial}{\partial r}\left(r \frac{\partial C_A}{\partial r}\right) .
$$

The DAC problem consists in solving Eq. 2 with the boundary condition
$$
-D_{A B}\left(\frac{\partial C_A}{\partial r}\right)_{r=R}=\dot{q}(t)
$$
where the molar flux $\dot{q}(t)$ of $\mathrm{CO}_2$ through the adsorbent surface is given by the assumed adsorption kinetics
$$
\dot{q}(t)=\frac{d q}{d t}=k_s\left(q_e-q\right)
$$

Here $k_s$ is a constant that models the kinetics of the adsorption, $q(t)$ is the molar concentration of $\mathrm{CO}_2$ per unit adsorbent surface, and $q_e$ is the equilibrium concentration at the given temperature and pressure conditions.

Solving the adsorption problem consists of computing the concentration $C_A(x, r)$ over time. The breakthrough curve is obtained by integrating $C_A$ over the honeycomb exit and plotting the result over time.

[^1]: https://phys.libretexts.org/Bookshelves/Thermodynamics_and_Statistical_Mechanics/Heat_and_Thermodynamics_(Tatum)/07%3A_The_First_and_Second_Laws_of_Thermodynamics/7.01%3A_The_First_Law_of_Thermodynamics_and_Internal_Energy
[^2]: [[Physical and Computational Aspects of Convective Heat Transfer]]
[^3]: [[Fundamentals of heat and mass transfer]] Pg. 976