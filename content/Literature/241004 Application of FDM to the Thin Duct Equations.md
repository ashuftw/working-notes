---
title: Finite Difference of Thin Duct Equation
draft: true
tags: 
date: 2024-10-04
---

### [[241001 Governing Equations|Steady State Thin Duct equation]]

$$u_d \frac{\partial C_A}{\partial x} = D_{AB} \frac{1}{r} \frac{\partial}{\partial r}\left(r \frac{\partial C_A}{\partial r}\right)$$
### Forward difference approximation of LHS

$$\frac{\partial C_A}{\partial x} \approx \frac{C_A[i+1,j] - C_A[i,j]}{\Delta x}$$
### Central difference approximation of RHS 
Using central differences at $r_{j+1/2}$ and $r_{j-1/2}$
$$\left(\frac{\partial C_A}{\partial r}\right)_{j+1/2} \approx \frac{C_A[i,j+1] - C_A[i,j]}{\Delta r}$$ $$\left(\frac{\partial C_A}{\partial r}\right)_{j-1/2} \approx \frac{C_A[i,j] - C_A[i,j-1]}{\Delta r}$$
Now, we can approximate $\frac{\partial}{\partial r}\left(r \frac{\partial C_A}{\partial r}\right)$

$$
\frac{\partial}{\partial r}\left(r \frac{\partial C_A}{\partial r}\right) \approx \frac{r_{j+1/2} \left(\dfrac{C_A[i,j+1] - C_A[i,j]}{\Delta r} \right)- r_{j-1/2} \left( \dfrac{C_A[i,j] - C_A[i,j-1]}{\Delta r}\right)}{\Delta r}
$$


Where $r_{j+1/2} = \frac{r_j + r_{j+1}}{2}$ and $r_{j-1/2} = \frac{r_j + r_{j-1}}{2}$.

## Step 3: Combine the Discretized Terms

Substituting the discretized right-hand side into our equation:

$$u_d \frac{C_A[i+1,j] - C_A[i,j]}{\Delta x} = D_{AB} \frac{1}{r_j} \frac{r_{j+1/2} \frac{C_A[i,j+1] - C_A[i,j]}{\Delta r} - r_{j-1/2} \frac{C_A[i,j] - C_A[i,j-1]}{\Delta r}}{\Delta r}$$

## Step 4: Solve for C_A[i+1,j]

Multiply both sides by $\Delta x$:

$$u_d (C_A[i+1,j] - C_A[i,j]) = \frac{D_{AB} \Delta x}{r_j \Delta r^2} (r_{j+1/2} (C_A[i,j+1] - C_A[i,j]) - r_{j-1/2} (C_A[i,j] - C_A[i,j-1]))$$

Now, solve for $C_A[i+1,j]$:

$$C_A[i+1,j] = C_A[i,j] + \frac{D_{AB} \Delta x}{u_d r_j \Delta r^2} (r_{j+1/2} (C_A[i,j+1] - C_A[i,j]) - r_{j-1/2} (C_A[i,j] - C_A[i,j-1]))$$