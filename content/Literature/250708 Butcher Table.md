---
title: Butcher Table
draft: false
tags: 
date: 2025-07-09
---
**Butcher tableau** is essentially a compact recipe card that defines a specific [[250709 Runge-Kutta Method Procedure|Runge-Kutta]] method for solving ordinary differential equations. It neatly organizes all the coefficients you need for the calculation into a single table.
## Definition
A **Butcher Table** represents a Runge-Kutta method for solving ordinary differential equations $y' = f(t,y)$. It encodes how to compute intermediate stages and combine them to advance the solution.

**General Form**
$$
\begin{array}{c|c}
\mathbf{c} & A \\
\hline
& \mathbf{b}^T
\end{array}
=
\begin{array}{c|cccc}
c_1 & a_{11} & a_{12} & \cdots & a_{1s} \\
c_2 & a_{21} & a_{22} & \cdots & a_{2s} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
c_s & a_{s1} & a_{s2} & \cdots & a_{ss} \\
\hline
& b_1 & b_2 & \cdots & b_s
\end{array}
$$

- $C$-> time increments for intermediate stages
- $a$ -> coefficients for combining previous $k$ values in each stage
- $b$ -> final weights for combining all $k$ values to get $y_{i+1}$
- $k$ -> intermediate slope evaluations
