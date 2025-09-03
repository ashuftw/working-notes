---
title: Expectation Maximization Algorithm
draft: false
date: 2024-08-21
---
It is an iterative algorithm used to estimate the parameters of a [[240514 Multivariate Gaussian Model and Gaussian Mixture Model|Gaussian Mixture Models]]. The algorithm alternates between two steps:
1.  **E-step**: Calculates the posterior probabilities (responsibilities) of each data point belonging to each Gaussian component.
2.  **M-step**: Uses these responsibilities to re-calculate the GMM parameters (weights, means, and covariances).