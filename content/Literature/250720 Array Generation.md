---
title: Array Generation
draft: false
tags: 
date: 2025-07-20
---
```python
# Linear spacing between start and stop
np.linspace(start, stop, num_points)
# With endpoint control
np.linspace(0, 10, 100, endpoint=False)  # Excludes endpoint

# Logarithmic spacing (powers of 10)
np.logspace(start_exp, stop_exp, num_points)
np.logspace(1, 3, 100)         # 100 points from 10¹ to 10³

# Custom base logarithmic spacing
np.logspace(1, 4, 100, base=2)  # Powers of 2 from 2¹ to 2⁴


# Step-based arrays
np.arange(start, stop, step)
np.arange(0, 10, 0.1)          # 0 to 10 in steps of 0.1
np.arange(10)                  # 0 to 9 (integers)
np.arange(1, 11)               # 1 to 10

# For floating point, better to use:
np.linspace(0, 10, 101)        # More predictable than arange

# Convert a list to numpy array
named_list = np.array(named_list)
```