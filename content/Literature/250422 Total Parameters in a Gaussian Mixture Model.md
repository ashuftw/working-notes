---
title: Total Parameters in a Gaussian Mixture Model
draft: false
tags: 
date: 2025-04-22
---

## Formula


$$
\text { Total Parameters }=\underbrace{(K-1)}_{\text {Mixing Coeffs }}+\underbrace{(K \times D)}_{\text {Means }}+\underbrace{\left(K \times \frac{D(D+1)}{2}\right)}_{\text {Covariances }}
$$


## Example

For $K=3$ and $D=5$, this evaluates to


$$
(3-1)+(3 \times 5)+\left(3 \times \frac{5(5+1)}{2}\right)=2+15+(3 \times 15)=62
$$
