---
title: Finite Difference of Thin Duct Equation
draft: true
tags: 
date: 2024-10-04
---

## To analyse the DAC [[241001 Governing Equations| Equations]], we solve the following boundary value problem.

### Thin Duct Equation


$$
u_d \frac{\partial C_A}{\partial x} = D_{AB} \frac{1}{r} \frac{\partial}{\partial r}\left(r \frac{\partial C_A}{\partial r}\right)\tag{1}
$$


### Boundary Condition


$$
-D_{A B}\left(\frac{\partial C_A}{\partial r}\right)_{r=R}=\dot{q}(t)
$$


### Adsorption Model


$$
\dot{q}(t)=\frac{d q}{d t}=k_s\left(q_e-q\right)
$$


## Discretization

### 1. Convection Term 

Using Forward difference approximation


$$
\frac{\partial C_A}{\partial x} \approx \frac{C_A[i+1,j] - C_A[i,j]}{\Delta x}
$$


Using Central difference


$$
\left(\frac{\partial C_A}{\partial x}\right)_i \approx \frac{C_{A,i+1} - C_{A,i-1}}{2\Delta x}
$$


Where, 
- $j\rightarrow$ radial domain
- $i\rightarrow$ axial domain

### 2. Diffusion Term


$$
D_{AB} \cdot \frac{1}{r} \cdot \frac{\partial}{\partial r}\left(r \cdot \frac{\partial C_A}{\partial r}\right)
$$


Chain rule


$$
D_{AB} \cdot \left[\frac{1}{r} \cdot \frac{\partial C_A}{\partial r} + \frac{\partial^2 C_A}{\partial r^2}\right]
$$


**Central Difference**


$$
\left(\frac{\partial C_A}{\partial r}\right)_j \approx \frac{C_{A,j+1} - C_{A,j-1}}{2\Delta r}
$$



$$
\left(\frac{\partial^2 C_A}{\partial r^2}\right)_j \approx  \frac{C_{A,j+1} - 2C_{A,j} + C_{A,j-1}}{\Delta r^2}
$$


Substituting,


$$
D_{AB} \cdot \left[\frac{1}{r_j} \cdot \frac{C_{A,j+1} - C_{A,j-1}}{2\Delta r} + \frac{C_{A,j+1} - 2C_{A,j} + C_{A,j-1}}{\Delta r^2}\right]
$$


> **Note:** Full derivation of Central difference approximations for First and Second Order Diff. Equations can be found here. [^1]

- **Applying the Forward Euler Method to the Adsorption Model**


$$
\quad \frac{dq}{dt}= \frac{q_{n+1} - q_{n}}{dt} =k_s\left(q_e-q_n\right)
$$



$$
\boxed{\quad  q_{n+1}  =  q_n +\Delta t\cdot k_s\left(q_e-q_n\right)}
$$


[[241007 Without the Boundary condition?]]

[^1]: https://www.dam.brown.edu/people/alcyew/handouts/numdiff.pdf