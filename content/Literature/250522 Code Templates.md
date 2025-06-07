---
title: Code Templates
draft: true
tags: 
date: 2025-05-22
---

### Template: Basic OOP Class

```python
class ClassName:
    def __init__(self, param1, param2=default_value):
        self._protected_attr = param1  # protected attribute
        self._another_attr = param2
    
    @property
    def protected_attr(self):
        return self._protected_attr
    
    @protected_attr.setter  
    def protected_attr(self, value):
        self._protected_attr = value
    
    def __repr__(self):
        return f"ClassName(attr={self._protected_attr})"
    
    def __add__(self, other):
        # Define addition behavior
        return ClassName(self._protected_attr + other._protected_attr)
```

### Template: ODE System

```python
def ode_system(t, y, *args):
    # y = [y1, y2, y3, ...]  # state variables
    # Unpack parameters
    param1, param2 = args
    
    # Define derivatives
    dy1dt = y[1]  # y1' = y2
    dy2dt = -param1*y[0] - param2*y[1]  # y2' = -k*y1 - c*y2
    
    return [dy1dt, dy2dt]

# Solve
sol = solve_ivp(ode_system, (0, 10), [initial_cond1, initial_cond2], 
                args=(param1, param2), method='RK45')
```

### Template: Curve Fitting Function

```python
def fit_function(x, a, b, c):
    return a * np.exp(b * x) + c

# Usage
popt, pcov = curve_fit(fit_function, x_data, y_data, p0=[1, 0.1, 0])
x_fit = np.linspace(x_data.min(), x_data.max(), 100)
y_fit = fit_function(x_fit, *popt)

# Error calculation
residuals = y_data - fit_function(x_data, *popt)
ss_res = np.sum(residuals ** 2)
error_percent = (ss_res / (len(y_data) * np.max(y_data))) * 100
```
