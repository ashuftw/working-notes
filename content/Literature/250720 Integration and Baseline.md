---
title: Integration and Baseline
draft: false
tags: 
date: 2025-07-20
---
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