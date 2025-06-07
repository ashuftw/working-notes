---
title: Troubleshooting
draft: true
tags: 
date: 2025-05-22
---
### Common Errors & Fixes:
```python
# Dimension mismatch
x.shape, y.shape  # check dimensions first
x = x.flatten() if len(x.shape) > 1 else x

# Singular matrix error
try:
    result = np.linalg.solve(A, b)
except np.linalg.LinAlgError:
    result = np.linalg.lstsq(A, b, rcond=None)[0]

# ODE convergence issues  
sol = solve_ivp(func, t_span, y0, method='Radau', rtol=1e-8)

# Plot not showing
plt.show()  # don't forget this!
```

### Debugging Checklist:

- Check array dimensions with `.shape`
- Verify data types with `.dtype`
- Use `print()` statements for intermediate values
- Check for NaN/inf values with `np.isnan()`, `np.isinf()`
