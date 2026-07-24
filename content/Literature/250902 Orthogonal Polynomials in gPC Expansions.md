---
title: Orthogonal Polynomials in gPC Expansions
draft: true
tags:
date: 2025-09-02
---
The primary use of orthogonal polynomials in the lecture notes is to serve as the **basis functions** for the **generalized Polynomial Chaos (gPC) expansion**. A random variable or model output $Y$ is approximated by a series of these polynomials:

$$
Y \approx \tilde{Y} = \sum_{i=0}^{n}q_{i}\Phi_{i}(\xi)
$$

The choice of polynomial family (e.g., Hermite, Legendre) is dictated by the distribution of the underlying random variable (the "germ") $\xi$ to satisfy the orthogonality condition.

The orthogonality property is crucial because it greatly simplifies computations:

1.  **Efficient Coefficient Calculation**: The coefficients $q_i$ can be calculated efficiently using a projection. Because $\mathbb{E}[\Phi_i \Phi_j] = 0$ for $i \neq j$, each coefficient can be found independently without solving a large system of equations:


	$$
	q_{j} = \frac{\mathbb{E}[Y \cdot \Phi_{j}(\xi)]}{\mathbb{E}[\Phi_{j}(\xi)^{2}]}
	$$



2.  **Direct Moment Extraction**: Moments of the approximated output $\tilde{Y}$ can be computed directly from the gPC coefficients. Assuming the polynomials are normalized ($\mathbb{E}[\Phi_i^2]=1$, and $\Phi_0=1$):
    - **Mean**: The mean is simply the first coefficient, $q_0$.


    	$$
    	\mathbb{E}[\tilde{Y}] = \mathbb{E}[\sum_{i=0}^{n}q_{i}\Phi_{i}(\xi)] = q_0 \mathbb{E}[\Phi_0] = q_0
    	$$


    - **Variance**: The variance is the sum of the squares of the other coefficients.


    	$$
    	\mathbb{V}[\tilde{Y}] = \mathbb{E}[(\tilde{Y} - q_0)^2] = \mathbb{E}[(\sum_{i=1}^{n}q_{i}\Phi_{i}(\xi))^2] = \sum_{i=1}^{n}q_{i}^{2}
    	$$



In short, using an orthogonal polynomial basis turns a complex approximation problem into a much simpler one by decoupling the terms in the expansion, allowing for straightforward calculation of coefficients and statistical moments.