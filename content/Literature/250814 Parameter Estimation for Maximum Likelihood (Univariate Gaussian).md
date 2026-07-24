---
title: Parameter Estimation for Maximum Likelihood (Univariate Gaussian)
draft: false
tags: 
date: 2025-08-14
---
A univariate Gaussian is a special case of a multivariate Gaussian where the data is one-dimensional. The parameter vector is $\theta = [\mu, \sigma^2]^T$. 

The ML estimation process is analogous to the [[240514 Parameter Estimation for Maximum Likelihood (Multivariate Gaussian)|multivariate case]]:

-   The **ML estimate of the mean ($\hat{\mu}$)** is the sample mean (average) of the scalar training data points.


	$$
	\hat{\mu} = \frac{1}{T} \sum_{\tau=1}^{T} o_{\tau}
	$$


-   The **ML estimate of the variance ($\hat{\sigma^2}$)** is the sample variance of the training data.


	$$
	\hat{\Sigma} = \frac{1}{T-1} \sum_{\tau=1}^{T} (o_{\tau} - \hat{\mu})(o_{\tau} - \hat{\mu})^T
	$$


	*Note: Using a denominator of T-1 provides an unbiased estimate.*