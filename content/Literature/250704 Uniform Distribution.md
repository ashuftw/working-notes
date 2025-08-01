---
title: Uniform Distribution
draft: true
tags: 
date: 2025-07-04
---
![[../Files/Pasted image 20250704155431.png|center|400]]
The general notation is:


$$
X \sim \mathcal{U}(a, b)
$$
- $a$ is the minimum value (lower bound).
- $b$ is the maximum value (upper bound).
## Variance

$$
\mathbb{V}[X]=\frac{(b-a)^2}{12}
$$
A special case is a uniform distribution defined symmetrically around a mean $\mu$, such as $X \sim \mathcal{U}(\mu-\Delta, \mu+\Delta)$. In this case, the formula simplifies to$\mathbb{V}[X]=\frac{\Delta^2}{3}$


## Expectation for Moments
Expectation values of powers of $\xi$, where $\xi \sim U(-1, 1)$
$$
E\left[\xi^n\right]= \begin{cases}0 & \text { if } \mathrm{n} \text { is odd } \\ \frac{1}{n+1} & \text { if } \mathrm{n} \text { is even }\end{cases}
$$
- $E[\xi] = 0$
- $E[\xi^2] = \frac{1}{3}$
- $E[\xi^3] = 0$ ..
