May 2022
   

Tags: 

# 1. Transport Equations
The Navier-Stokes equations relate the rate of change of moThe Navier-Stokes equations relate the rate of change of momentum of the fluid parcel to the net force applied to the fluid parcel. It is used to calculate the velocity field for the given problem.

### Momentum: The Navier-Stokes Equations

From Newton’s II law
$$
\begin{align*}\text{Force}\propto \text{Rate of change of Momentum}\end{align*}
$$

In Cartesian coordinate system ![[Pasted image 20220430154540.png|center]]
For Fluids, we solve the Navier-Stokes equations which are analogous to Newton's II law. 
For a fluid parcel of volume $V$, the Navier-Stokes equations can be written as![[Pasted image 20220430154704.png|center]]
Where $m\rightarrow$ mass of fluid parcel, $D/Dt\rightarrow$ [[220430 Material, Substantial or Lagrangian Derivative|material derivative]] 
Since $V$ is constant, it is standard practice to divide it. ![[Pasted image 20220430155219.png|center]]
$\rho\rightarrow$fluid density, $f\rightarrow$sum of external forces per unit volume, acting on a fluid parcel.

Expanding the material derivative![[Pasted image 20220430161130.png|center]]
Manipulating LHS![[Pasted image 20220430161245.png|center]]
Most common force that act to change the momentum of a fluid parcel are pressure, viscosity and gravity.![[Pasted image 20220430161355.png|center]]
Pressure gradient is -ve as the fluid particle accelerates in the direction of decreasing pressure. 

-   The Navier-Stokes equations are non-linear because of the $U U$ term.
-   RHS: Total forces acting on the fluid particles.
-   LHS: Acceleration of the fluid parcel caused by the forces.

### Temperature: Total Energy equation (Simplified)
The Total Energy equation helps to calculate the temperature field.![[Pasted image 20220430171834.png|center]]
Thermal energy is transported in the fluid by convection and diffusion (radiation is ignored).
Expanding the Diffusion term![[Pasted image 20220430171937.png|center]]
Expanding the Convection term![[Pasted image 20220430171951.png|center]]
- Most transport equations have the same form having a Time derivative, Convection term, Diffusion Term and finally the Source Term.
- Properties like turbulence are usually introduced as a source term.
- It isn’t uncommon to have 5-6 source terms.




