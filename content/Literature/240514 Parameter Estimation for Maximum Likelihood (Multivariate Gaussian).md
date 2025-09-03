---
title: Parameter Estimation for Maximum Likelihood (Multivariate Gausssian)
draft: false
date: 2024-05-14
---
### Maximum Likelihood (ML) Parameter Estimation

The maximum likelihood estimate finds parameters $\theta$ that maximize the likelihood of observing the training data:
$$
\hat{\boldsymbol{\theta}}^{ML} = \arg\max_{\boldsymbol{\theta}} L(\boldsymbol{\theta}) = \arg\max_{\boldsymbol{\theta}} p(\boldsymbol{\mathbf O|\theta})
$$
In practice, we maximize the **log-likelihood** $\mathrm{LL}(\boldsymbol{\theta})$
$$
\hat{\boldsymbol{\theta}}^{(\mathrm{ML})}=\arg \max _{\boldsymbol{\theta}} \mathrm{LL}(\boldsymbol{\theta})=\arg \max_\theta\sum_{\tau=1}^T \log \mathrm{p}\left(\mathbf{x}=\mathbf{o}_\tau \mid \boldsymbol{\theta}\right)
$$

To find the parameters that maximize the likelihood of observing the training data, one must find the maximum of the log-likelihood function, $LL(\theta)$. This is typically done by taking the **partial derivative** with respect to each parameter, **setting it to zero**, and solving the resulting system of equations.

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

In pattern recognition, we need parameter estimation to **train classifiers** by determining the unknown parameters of probability distributions from training data. They are:
- **Prior probabilities** $P(s=i)$
- **Likelihood probability density functions** $p(\mathbf{x}|s=i)$

Assuming that the Likelihood can by represented by a Gaussian, we find **mean $\mu_i$** and **covariance $\Sigma_i$**
such that it closely represents the **Likelihood**.  The ML estimates for the parameters are estimated as follows:
-   **Sample Mean (unbiased):** This is the average of all the training vectors.
    $$\hat{\mu} = \frac{1}{T} \sum_{\tau=1}^{T} o_{\tau}$$
-   **Sample Covariance (unbiased):** This is the average of the outer products of the centered data vectors. 
    $$\hat{\Sigma} = \frac{1}{T-1} \sum_{\tau=1}^{T} (o_{\tau} - \hat{\mu})(o_{\tau} - \hat{\mu})^T$$*Note: Using a denominator of T-1 provides an unbiased estimate.*
