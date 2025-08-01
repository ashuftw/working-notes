---
title: Numerical Methods
draft: true
tags: 
date: 2025-07-31
---
## Task 1 (Lagrange interpolation)
- **$x=(x_0, x_1, x_2)$ and $y(x)$** 
- **Sketch each Basis Polynomial** 
## Task 2 (Numerical Integration)
1. **Compute using $\frac 3 8^{\text{th}}$ rule (Formula Given) and midpoint rule $$ I(f)=\int_0^1 18x^2-1\, dx$$ **
2. **What is degree of Accuracy?**
3. **Compute degree of Accuracy for the $\frac 3 8^{\text{th}}$ rule and assume it can integrate Constant and linear Polynomials exactly.** 
## Task 3 (Numerical Differentiation and Extrapolation)
$$
f(x) = x^3
$$
1. **Calculate $f'(1)$ using Backward difference coefficient which $h_1 =\frac 1 2$, $h_2=\frac 1 4$. Compare with exact value.** 
2. **Carry $1$ step extrapolation scheme using the results from above and compute the resulting scheme.** 
3. **Find convergence order of resulting scheme.** 
## Task 4 (Banach's Fixed Point Theorem)
$$
f(x) =x^2 -x -1 \quad \& \quad g =  1 + \frac 1 x
$$
1. **Derive $g$**
2. **Check Banach's Fixed Point Theorem for $g$ on Domain $D = [1.5,2]$**
3. **Perform iterations (values are given)**
## Task 5 (One Step Method)
1. **Derive improved Euler Method for ODE $y' = f(t, y(t)$) with $y(0) = 0$. Start with the Fundamental Theorem of calculus. Clearly indicate when the calculated values are exact and when they are approximations. Assume equal step** 
2.  **Use Improved Euler to approximate $$y' = 4y+1, \quad y(0)= 0$$**
	**Consider $h = \frac 1 2$. Use improved Euler to approximate $y$ at $t=1$**
## Task 6 (Truncation error, consistency, convergence)
1. **Formally define Error, Consistency, Convergence in a few sentence.** 
2. **What's the connection between Consistency, Convergence and Stability.** 
## Task 7 ( Butcher Tableau, Runge-Kutta Methods)
1. **Translate the method into butcher table and provide the derivation in clear terms. $$\text{long method}$$**
2. **Translate Butcher table to RK Method**
3. **Explain if the Butcher table is consistent or not and if it is either explicit or implicit.** 
## Task 8 (Finite Difference)
$$
\begin{aligned}
u_t &= u_{xx}, && t>0, \quad x \in (0, x_{\text{max}}) \\
u(t,0) &= g_1, && t>0 \\
u(0,x) &= u_0(x), && x \in (0, x_{\text{max}})
\end{aligned}
$$
**Write the ODE System in Matrix Vector form. State dimensions and clearly indicate which values are exact and which are approximations.** 
