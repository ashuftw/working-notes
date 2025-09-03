---
title: FOSM Approximation of Variance
draft: false
tags:
date: 2025-09-03
---

For the variance, we proceed by [[240729 First Order Second Moment (FOSM)|computing]] the variance of the Taylor expansion:



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