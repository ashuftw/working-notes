---
title: Function Library
draft: true
tags: 
date: 2025-05-22
---
### NumPy Quick Reference:

```python
# Array Creation
np.array([1,2,3])
np.zeros((3,3))
np.ones((2,4))  
np.linspace(0, 10, 100)  # 100 points from 0 to 10
np.arange(0, 10, 0.1)    # step size 0.1
np.random.randn(100)     # random normal distribution

# Matrix Operations  
A.T or np.transpose(A)
np.dot(A, B) or A @ B
np.linalg.det(A)
np.linalg.inv(A)
np.linalg.solve(A, b)
```

### Matplotlib Gallery:

```python
# Multiple subplot configurations
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))
ax1.plot(x, y1); ax2.plot(x, y2)

# Log plots
plt.semilogx(x, y)    # log x-axis
plt.semilogy(x, y)    # log y-axis  
plt.loglog(x, y)      # both log

# Formatting
plt.plot(x, y, 'r--', linewidth=2, markersize=8, label='Data')
colors: 'r', 'g', 'b', 'k', 'c', 'm', 'y'
styles: '-', '--', '-.', ':'
markers: 'o', 's', '^', 'x', '+'
```
