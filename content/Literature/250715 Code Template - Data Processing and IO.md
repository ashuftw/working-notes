---
title: Code Template - Data Processing and IO
draft: true
tags: 
date: 2025-07-15
---
### CSV Reading

```python
import numpy as np
import pandas as pd

# Method 1: NumPy
data = np.genfromtxt('filename.csv', delimiter=',', skip_header=1)
x_data = data[:, 0]  # First column
y_data = data[:, 1]  # Second column

# Method 2: NumPy loadtxt
x, y = np.loadtxt('filename.csv', delimiter=',', unpack=True)

# Method 3: Pandas (if allowed)
df = pd.read_csv('filename.csv')
x = df['column1'].values
y = df['column2'].values
```

### Plotting Essentials

```python
import matplotlib.pyplot as plt

# Basic plot with ALL common requirements
plt.figure(figsize=(8, 6))
plt.plot(x, y, 'b-', label='Data', linewidth=2)
plt.plot(x_fit, y_fit, 'r--', label='Fit', linewidth=2)
plt.xlabel('X Label')
plt.ylabel('Y Label')
plt.title('Title')
plt.legend(loc='best')
plt.grid(True)
plt.xlim([0, 10])  # If specific limits needed

# Line styles: '-' solid, '--' dashed, '-.' dash-dot, ':' dotted
# Markers: 'o' circle, 's' square, '^' triangle, 'x' cross
# Colors: 'b' blue, 'r' red, 'g' green, 'k' black

# Subplots
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8, 10))
ax1.plot(t, x1, 'b-', label='Mass 1')
ax1.set_xlabel('Time [s]')
ax1.set_ylabel('Position [m]')
ax1.legend()
ax1.grid(True)

ax2.plot(t, x2, 'r-', label='Mass 2')
ax2.set_xlabel('Time [s]')
ax2.set_ylabel('Position [m]')
ax2.legend()
ax2.grid(True)

plt.tight_layout()
plt.show()

# Text annotation
plt.text(0.1, 0.9, f'a={a:.1f}\nb={b:.1f}', 
         transform=plt.gca().transAxes, 
         bbox=dict(boxstyle='round', facecolor='wheat'))
```

### Curve Fitting

```python
from scipy.optimize import curve_fit

# Polynomial fitting
coeffs = np.polyfit(x, y, deg=4)  # 4th order polynomial
y_poly = np.polyval(coeffs, x)

# Get residuals
residuals = np.polyfit(x, y, deg=4, full=True)[1]
error = residuals[0] / (len(x) * np.max(y)) * 100
print(f"The 4th order polynomial has an error of {error:.2f} %")

# Custom function fitting
def func(x, a, b):
    return x/a * np.tanh(x/b)
    # Other common: a * np.exp(b * x), a * x**b

popt, pcov = curve_fit(func, x_data, y_data, p0=[1, 2])
a_opt, b_opt = popt
y_fit = func(x_data, a_opt, b_opt)

# Save parameters
np.savetxt('params.txt', popt)
```