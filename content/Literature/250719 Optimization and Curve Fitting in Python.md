---
title: Optimization and Curve Fitting in Python
draft: true
tags: 
date: 2025-07-19
---
## Find Zero using [[230629 Newton-Raphson or Newton's Method|Newton's Method]]
```python
from scipy.optimize import newton
 
x_solution = newton(equation_function, initial_guess_x0, args=(parameters,))
```
