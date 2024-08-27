May 2022
  

Tags: [[CFD]] [[220507 Transport Equation]] [[Conservation of Momentum]] [[220507 Navier-Stokes Equations]] 

# Momentum Transport equation
The momentum transport equation defines how the momentum is transported across the field. 
Essentially, it expresses the Newton's Second Law applied to a fluid. 
$$
\text{Force}\propto\text{Rate of change of momentum}
$$

For a fluid parcel of volume $V$, Newton's II law can be expressed as follows 
$$
F=\dfrac{D}{Dt}(m\mathbf U)
$$

The [[220430 Material Derivative or Substantial Derivative or Lagrangian Derivative]] is used here as the velocity is function of both time and space.
When applied to a fluid parcel, the force per unit volume $f$ is given by 
$$
\dfrac{D}{Dt}(\rho \mathbf U)=f
$$

Simplifying
$$
\dfrac{\partial(\rho \mathbf U)}{\partial t}+\mathbf U\cdot \nabla (\rho \mathbf U)=f
$$

It can be shown that
$$
\dfrac{\partial(\rho \mathbf U)}{\partial t}+ \nabla\cdot  (\rho \mathbf U\ \mathbf U)=f
$$

The net forces acting on the fluid parcel can be expressed as follows
$$
\boxed{\dfrac{\partial(\rho \mathbf U)}{\partial t}+ \nabla\cdot  (\rho \mathbf U\ \mathbf U)=\underbrace{-\nabla p }_{\text{Pressure}}+ \underbrace{\nabla\cdot \tau}_{\text{Shear Stress}}+\underbrace{\rho \ g}_{gravity}}
$$

- The pressure term is -ve as the velocity increases in the direction of decreasing pressure. 

---
# References
1. [[220814 CFD-Fundamentals#Momentum The Navier-Stokes Equations]]

