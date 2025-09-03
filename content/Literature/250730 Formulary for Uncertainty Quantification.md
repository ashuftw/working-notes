---
title: Expectation and Related Formulas
draft: true
tags: 
date: 2025-07-30
---
Some properties of **Expectation** ($\mathbb{E}[X]$) and related concepts like **Variance** ($\mathbb{V}[X]$), compiled for solving problems in uncertainty quantification.

### General Definition and Properties of Expectation

- **Definition of Expectation (Continuous)**

    $$ \mathbb{E}[X] = \int_{-\infty}^{\infty} x f_X(x) dx $$

- **Definition of Expectation (Discrete)**

    $$ \mathbb{E}[X] = \sum_i x_i \mathbb{P}(X=x_i) $$

- **Linearity of Expectation**

    $$ \mathbb{E}[aX + bY] = a\mathbb{E}[X] + b\mathbb{E}[Y] $$

- **Expectation of a Constant**

    $$ \mathbb{E}[c] = c $$

- **Expectation of Independent Variables**

    $$ \mathbb{E}[XY] = \mathbb{E}[X]\mathbb{E}[Y] \quad \text{(if X and Y are independent)} $$

### Variance and Covariance

- **Definition of Variance**

    $$ \mathbb{V}[X] = \mathbb{E}[(X - \mathbb{E}[X])^2] $$

- **Computational Formula for Variance**

    $$ \mathbb{V}[X] = \mathbb{E}[X^2] - (\mathbb{E}[X])^2 $$

- **Properties of Variance**

    $$ \mathbb{V}[X+a] = \mathbb{V}[X] $$

    $$ \mathbb{V}[aX] = a^2 \mathbb{V}[X] $$

- **Variance of a Sum of Independent Variables**

    $$ \mathbb{V}\left[\sum_{i=1}^{K} X^{(i)}\right] = \sum_{i=1}^{K} \mathbb{V}[X^{(i)}] $$

- **Definition of Covariance**

    $$ \text{cov}(X,Y) = \mathbb{E}[(X - \mathbb{E}[X])(Y - \mathbb{E}[Y])] $$

- **Computational Formula for Covariance**

    $$ \text{cov}(X,Y) = \mathbb{E}[XY] - \mathbb{E}[X]\mathbb{E}[Y] $$

### Polynomial Chaos Expansions (PCE)

- **Expectation from gPC Coefficients**: 
    $$ \mathbb{E}[Y] = q_0 \quad \text{for} \quad Y \approx \sum_{i=0}^{P} q_i \Phi_i(\xi) $$
	The mean is the first coefficient.
- **Variance from gPC Coefficients**

    $$ \mathbb{V}[Y] = \sum_{i=1}^{P} q_i^2 $$

- **Raw Second Moment from gPC Coefficients**

    $$ \mathbb{E}[Y^2] = \mathbb{V}[Y] + (\mathbb{E}[Y])^2 = \sum_{i=1}^{P} q_i^2 + q_0^2 $$

- **Projection Formula for Coefficients**

    $$ q_i = \frac{\mathbb{E}[\mathcal{M}(X(\xi))\Phi_i(\xi)]}{\mathbb{E}[\Phi_i^2(\xi)]} $$

### Monte Carlo (MC) Methods

- **Expectation of the MC Estimator**: The estimator is unbiased.

    $$ \mathbb{E}[\hat{\mu}_K] = \mu
    
    $$
    where, 
    $$
    \mathbb E[\hat \mu_K]=\frac{1}{k}\sum_{i=1}^{K}y^{(i)}=\frac{1}{k}\sum_{i=1}^{K}\mathcal{M}(x^{(i)})$$
	

- **Mean-Square Error (MSE) of an Estimator Z**: This is a general relation.

    $$ \mathbb{E}[(Z - \mathbb{E}[X])^2] = \mathbb{V}[Z] + (\mathbb{E}[Z] - \mathbb{E}[X])^2 $$

- **MSE for the Unbiased MC Estimator**

    $$ \mathbb{E}[(\hat{\mu}_K - \mathbb{E}[X])^2] = \mathbb{V}[\hat{\mu}_K] = \frac{\mathbb{V}[X]}{K} $$

- **Multi-Fidelity Monte Carlo (MFMC) Expectation**

    $$ \mathbb{E}[f_H(x)] = \mathbb{E}[f_H(x) - f_L(x)] + \mathbb{E}[f_L(x)] $$

### Specific Distributions

- **Expectation of a Uniform Distribution** $X \sim \mathcal{U}(a,b)$

    $$ \mathbb{E}[X] = \frac{a+b}{2} $$

- **Expectation of a Standard Normal Distribution** $X \sim \mathcal{N}(0,1)$

    $$ \mathbb{E}[X] = 0 $$

What are the expectation values of powers of $\xi$, where $\xi \sim U(-1, 1)$?
$$
E\left[\xi^n\right]= \begin{cases}0 & \text { if } \mathrm{n} \text { is odd } \\ \frac{1}{n+1} & \text { if } \mathrm{n} \text { is even }\end{cases}
$$
- $E[\xi] = 0$
- $E[\xi^2] = \frac{1}{3}$
- $E[\xi^3] = 0$
---
**General Rule:**
- For **n odd**: $E[\xi^n] = 0$
- For **n even**: $E[\xi^n] = \frac{1}{n+1}$