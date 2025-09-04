---
title: Gaussian Mixture Model
draft: true
tags: 
date: 2025-07-27
---
A [[240305 Normal or Gaussian Distribution|Gaussian]] Mixture Model (GMM) represents a probability distribution as a weighted sum of multiple Gaussian distributions. The general formula for a GMM is:


$$
p(x) = \sum_{k=1}^{K} \pi_k N(x | w_k, \Sigma_k)
$$


Here, $K$ is the number of Gaussian components in the mixture.
The parameters of a GMM that need to be determined are:
* $w_k$: The mean (or center) of each Gaussian component $k$. This is similar to the prototype in k-means.
* $\Sigma_k$: The covariance matrix of each Gaussian component $k$, which controls its shape and extension.
* $\pi_k$: The mixing coefficient (or weight) for each Gaussian component $k$.
