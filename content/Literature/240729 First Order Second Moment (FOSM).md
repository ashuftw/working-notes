---
title: First Order Second Moment (FOSM)
draft: false
date: 2024-07-29
---

## Use Case

FOSM stands for First-Order Second Moment. It is a technique used to express how uncertainty in a model's inputs affects the uncertainty in its outputs 

It is called "*First-Order*" because it creates a linear (first-order) approximation of the model and "*Second-Moment*" because it focuses on the second statistical moment (variance) of the model output. 

### Mathematical Framework

- **A random variable in terms of deterministic and stochastic components is given by** 




	$$
	X=\bar X+\tilde X
	$$




	Here we assume that $E[X]=\bar X$ and $E[\tilde X]=0$
- **Model $\mathcal M(X)$ can be approximated using first order Taylor expansion around mean**




	$$
	\mathcal{M}(X)=\mathcal{M}(\bar{X}+\tilde{X}) \approx \mathcal{M}(\bar{X})+\mathcal{M}^{\prime}(\bar{X}) \tilde{X}
	$$




### Approximation of Mean 



$$
\begin{align*} 
\mathbb E[ \mathcal{M}(\bar{X})+\mathcal{M}^{\prime}(\bar{X}) \tilde{X}]&= \mathbb E[ \mathcal{M}(\bar{X})]+\mathbb E[\mathcal{M}^{\prime}(\bar{X}) \tilde{X}]\\
& = \mathcal{M}(\bar{X})+\mathcal{M}^{\prime}(\bar{X}) \cancelto{0}{\mathbb E [\tilde{X}]}\\
\end{align*}
$$




$$
\boxed{\mathbb E[\mathcal{M}(X)]\approx \mathcal{M}(\bar{X})}
$$



> This shows that evaluating the model at the mean input is an approximation of the mean output.

### Approximation of Variance

For the variance, we proceed similarly by computing the variance of the Taylor expansion:



$$
\begin{aligned}
V[\mathcal{M}(X)] & \approx V\left[\mathcal{M}(\bar{X})+\mathcal{M}^{\prime}(\bar{X}) \tilde{X}\right] \\
& =V\left[\mathcal{M}^{\prime}(\bar{X}) \tilde{X}\right] \\
& =\left(\mathcal{M}^{\prime}(\bar{X})\right)^2 V[\tilde{X}]
\end{aligned}
$$





$$
\boxed{V[\mathcal{M}(X)] \approx\left(\mathcal{M}^{\prime}(\bar{X})\right)^2 V[\tilde{X}]}
$$

Where $\mathbb E [\tilde{X^2}]= \mathbb V [\tilde{X}]$
> This result shows that the output variance is approximately the product of the squared sensitivity (derivative) at the mean and the input variance, providing a simple way to propagate uncertainty through models.
