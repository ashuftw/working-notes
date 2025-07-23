---
title: Euler-Heun Method
draft: false
tags: 
date: 2025-07-09
---
## Definition
It is [[230417 Numerical Methods for Differential Equations|Numerical Method]] used to find the approximate solution of an [[221106 Ordinary Differential Equations|Ordinary Differential Equation]]
an explicit predictor-corrector method that combines Euler's method (**Predictor**) with the trapezoidal rule (**Corrector**) to achieve higher accuracy.

**Formula**

$$
y_{i+1} = y_i +  \underbrace{\frac{h}{2}[f(t_i, y_i) + f(t_{i+1}, \overbrace{y_i + hf(t_i, y_i)}^{\text{Euler}})]}_\text{Trapezoidal}
$$

### Derivation

**Starting point:** The exact solution satisfies 
$$
y(t_{i+1}) = y(t_i) + \int_{t_i}^{t_{i+1}} f(t, y(t)) , dt
$$


**Step 1: Apply trapezoid rule** to approximate the integral: 
$$
\int_{t_i}^{t_{i+1}} f(t, y(t)) , dt \approx \frac{h}{2}[f(t_i, y(t_i)) + f(t_{i+1}, y(t_{i+1}))]
$$


where $h = t_{i+1} - t_i$.

**Step 2: Replace exact values** with approximations:

- $y(t_i) \approx y_i$ (known)
- $y(t_{i+1}) \approx y_{i+1}$ (unknown)

This gives: 
$$
y_{i+1} = y_i + \frac{h}{2}[f(t_i, y_i) + f(t_{i+1}, y_{i+1})]
$$


**Step 3: Make explicit** by approximating $y_{i+1}$ on the right side using Euler's method: 
$$
\tilde{y}_{i+1} = y_i + hf(t_i, y_i)
$$


**Step 4: Final Euler-Heun formula:** 
$$
\boxed{y_{i+1} = y_i + \frac{h}{2}[f(t_i, y_i) + f(t_{i+1}, y_i + hf(t_i, y_i))]}
$$



### Properties of Euler-Heun:
- **Explicit** method (no implicit equation to solve)
- **One-step** method (uses only $y_i$ to compute $y_{i+1}$)
- **Consistency order 2** (local error $O(h^3)$, global error $O(h^2)$)
- **2 stages**: requires 2 evaluations of $f$ per step
- **Runge-Kutta method** of order 2
- **Stability region** larger than Euler's method
- Also called **improved Euler** or **modified Euler** method
