---
title: Curse of Dimensionality in Quadrature Rules
draft: true
tags:
date: 2025-09-04
---
The [[250729 Quadrature to Approximate Expected Value|quadrature rules]] can be extended from a **single** input variable to **multiple** **dimensions**? This is is possible by taking all possible combinations of the one-dimensional nodes for each variable, thus creating a multi-dimensional grid of points. This construction is called a **Tensor Product Rule**.

## Drawback
The total number of points ($n_{qu;1} \cdot n_{qu;2} \cdot ...$) grows exponentially with the number of input dimensions, making it computationally infeasible. This is the **"curse of dimensionality"**. 

## Solution Strategy: Sparsegrids
A strategy to mitigate this is using **Sparse Grids**, which intelligently leave out less significant points from the full tensor grid.

The plots show how different quadrature rules (Sparse Grid vs. Tensor Grid) select these evaluation points within the input parameter space to approximate the expected value of the model's output. 
![[../Files/Pasted image 20250904150619.png]]
Where, 
- The axis labels represent the values of the two independent input variables (normalized), let's call them $X_1$ and $X_2$, over which a numerical integration is performed. 
- Each blue dot on the plots is a quadrature node-a specific point ( $x_1, x_2$ ) where the model function $\mathcal{M}\left(X_1, X_2\right)$ is evaluated.
