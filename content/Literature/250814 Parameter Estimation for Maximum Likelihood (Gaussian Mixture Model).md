---
title: Parameter Estimation for Maximum Likelihood (Gaussian Mixture Model)
draft: false
tags: 
date: 2025-08-14
---
 A GMM is a sum of multiple weighted Gaussian components: 
 $$
 p(x|\theta) \sim \sum_{k=1}^{K} c_k \cdot \mathcal{N}(x;\mu_k, \Sigma_k)
 $$
 
When trying to find the ML estimates for all the weights ($c_k$), means ($\mu_k$), and covariances ($\Sigma_k$), the set of equations derived from setting the partial derivatives of the log-likelihood to zero **cannot be solved directly**. 
 
This is because of the sum inside the logarithm, which makes a closed-form solution intractable. Instead, iterative methods like the **[[240821 Expectation Maximization Algorithm|Expectation-Maximization (EM) algorithm]]*** are required.