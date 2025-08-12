---
title: Parameter Estimation for Maximum Likelihood
draft: false
date: 2024-05-14
---

### Maximum Likelihood (ML) Parameter Estimation

The maximum likelihood estimate finds parameters $w$ that maximize the likelihood of observing the training data:

$$
\hat{\boldsymbol{w}}_{ML} = \arg\max_{\boldsymbol{w}} L(\boldsymbol{w}) = \arg\max_{\boldsymbol{w}} \prod_{n=1}^{N} p(\mathbf{x}_n|\boldsymbol{w})
$$
In practice, we maximize the **log-likelihood**:
$$
\hat{\boldsymbol{w}}_{ML} = \arg\max_{\boldsymbol{w}} \sum_{n=1}^{N} \log p(\mathbf{x}_n|\boldsymbol{w})
$$
To find the parameters that maximize the likelihood of observing the training data, one must find the maximum of the log-likelihood function, $LL(\theta)$. This is typically done by taking the partial derivative with respect to each parameter, setting it to zero, and solving the resulting system of equations.

The formula is:
$$ \frac{\partial}{\partial\theta_r} LL(\theta) = \sum_{\tau=1}^{T} \frac{\partial}{\partial\theta_r} \log p(x=o_{\tau}|\theta) \stackrel{!}{=} 0, \quad \text{for } r=1,2,...,R $$

- **$\hat{\theta}^{(ML)}$**: The parameter vector that maximizes the likelihood.
- **$LL(\theta)$**: The log-likelihood function.
- **$o_{\tau}$**: The training data vectors.
- **$\theta_r$**: The individual parameters to be estimated.
- $T$: Total training samples in the dataset
- $T$: Total parameters in the model (that need to be estimated) 

> **Note:**  $\stackrel{!}{=} 0$ This notation means "**set equal to zero**". We set the derivative to zero to find the critical points (maxima, minima, or saddle points) of the log-likelihood function. In this context, we are looking for the maximum.
***

### Why Parameter Estimation is Needed

In pattern recognition, we need parameter estimation to **train classifiers** by determining the unknown parameters of probability distributions from training data. (we assume that the likelihood functions can be represented with a known distribution.

Specifically, we need to estimate:
- **Prior probabilities** $P(s=i)$
- **Likelihood probability density functions** $p(\mathbf{x}|s=i)$

While priors are often simple to estimate, determining the likelihood pdfs is more complex. In **parametric estimation**, we assume the likelihood function follows a known mathematical form (e.g., a Gaussian distribution), but its specific parameters (like the **mean $\mu_i$** and **covariance $\Sigma_i$**) are unknown.

Therefore, **parameter estimation is the process of using the training data to calculate these unknown parameters**. Once estimated, these parameters define the likelihood functions, enabling the Bayesian classifier to compute the necessary posterior probabilities and make informed decisions about class membership. 