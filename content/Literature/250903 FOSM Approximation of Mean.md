---
title: FOSM Approximation of Mean
draft: false
tags:
date: 2025-09-03
---
For the mean, we proceed by [[240729 First Order Second Moment (FOSM)|computing]] the expected value of the Taylor expansion:

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