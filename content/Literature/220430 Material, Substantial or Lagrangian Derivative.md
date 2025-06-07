---
title: Material, Substantial or Lagrangian Derivative
draft: false
date: 2022-04-30
---

## Ashu's Shorthand definition
A material Derivative expresses the rate of change of a function of both time and space. 

The substantial derivative $\frac{D}{Dt}$ of a quantity $\phi$ is the rate of change of  $\phi$ belonging to a certain particle moving within a material or substance.  

## Proof 

Temperature of a moving particle $p$.

$$
T_p = T_p [x_p(t), y_p(t), y_p(t), z_p(t), t]
$$


Applying multi-variable chain rule 
$$
\frac{d T_p}{d t} = \frac{\partial T_p}{\partial t}+\frac{\partial T_p}{\partial x_p}\frac{dx_p}{dt}+\frac{\partial T_p}{\partial y_p}\frac{dy_p}{dt}+\frac{\partial T_p}{\partial z_p} \frac{dz_p}{dt}
$$

After simplification

$$
\frac{d T_p}{d t} = \frac{\partial T_p}{\partial t}+u\frac{\partial T_p}{\partial x_p}+v\frac{\partial T_p}{\partial y_p}+w\frac{\partial T_p}{\partial z_p}=\frac{DT_p}{Dt}
$$

Using vector calculus notation 
$$
\boxed{\frac{DT}{Dt}=\frac{\partial T}{\partial t}+\underbrace{(\vec{U}\cdot \nabla T)}_{\text{convective der}}}
$$


Note: The fluid particle in this context refers to the Fluid parcel in continuum mechanics. 



---
# References
[Faculty of Khan - The Material Derivative | Fluid Mechanics](https://www.youtube.com/watch?v=xlxK0VuY9yY)