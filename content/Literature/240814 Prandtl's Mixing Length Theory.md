---
title: Prandtl's Mixing Length Theory
draft: false
tags:
---
It proposes a way to express Turbulent Viscosity through dimensional analysis in order to solve the [[240813 The Closure Problem of RANS|the Closure problem]] in [[240813 Reynolds Averaged Navier Stokes (RANS)|RANS]]

The Kinematic Turbulent Viscosity ($v_t$) in the [[240813 Eddy Viscosity or Boussinesq Hypothesis|Boussinesq Assumption]]
$$
v_t \propto \mathrm{m}^2 / \mathrm{s}
$$
Through [[230223 Buckingham's Pi Theorem|dimensional analysis]] 
$$
v_t \propto U_{\text {turb }} l_m
$$
Where,
- $U_{\text {turb }}\rightarrow$ Characteristic Velocity
- $l_m\rightarrow$ Mixing Length

Similarly fluctuating velocity can be written in terms of Mean Strain
$$
u^{\prime} \sim l_m \frac{\partial \bar{u}}{\partial y}
$$

Plugging into the [[240813 Reynolds Stress Tensor|Reynolds Stress Tensor]] 
$$
-\overline{u^{\prime}_i u^{\prime}_j}  =l_m^2\left|\frac{\partial \bar{u}_j}{\partial y}\right| \frac{\partial \bar{u}_i}{\partial y}
$$

> Note: $j$ here is the vertical component and it cannot be negative 

Using the [[240813 Eddy Viscosity or Boussinesq Hypothesis|Boussinesq Hypothesis]]
$$
v_t\left(\frac{\partial \bar{u}_i}{\partial x_j}\right)  =l_m^2\left|\frac{\partial \bar{u}_j}{\partial y}\right| \frac{\partial \bar{u}_i}{\partial y}
$$
$$\boxed{
v_t  =l_m^2\left|\frac{\partial \bar{u}}{\partial y}\right|
}
$$
Thus we have an equation to calculate [[240404 Eddy Viscosity|Eddy Viscosity]]

> Note: The Mixing length ($l^2_m$) is selected base on the kind of flow.  
