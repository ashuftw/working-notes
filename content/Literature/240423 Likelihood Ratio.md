---
title: Likelihood Ratio
draft: false
date: 2024-04-23
---

## Use-case 

The [[240423 Likelihood Ratio|Likelihood Ratio]] defines a [[250505 Discriminant Function|Discriminant Function]] without biases (priors) in the context of a [[240410 Bayesian Classifier|Bayesian classifier]]. 

### Mathematical Definition 

For a two class case,



$$
\boxed{ LR(\mathbf{x}) = \frac{p(\mathbf{x}|s = 1)}{p(\mathbf{x}|s = 2)} > \theta \Rightarrow \text{Decide for } s = 1, \text{ else for } s = 2. 
}
$$



## Variants of the threshold:

- **Maximum Likelihood Decision** 





	$$
	\theta = 1
	$$





Simple decision

- **Bayes Decision**  





	$$
	\theta = \dfrac{P(s = 2)}{P(s = 1)}
	$$





Makes use of Prior
- **Bayes Risk Decision** 





	$$
	\theta = \frac{\lambda_{1\textcolor{red}2} - \lambda_{2\textcolor{red}2}}{\lambda_{2\textcolor{blue}1} - \lambda_{1\textcolor{blue}1}} \cdot \frac{\textcolor{red}{P(s = 2)}}{\textcolor{blue}{P(s = 1)}}
	$$





Use Prior and Cost

> Note: $\lambda_{12}$ is the cost of deciding state $1$ given state $2$ is true, so an and so forth. 

![[../Files/Pasted image 20240423154225.png]]

> Note: The threshold has same units as the $y-$axis.

---

# References

[[Private/Excalidraw/Drawing 2024-08-19 12.05.49.excalidraw.md#^JEVRL-PwRECHjrQpPAmtn|Source]]
