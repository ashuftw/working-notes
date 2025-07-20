---
title: Plot Fills
draft: false
tags: 
date: 2025-07-20
---

### 1. **Splitting data at point** 
```python
# Find index where variable is closest to split_value
split_value = 0  # Change as needed (e.g., x=0, y=0, etc.)
split_var = x    # Change to variable you're splitting by

split_idx = np.argmin(np.abs(split_var - split_value))

# Split into two parts (both include the split point)
x_part1 = x[:split_idx+1]  # Start to split point (inclusive)
y_part1 = y[:split_idx+1]
x_part2 = x[split_idx:]    # Split point to end
y_part2 = y[split_idx:]

```

### 2. **Preparing Data for Interpolation** 
```python
# Method A: Sort to ensure monotonic x-values
sort_idx1 = np.argsort(x_part1)
x_part1, y_part1 = x_part1[sort_idx1], y_part1[sort_idx1]

sort_idx2 = np.argsort(x_part2)
x_part2, y_part2 = x_part2[sort_idx2], y_part2[sort_idx2]

# Method B: Check and reverse if needed
if x_part1[0] > x_part1[-1]:  # If decreasing
    x_part1, y_part1 = x_part1[::-1], y_part1[::-1]
```

### 3. **Interpolation** 
```python
# Find common x-range
x_min = max(x_part1.min(), x_part2.min())
x_max = min(x_part1.max(), x_part2.max())

# Create high-resolution common x-axis
x_common = np.linspace(x_min, x_max, 1000)  # 1000 points

# Interpolate both curves
y_part1_interp = np.interp(x_common, x_part1, y_part1)
y_part2_interp = np.interp(x_common, x_part2, y_part2)
```

### 4. **Fill between**
```python
fig, ax = plt.subplots(figsize=(8,6))

# Plot original curves
ax.plot(x_part1, y_part1, 'r-', label='Part 1')
ax.plot(x_part2, y_part2, 'g-', label='Part 2')

# Fill between interpolated curves
ax.fill_between(x_common,           # x-values
                y_part2_interp,     # y1 (bottom/first curve)
                y_part1_interp,     # y2 (top/second curve)
                color='gray',       # fill color
                label='Filled area')


```