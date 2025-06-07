---
title: Bias-Variance decomposition
draft: false
tags: 
date: 2025-06-05
---
## Expected Test Error 
$$
E_{D,\nu}[(t - y(x,w))^2] = \text{bias}_D(y)^2 +\underbrace{ \text{Var}_D(y)}_\text{model variance} + \underbrace{\sigma^2}_\text{noise}
$$

The expectation $E_{D,\nu}[\cdot]$ is taken over both:
1. Different possible training datasets **D** (sampling variability)
2. Different realizations of the noise **ν**

**Note** 
- **Model variance** = $\text{Var}_D(y)$ represents  how much predictions vary with different training sets
- **Noise** Recall $t=f(x)+\nu$
	- $f(x)$ is the true underlying function
	- $\nu \sim \mathcal{N}(0, \sigma^2)$ is Gaussian noise with zero mean and variance $\sigma^2$


## Calculating Individual terms

1. **Bias² = $(f - E_D[y])^2$**
	- How far off your average prediction is from the truth
	- High bias = consistently wrong in the same direction (underfitting)
	- Like a rifle that always shoots left of target
	- $f$ is the true function
2. **Variance = $E_D[(E_D[y] - y)^2]$**
	- High variance = predictions change wildly with different training sets
	- Like a rifle with shaky aim - shots scattered everywhere
3. **Noise = $\sigma^2$**
	- Irreducible error in the data itself
	- Measurement errors, random fluctuations
	- Can't be eliminated no matter how good your model
### The Tradeoff
- **Simple models:** High bias, low variance
- **Complex models:** Low bias, high variance
- **Goal:** Find optimal complexity that minimizes total error

**Key Insight:** You cannot reduce bias and variance simultaneously - there's always a tradeoff. The art of machine learning is finding the right balance.