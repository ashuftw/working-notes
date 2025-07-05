---
title: Code Templates
draft: true
tags: 
date: 2025-05-22
---
## Cheatsheet 

### 1. **File Reading Template**

```python
import numpy as np
# NumPy method
data = np.loadtxt('filename.csv', delimiter=',',skiprows=1)
# load data 
x, y = data[:,0], data[:,1]
```

### 2. **Basic Plotting Template**
**Single Plot**
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, y, '-', label='Label1') 
ax.plot(v, w, '-', label='Label2') # if plotting 2 datasets 
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label') 
ax.legend() #ax.legend(loc='upper left')
plt.tight_layout()
plt.show()
plt.savefig('name.png')

```
**Multiple Subplots**
```python
# 2 rows, 1 collumn
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(8,6)) 
# 1 rows, 2 collumn
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10,4))

```
**Finding Peaks**
```python
peak_idx = np.argmax(y_data)  # or np.argmin() for valleys
peak_value = data[max_idx]
```
**Markers**
```python
# Add markers (crosses)
ax.plot(x_pos, y_pos, 'rx', markersize=10, markeredgewidth=2) 
```

**Plot-Annotations**
```python
ax.text(x_pos+5, y_pos+0.1, f'Tm = {temp:.1f}°C', 
        bbox=dict(boxstyle="round,pad=0.3", facecolor="white", edgecolor="red"))
```
**Line styles** 
```python
'-'    # solid line
'--'   # dashed line  
'-.'   # dash-dot line
':'    # dotted line
'k-'   # black solid
'r--'  # red dashed
```
### **3. Integration and Baseline** 
```python
# A) Peak-based integration (DSC, force curves, etc.)
peak_idx = np.argmax(y_data)  # or np.argmin() for valleys
window = 20  # adjust based on peak width
start_idx = peak_idx - window
end_idx = peak_idx + window

# B) Range-based integration (find indices for specific x-values)
start_idx = np.argmin(np.abs(x_data - start_value))  # closest to start_value
end_idx = np.argmin(np.abs(x_data - end_value))      # closest to end_value

# Extract region of interest
x_region = x_data[start_idx:end_idx]
y_region = y_data[start_idx:end_idx]

# Create baseline (linear between endpoints)
baseline = np.linspace(y_region[0], y_region[-1], len(y_region))
# Alternative: baseline = np.full(len(y_region), min(y_region))  # horizontal

# Baseline-corrected data
corrected_y = y_region - baseline

# Numerical integration
area = np.trapz(corrected_y, x_region)  # trapezoidal rule

# Visualize integration area
ax.fill_between(x_region, y_region, baseline, 
                color='lightblue', alpha=0.5, label='Integration area')

print(f"Integrated area: {area:.2f}")
```
### 3. **Curve Fitting Template**

```python
from scipy.optimize import curve_fit
def model(x, a, b):
    return a * x + b
params, _ = curve_fit(model, xdata, ydata, p0=[1, 1])
```

### 4. **ODE Solving Template**

```python
from scipy.integrate import solve_ivp
def system(t, y, params):
    # y = [y1, y2, ...]
    dydt = [eq1, eq2, ...]
    return dydt
sol = solve_ivp(system, [t0, tf], y0, args=(params,), 
                method='RK45', dense_output=True)
```

### 5. **Basic OOP Template**

```python
class MyClass:
    def __init__(self, param):
        self._protected = param
    
    @property
    def protected(self):
        return self._protected
    
    @protected.setter
    def protected(self, value):
        self._protected = value
```

