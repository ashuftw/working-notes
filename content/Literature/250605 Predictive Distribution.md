---
title: Predictive Distribution
draft: false
tags: 
date: 2025-06-05
---
For a given input a [[250605 Predictive Distribution|predictive distribution]] tells you the likely output value and how spread out (uncertain) it is. 

**Mathematically:**
$$
p(t \mid x, \text { training data })=\mathcal{N}\left(t \mid m(x), s^2(x)\right)
$$
> The probability of getting output value $t$, given input $x$ and our training data

where,
- $m(x)=$ most likely prediction (mean)
- $s^2(x)=$ uncertainty of prediction (variance)
- The prediction is a Gaussian bell curve centered at $m(x)$

**To generalize with the predictive distribution:**
- Use the mean $m(x)$ as the predicted value
- Use the variance $s^2(x)$ to express confidence in the prediction
