---
title: Bayesian Discriminant Function (Gaussian)
draft: false
tags: 
date: 2025-08-14
---
## Decision Surface 
 For a classifier where the likelihood for each class is a multivariate Gaussian distribution, the decision surfaces are generally **hyperquadrics**. A hyperquadric is a generalization of conic sections (like ellipses, parabolas, and hyperbolas) to higher dimensions. This means the boundaries separating the classes can be hyperplanes, pairs of hyperplanes, hyperspheres, hyperellipsoids, or hyperparaboloids.
## Discriminant Function
Assuming a minimum-error-rate classification and Gaussian likelihoods $p(x|s=i) \sim \mathcal{N}(x;\mu_i, \Sigma_i)$, the logarithmic discriminant function is:

$$
g_i(x) = \ln p(x|s=i) + \ln P(s=i)
$$


Expanding the Gaussian term, we get:
$$
g_i(x) = -\frac{1}{2}(x-\mu_i)^T\Sigma_i^{-1}(x-\mu_i) -\cancel{ \frac{d}{2}\ln(2\pi)} - \frac{1}{2}\ln(|\Sigma_i|) + \ln P(s=i)
$$

The term $(x-\mu_i)^T\Sigma_i^{-1}(x-\mu_i)$ is a quadratic form in $x$, which is why the resulting decision boundaries $g_i(x) = g_j(x)$ are hyperquadrics. The term $-\frac{d}{2}\ln(2\pi)$ is a constant across all classes and can be ignored.

What happens to the decision surface of a Gaussian classifier in the special case where all covariance matrices are equal and diagonal, i.e., $\Sigma_i = \sigma^2I$?

## Special Case: Covariance matrices are equal and diagonal
When the covariance matrix for every class $i$ is assumed to be $\Sigma_i = \sigma^2I$, it means the features are statistically independent and have the same variance $\sigma^2$ for all classes. In this case, the quadratic term in the discriminant function simplifies, and the decision surface becomes a **hyperplane**. 
The discriminant function simplifies to:
$$
g_i(x) = -\frac{||x-\mu_i||^2}{2\sigma^2} + \ln P(s=i)
$$
where $||x-\mu_i||^2$ is the squared Euclidean distance. The quadratic terms $x^Tx$ cancel out when comparing $g_i(x)$ and $g_j(x)$, leaving a linear equation in $x$, which defines a hyperplane.

## Special Case: Covariance matrices are equal and diagonal AND a flat prior?
If we have the special case of equal diagonal covariances ($\Sigma_i = \sigma^2I$) and a flat prior ($P(s=i) = \frac{1}{N}$ for all classes), the discriminant function simplifies even further to:
$$
g_i(x) = -||x-\mu_i||^2
$$
Maximizing this $g_i(x)$ is equivalent to **minimizing the Euclidean distance** $||x-\mu_i||$. Therefore, the classifier simply assigns a feature vector $x$ to the class with the nearest mean $\mu_i$. This is known as a **minimum Euclidean distance classifier**.