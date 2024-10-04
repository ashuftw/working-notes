---
title: Governing Equations
draft: true
date: 2024-10-01
---

### First Law of Thermodynamics[^1]
$$ \dot E = \dot{W} + \dot{Q} $$

Where,
- $\dot E\rightarrow$  rate of change of Internal Energy
- $\dot{W}\rightarrow$ rate of work done by external forces
- $\dot{Q}\rightarrow$  rate of heat addition

Using this, one can derive the Conservation of Species. Details. [^2]
### Conservation of Species in a 2D Binary Mixture
Derivation[^3]
$$
\frac{\partial C_A}{\partial t}+u \frac{\partial C_A}{\partial x}+v \frac{\partial C_A}{\partial y}=D_{A B}\left(\frac{\partial^2 C_A}{\partial x^2}+\frac{\partial^2 C_A}{\partial y^2}\right)\tag{1}
$$
where,
- $C_A(x, y, t)\rightarrow$molar concentration of $\mathrm{CO}_2$
- $C_B(x, y, t)\rightarrow$molar concentration of air
- $u(x, y, t),\, v(x, y, t)\rightarrow$velocities in $x$ and $y$
- $D_{A B}$ is the mass diffusivity of the A-B mixture or the Binary Diffusion Coefficient. 

**Note:**
- LHS -> Net Transport of Species $A$ due to advection (bulk fluid motion).
- RHS -> Inflow due to diffusion and production due to chemical reaction (Edit: check the presence of $\dot N$ as shown in [[Fundamentals of heat and mass transfer|Incorpera]])

### Transformation into Cylindrical Coordinates

Assuming fully developed laminar flow within each cell. (Eq. 1) becomes
$$
\frac{\partial C_A}{\partial t}+u_d \frac{\partial C_A}{\partial x}=D_{A B} \frac{1}{r} \frac{\partial}{\partial r}\left(r \frac{\partial C_A}{\partial r}\right)\tag2
$$

where, 
- $u_d=u_m\left(1-\left(\frac{r}{R}\right)^2\right)$ parabolic velocity profile in each cell of diameter $R$ 
- $u_m\rightarrow$ maximum velocity
- $r\rightarrow$ radial coordinate

### Thin Duct Equation
Note that in steady state, (Eq. 2) reduces to the thin duct equation. 
$$
u_d \frac{\partial C_A}{\partial x}=D_{A B} \frac{1}{r} \frac{\partial}{\partial r}\left(r \frac{\partial C_A}{\partial r}\right) .\tag3
$$
More on (Eqn. 3)[^4]
### Boundary Condition
The DAC problem consists in solving (Eq. 2) with the boundary condition
$$
-D_{A B}\left(\frac{\partial C_A}{\partial r}\right)_{r=R}=\dot{q}(t)\tag4
$$
where,
- $\dot{q}(t)\rightarrow$ Molar flux of $\mathrm{CO}_2$ through the adsorbent surface. 
- $\left(\frac{\partial C_A}{\partial r}\right)_{r=R}\rightarrow$ Concentration Gradient of $C_A$ at the surface.
### Adsorption Model
We assume adsorption kinetics such that
$$
\dot{q}(t)=\frac{d q}{d t}=k_s\left(q_e-q\right) \tag 5
$$

where,
- $k_s\rightarrow$ model constant
- $q(t) \rightarrow$ instantaneous molar concentration of $\mathrm{CO}_2$ per unit adsorbent surface.
- $q_e\rightarrow$ equilibrium concentration at the given temperature and pressure conditions.

**Note:**  $(q_e - q)$ represents the difference between the equilibrium concentration and the current concentration, which drives the adsorption process.

## Solution Method
- Solving the adsorption problem consists of computing the concentration $C_A(x, r)$ over time. 
- The breakthrough curve is obtained by integrating $C_A$ over the honeycomb exit and plotting the result over time.

[^1]: [LibreTexts Physics: The First Law of Thermodynamics and Internal Energy](https://phys.libretexts.org/Bookshelves/Thermodynamics_and_Statistical_Mechanics/Heat_and_Thermodynamics_(Tatum)/07%3A_The_First_and_Second_Laws_of_Thermodynamics/7.01%3A_The_First_Law_of_Thermodynamics_and_Internal_Energy)
[^2]: [[Physical and Computational Aspects of Convective Heat Transfer]]
[^3]: [[Fundamentals of heat and mass transfer]] Pg. 976
[^4]: [[Physical and Computational Aspects of Convective Heat Transfer]] Chpt. 5, Pg. 125
