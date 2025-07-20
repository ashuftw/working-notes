---
title: File Reading Template
draft: false
tags: 
date: 2025-07-20
---
```python
import numpy as np
# NumPy method
data = np.loadtxt('filename.csv', delimiter=',',skiprows=1) # delimiter='\t' - space separated
# load data 
x, y = data[:,0], data[:,1]
```