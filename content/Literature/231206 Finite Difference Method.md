---
title: Finite Difference Method
draft: false
tags:
---
## 1D Boundary value problem
**Differential equation**

$$
-a(x) u^{\prime \prime}(x)+b(x) u^{\prime}(x)+c(x) u(x)=f(x), \quad x \in(0,1)
$$

**Boundary conditions** 

$$
\begin{aligned}
& u(0)=g_D \quad \text { Dirichlet boundary condition } \\
& u^{\prime}(1)=g_N \quad \text { Neumann boundary condition } \\
&
\end{aligned}
$$

**Goal:** Apply Finite Differences to discretize the problem. 
### Step 1: Meshing 
$x\in [0,1]$ is divided with $n$ equidistant parts.   

![[Pasted image 20231206123754.png|#center|500]]

$$
x_j=j h, \quad j=0, \ldots, n, \quad h=\frac{1}{n}
$$

### Step 2: Discretization
The derivative can be calculated using three different ways
![[Pasted image 20231206124417.png|#center|600]]

The Differential equation then can be written
![[Pasted image 20231206124537.png|#center|600]]
## Step 4: Plotting

![[Pasted image 20231206124718.png|center|600]]