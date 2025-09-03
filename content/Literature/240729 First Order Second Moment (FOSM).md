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





> [!note]
> It's not a good idea to use FOSM if the model is highly non-linear. Because:
> - FOSM is modeled around the mean. 
> - It requires only the model's output and it's derivatives at a single point (the mean).
 