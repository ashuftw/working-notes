---
title: Common Patterns
draft: true
tags: 
date: 2025-05-22
---
### File Reading Patterns:
```python
# CSV with headers
data = np.genfromtxt('file.csv', delimiter=',', names=True)
x_data = data['column1'] 
y_data = data['column2']

# Excel reading
import pandas as pd
df = pd.read_excel('file.xlsx')
# or with openpyxl for writing

# Text file line by line
with open('file.txt', 'r') as f:
    lines = f.readlines()
```

### Data Processing Patterns:

```python
# Remove outliers/clean data
mask = (data > lower_bound) & (data < upper_bound)
clean_data = data[mask]

# Statistical analysis
mean_val = np.mean(data)
std_val = np.std(data)  
max_val = np.max(data)
min_val = np.min(data)

# Find indices
max_idx = np.argmax(data)
min_idx = np.argmin(data)
```
