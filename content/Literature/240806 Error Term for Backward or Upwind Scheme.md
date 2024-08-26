---
title: Error Term for Backward or Upwind Scheme
draft: false
tags:
---
**1D Convection Equation**

$$
\frac {\partial u} {\partial t} + c \frac {\partial u} {\partial x }=0
$$

**Discretizing**

$$
\frac{\partial u}{\partial t}+c \frac{u_i-u_{i-1}}{\Delta x}=0
$$

Using [[231115  The Taylor Expansion|Taylor Expansion]] we have the error term can be found out (truncation error)


$$
u_{i-1}=u_i-\Delta x \frac{\partial u}{\partial x}+\frac{\Delta x^2}{2!} \frac{\partial^2 u}{\partial x^2}-\ldots
$$

where  $\Delta_x= (u_{i-1}-u_i)$ 

$$
\frac{u_i-u_{i-1}}{\Delta x}=\frac{\partial u}{\partial x}-\frac{\Delta x}{2!} \frac{\partial^2 u}{\partial x^2}  +\ldots
$$

The **Discretized Convection Equation**

$$
\boxed{
\frac{\partial u}{\partial t}+c \frac{\partial u}{\partial x}=\underbrace{c \frac{\Delta x}{2!}\frac{\partial^2 u}{\partial x^2}}_\text{Diffusion Term}-c \frac{\Delta x^2}{3!} \frac{\partial^3 u}{\partial x^3}+\ldots}
$$

> In the Continuous form, the RHS is $0$


