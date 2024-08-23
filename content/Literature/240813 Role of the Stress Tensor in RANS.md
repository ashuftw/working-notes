---
title: Role of the Stress Tensor in RANS
draft: false
tags:
---
By definition, [[240813 Reynolds Averaged Navier Stokes (RANS)|RANS]] modelling averages or filters the temporal fluctuations in the flow. Thereby also filtering turbulent behaviour of the fluid. 

Hence the average effect of the Turbulent behaviour is contributed to integral motion of the fluid through the [[240813 Reynolds Stress Tensor and Turbulent Shear Stress|Reynolds Stress Tensor]] in the momentum equation. It is represented as $\tau^{turb}_{ij}$.

The RANS Momentum Equation is given by
$$\boxed{
\frac{\partial \bar{u}_i}{\partial t}+\frac{\partial \bar{u}_i \bar{u}_j}{\partial x_j}=-\frac{1}{\rho} \frac{\partial \bar{p}}{\partial x_i}+\frac{\partial}{\partial x_j}\left[v \frac{\partial\bar u_i}{\partial x_j}+\tau_{i j}^{t u r b}\right]}
$$
where $\tau_{i j}^{t u r b} = -\overline{u_i' u_j'}$  represents the [[240813 Reynolds Stress Tensor and Turbulent Shear Stress|Reynolds Stresses]]






