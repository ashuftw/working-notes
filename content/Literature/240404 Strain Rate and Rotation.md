---
title: Strain Rate and Rotation
draft: false
tags:
---
## Strain rate
It is the rate at which deformation occurs in all directions. It takes into changes in volume and shape. 
**Strain rate tensor**

$$
S_{i j}=\frac{1}{2}\left(\frac{\partial u_i}{\partial x_j}+\frac{\partial u_j}{\partial x_i}\right)
$$

> For $i,j=1,2,3$ (Dimensions)
## Rotation
It is the rate at which a fluid particle rotates about it's own axis. The rotation of at a point is given by the Vorticity ($\vec{\omega}=\nabla \times \vec{u}$) of the flow (which defines the Rotation for a whole field)
**Rotational Tensor**

$$
\Omega_{i j}=\frac{1}{2}\left(\frac{\partial u_i}{\partial x_j}-\frac{\partial u_j}{\partial x_i}\right)
$$

## Derivation
Both Strain rate and rotation can be unpacked from the gradient of velocity.

$$
\begin{align*}
\frac{\partial u_i}{\partial x_j}=&  \overbrace{\frac{1}{2} \frac{\partial u_i}{\partial x_j}+\frac{1}{2} \frac{\partial u_j}{\partial u_i}}^{\text{Symmetric part}}+\overbrace{\frac{1}{2} \frac{\partial u_i}{\partial u_j}-\frac{1}{2} \frac{\partial u_j}{\partial u_i}}^{\text{Asymmetric part}}\\ \\
=& S_{ij}+\Omega_{ij}
\end{align*}
$$



