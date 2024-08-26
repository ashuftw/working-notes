---
title: Multivariate Gaussian PDF
draft: false
tags:
---

Assume $X$ is an independent Random **Vector**. Then the[[230712 Joint Density|Joint Density]] is given by 

$$
f_{\boldsymbol{X}}(\boldsymbol{x})=f_{X_1}\left(x_1\right) \cdots f_{X_n}\left(x_n\right)
$$

In the multivariate Gaussian Case, $X$ is normally distributed (Mean is in the center). Then we can represent $X$ as
$$
X\sim\mathcal N(\mu_X, C_X)
$$

Where Mean Vector $\mu_X=\mathbb{E}[X]$ and Covariance Matrix $C_X = \text C[X,X]$ 

The PDF of the Multivariate Gaussian is then given by

$$
f_{\boldsymbol{X}}(\boldsymbol{x})=\frac{1}{\sqrt{(2 \pi)^n \operatorname{det}\left(\boldsymbol{C}_{\boldsymbol{X}}\right)}} \mathrm{e}^{-\frac{1}{2}\left(\boldsymbol{x}-\boldsymbol{\mu}_{\boldsymbol{X}}\right)^{\top} \boldsymbol{C}_{\boldsymbol{X}}^{-1}\left(\boldsymbol{x}-\boldsymbol{\mu}_{\boldsymbol{X}}\right)}
$$

Example for Random Vector of size 2

![[Pasted image 20230606142207.png]]
Here, $\mathcal N(0, 1)\rightarrow$ Normal distribution with Mean $0$ and Variance $1$


