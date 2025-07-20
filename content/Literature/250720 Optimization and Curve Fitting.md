---
title: Optimization and Curve Fitting
draft: false
tags: 
date: 2025-07-20
---

```python
from scipy.optimize import curve_fit
def model(x, a, b):
    return a * x + b

initial_guess = [a,b]
# popt contains the optimal values for a and b
# pcov is the covariance matrix
popt, pcov = curve_fit(func, xdata, ydata, p0=initial_guess)
# Extract the optimized parameters
a_optimized, b_optimized = p

```

## Find Zero using [[230629 Newton-Raphson or Newton's Method|Newton's Method]]
```python
from scipy.optimize import newton
 
x_solution = newton(equation_function, initial_guess_x0, args=(parameters,))
```
