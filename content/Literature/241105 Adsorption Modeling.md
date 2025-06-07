---
title: Adsorption Modeling
draft: true
tags: 
date: 2024-11-05
---
### Boundary condition
$$
-D_{AB}\left(\frac{\partial C_A}{\partial y}\right)_{y=W} = \dot{q}(t)
$$
# Forward Difference
$$
-D_{AB}\frac{C_0 - C_1}{\Delta y} = \text{flux}
$$
$$
C_0 = C_1- \Delta y \cdot \frac {\text{flux}}{D_{AB}} 
$$
Note: 
- $j=0\rightarrow$ Ghost layer 
- $j=1\rightarrow$ Physical wall
![[../Files/Pasted image 20241106133251.png|center|400]]
The wall lies in between the Ghost layer and the Inner layer. Therefore $\Delta y$ is divided by $2$
$$
\boxed{
C_0 = C_1- \frac {\Delta y} 2 \cdot \frac {\text{flux}}{D_{AB}} 
}
$$
# 3-Point Stencil
### Taylor series expansion for points near wall $(j=0)$:
$$
C_A(j+1) = C_A(j) + \Delta y\left(\frac{\partial C_A}{\partial y}\right) + \frac{(\Delta y)^2}{2}\left(\frac{\partial^2 C_A}{\partial y^2}\right) + O(\Delta y^3)
$$

$$
C_A(j+2) = C_A(j) + 2\Delta y\left(\frac{\partial C_A}{\partial y}\right) + 2(\Delta y)^2\left(\frac{\partial^2 C_A}{\partial y^2}\right) + O(\Delta y^3)
$$

Using Subscript notation
$$
C_1 = C_0 + \Delta y\left(\frac{\partial C_A}{\partial y}\right)_0 + \frac{(\Delta y)^2}{2}\left(\frac{\partial^2 C_A}{\partial y^2}\right)_0
$$
$$
C_2 = C_0 + 2\Delta y\left(\frac{\partial C_A}{\partial y}\right)_0 + 2(\Delta y)^2\left(\frac{\partial^2 C_A}{\partial y^2}\right)_0
$$

### Eliminate higher order terms
**Multiply first equation by 4 and subtract second equation**
$$\begin{align}
4C_1 - C_2 = 4\left[C_0 + \Delta y\left(\frac{\partial C_A}{\partial y}\right)_0 + \frac{(\Delta y)^2}{2}\left(\frac{\partial^2 C_A}{\partial y^2}\right)_0\right] \\
- \left[C_0 + 2\Delta y\left(\frac{\partial C_A}{\partial y}\right)_0 + 2(\Delta y)^2\left(\frac{\partial^2 C_A}{\partial y^2}\right)_0\right]
\end{align}
$$
**Simplify**
$$
4C_1 - C_2 = 3C_0 + 2\Delta y\left(\frac{\partial C_A}{\partial y}\right)_0
$$
**From boundary condition**
$$
\left(\frac{\partial C_A}{\partial y}\right)_0 = -\frac{\dot{q}}{D_{AB}} = -\frac{\text{flux}}{D_{AB}}
$$
**Substituting**
$$
4C_1 - C_2 = 3C_0 - 2\Delta y\frac{\text{flux}}{D_{AB}}
$$

**Rearranging**
$$
C_0 = \frac{4C_1 - C_2 + 2\Delta y\frac{\text{flux}}{D_{AB}}}{3}
$$



