---
title: Parameter Estimation for Maximum Likelihood
draft: false
date: 2024-05-14
---
## Use-case: Why We Need Parameter Estimation

In pattern recognition, we need parameter estimation to **train classifiers** by determining the unknown parameters of probability distributions from training data. Specifically, we need to estimate:
- Prior probabilities $P(s=i)$
- Likelihood probability density functions $p(\mathbf{x}|s=i)$

### Maximum Likelihood (ML) Parameter Estimation

The maximum likelihood estimate finds parameters $\boldsymbol{\theta}$ that maximize the likelihood of observing the training data:


$$
\hat{\boldsymbol{\theta}}_{ML} = \arg\max_{\boldsymbol{\theta}} L(\boldsymbol{\theta}) = \arg\max_{\boldsymbol{\theta}} \prod_{n=1}^{N} p(\mathbf{x}_n|\boldsymbol{\theta})
$$


In practice, we maximize the **log-likelihood**:


$$
\hat{\boldsymbol{\theta}}_{ML} = \arg\max_{\boldsymbol{\theta}} \sum_{n=1}^{N} \log p(\mathbf{x}_n|\boldsymbol{\theta})
$$


### For a multivariate Gaussian distribution, the ML estimates are:
- **Mean**: $\hat{\boldsymbol{\mu}} = \frac{1}{N} \sum_{n=1}^{N} \mathbf{x}_n$ (sample mean)
- **Covariance**: $\hat{\boldsymbol{\Sigma}} = \frac{1}{N} \sum_{n=1}^{N} (\mathbf{x}_n - \hat{\boldsymbol{\mu}})(\mathbf{x}_n - \hat{\boldsymbol{\mu}})^T$ (sample covariance)