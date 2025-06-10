---
title: Parameter Estimation for Maximum Likelihood
draft: false
date: 2024-05-14
---

## Use-case: Why We Need Parameter Estimation

Parameter estimation is essential in pattern recognition because:
1. In Bayesian classifiers, we must estimate the likelihood $p(x \mid s=i)$ and prior probabilities $P(s=i)$ to calculate posterior probabilities $P(s=i \mid \boldsymbol{x})$.
2. Real-world data distributions have unknown parameters that must be learned from training data.
3. Proper parameter estimation allows our model to generalize to unseen data.
4. The parameters define the specific instance of our model (e.g., which Gaussian from all possible Gaussians).

### Maximum Likelihood (ML) Parameter Estimation

For a dataset of observation vectors $\mathbf{X}=\left\{\mathbf{x}_1, \mathbf{x}_2, \ldots, \mathbf{x}_n\right\}$, assuming they are independent and identically distributed (i.i.d.), the likelihood of the training material is:

$$
p(\mathbf{X} \mid \boldsymbol{\theta})=\prod_{n=1}^N p\left(\mathbf{x}_n \mid \boldsymbol{\theta}\right)
$$

The **Maximum Likelihood (ML)** Parameter Estimation finds the parameter vector $\boldsymbol{\theta}$ that maximizes this likelihood:

$$
\boldsymbol{\theta}_{\mathrm{ML}}=\underset{\boldsymbol{\theta}}{\arg \max }\, p(\mathbf{X} \mid \boldsymbol{\theta})
$$

**ML Estimate of the Mean**

$$
\boxed{
\hat{\boldsymbol{\mu}}=\frac{1}{N} \sum_{n=1}^N \mathbf{x}_n
}
$$

**ML Estimate of the Covariance Matrix**

$$
\boxed{
\hat{\boldsymbol{\Sigma}}=\frac{1}{N} \sum_{n=1}^N\left(\mathbf{x}_n-\hat{\boldsymbol{\mu}}\right)\left(\mathbf{x}_n-\hat{\boldsymbol{\mu}}\right)^T
}
$$

where:
- $N$ is the total number of samples.
- $\mathbf{x}_n$ is the $n$-th sample.
- ^ represents the fact that the parameters are estimated. 