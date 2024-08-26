Status: #finished
## Use-case
In pattern recognition, we simplify the process of finding the distribution of a random variable by considering making an assumption that the distribution could be reasonably represented by a Gaußian. Thus we now only have to find the parameters that define the Gaußian. By selecting the right parameters that fit the data, we can use this model to make predictions based on new, unseen data. 
### Multivariate Gaussian model used to represent **Likelihood**

$$
p (\mathbf{x} \mid \boldsymbol{\theta}) \sim \mathcal{N}(\mathbf{x} ; \boldsymbol{\mu}, \boldsymbol{\Sigma})
$$

Parameter vector for Maximum Likelihood $\hat \theta$ consists of all the elements of $\hat \mu,\hat \Sigma$
**ML Estimate of the Mean**

$$
\boxed{
\hat{\boldsymbol{\mu}}=\frac{1}{T} \sum_{\tau=1}^T \mathbf{o}_\tau
}
$$


**ML Estimate of the Covariance Matrix**

$$
\boxed{
\hat{\boldsymbol{\Sigma}}=\frac{1}{T} \sum_{\tau=1}^T\left(\mathbf{o}_\tau-\hat{\boldsymbol{\mu}}\right)\left(\mathbf{o}_\tau-\hat{\boldsymbol{\mu}}\right)^T
}
$$

where:
- $T$ is the total number of samples.
- $\mathbf{o}_\tau$ is the $\tau$-th sample.



---
# References
