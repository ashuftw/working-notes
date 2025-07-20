---
title: Radial Basis Function
draft: false
tags: 
date: 2025-06-27
---
![[../Files/Pasted image 20250701134853.png|center|700]]

Where, $i$ is the number of outputs ($1$) and $j$ is the number of inputs $D$

**Key Model Selection Decisions:**

1. **Number of RBF units (hidden neurons)** -  How many radial basis functions to use in the hidden layer
2. **RBF centers** - Where to position each RBF unit in the **input space** (the centers of the Gaussian functions)
3. **RBF widths (σ or spread parameters)** - The width/spread of each radial basis function, which controls how much of the **input space each unit responds to**.
4. **Output weights ($w_{i,j}^\text{out}$)** - The weights connecting the RBF units to the output layer