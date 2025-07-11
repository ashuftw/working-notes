---
title: Butcher Table
draft: false
tags: 
date: 2025-07-09
---
## Definition
A Butcher tableau represents a Runge-Kutta method for solving ordinary differential equations $y' = f(t,y)$. It encodes how to compute intermediate stages and combine them to advance the solution.

**General Form**

$$
\begin{array}{c|cc}
& C_1 & a_{11} & a_{21} \\
& C_2 & a_{21} & a_{21} \\
\hline
& & b_1 & b_2
\end{array}
$$


- $C$-> time increments for intermediate stages
- $a$ -> coefficients for combining previous $k$ values in each stage
- $b$ -> final weights for combining all $k$ values to get $y_{i+1}$