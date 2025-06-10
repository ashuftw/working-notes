---
title: Quick Reference Page
draft: true
tags: 
date: 2025-05-22
---

### Essential Imports Block:

```python
# Standard Scientific Stack
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp, odeint
from scipy.optimize import curve_fit, fsolve, newton
from scipy.signal import butter, filtfilt
import pandas as pd
from openpyxl import Workbook
import datetime
```

### One-Liner Cheat Sheet:

```python
# File I/O
data = np.genfromtxt('file.csv', delimiter=',', skip_header=1)
np.savetxt('output.txt', data, delimiter=',', header='x,y')

# Plotting Essentials
plt.figure(figsize=(12,8))
plt.subplot(2,1,1)  # rows, cols, index
plt.plot(x, y, 'b-o', label='Data')
plt.xlabel('X Label'); plt.ylabel('Y Label'); plt.title('Title')
plt.legend(); plt.grid(True); plt.tight_layout()

# Curve Fitting
popt, pcov = curve_fit(func, x_data, y_data, p0=[initial_guess])
poly_coeffs = np.polyfit(x, y, degree)
y_fit = np.polyval(poly_coeffs, x)

# ODE Solving
sol = solve_ivp(ode_func, (t_start, t_end), y0, method='RK45', max_step=0.01)

# Linear Algebra
x = np.linalg.solve(A, b)  # Ax = b
inv_A = np.linalg.inv(A)
det_A = np.linalg.det(A)
```
