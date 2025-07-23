---
title: SS24 Numerical Methods
draft: true
tags: 
date: 2025-07-22
---
### a) $f(x) = \sin(\pi x)$
- $x_0 = 0$
- $x_1 = \frac{1}{2}$
- $x_2 = 1$
Find interpolation polynomial $p(x)$ with Vandermonde matrix and sketch the polynomial.
### b) Calculate error for interval $[0,1]$

## Q2

### a)

Calculate the accuracy of trapezoidal rule.

### b)

Derive the quadrature formula for Simpson's rule: $$\int f(x)dx$$

## Q3

### a)

Give approximation for first order for central difference quotient $\underline{x}$. Find its convergence order. Find exact answer by taking $x = 1$ and $h = 1$. State difference between actual and approximation.

### b)

Perform Romberg extrapolation for central difference quotient to approximate the first-order derivative of function. What is the convergence order of this?

## Q4

### a)

$f(x) = x + \sin(x)(m+y+x)$, $g(x) = \cos(x)$

Check if all conditions of Banach are met.

### b)

$x_0 = 0$. Perform two steps for Banach and Newton Method and show which converges (give it closer to value).

## Q5

### a)

Show if improved Euler method is consistent for $h \to 0$

### b)

[blank]

### c)

[blank]

## Q6

### a)

Derive the explicit and implicit Euler Methods starting with fundamental theorem of calculus. State the exact and approximates used.

### b)

Explain difference between explicit and implicit in terms of stability and computation.

### c)

Explain in one sentence relation for stability, convergence, consistency.

## Q7

### a)

Form a Butcher table from given equations

### b)

Form equation in form $y_{n+1}$ from the given Butcher table.

### c)

State 2 properties from (b) which can be seen from the Butcher table.

## Q8

### a)

[Something about]

### b)

[chat die]

## Q9 - Bonus (3 Marks)

Explain the advantage of controlling the step size and give an idea how step size can be controlled. $(g_4 = step size control)$

---

# Additional Notes

Week: W.S. 24/25 - Num

1. Polynomial Interpolation: She gave a function and need to find Interpolation polynomial error and plot
2. Journal Kepler Rule: She gave upper and lower limits and gave $N_1$. So we take, we need step size (calculate step first?)
3. Need to derive the Numerical differentiation Romberg extrapolation. To make it accurate.
4. Newton Polynomial: With 3 conditions - Mapping, Contraction etc. She gave 2 $g(x)$ and asked which $g(x)$ would I use for $f(x)$ (Banach $g$?)
5. Crank Nicolson problem with normal function
6. Accuracy, Stability, Convergence - Derivation of transition error of...
7. 2D PDE [Method of Lines]
8. Butcher Tableau