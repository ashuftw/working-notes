---
title: Basic Plotting
draft: false
tags: 
date: 2025-07-20
---
**Single Plot**
```python
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8,6))
ax.plot(x, y, color='blue', linestyle='-', label='Label1')
ax.plot(v, w, color='red', linestyle='-', label='Label2') # two plots
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.legend() #ax.legend(loc='upper left')
ax.grid(True)
plt.tight_layout()
plt.savefig('name.png')
plt.show()

ax.set_xlim(0,3) # if data has a range
plt.clf() # Clear the current figure 
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