---
title: Multi-Dimensional Polynomial Chaos Expansion
draft: false
date: 2024-07-22
---

## Case 1 
$\xi=\left(\xi_1, \xi_2\right)^{\top} ;\, \xi_1 \sim \mathcal{U}(-\sqrt{3}, \sqrt{3})$ and $\xi_2 \sim \mathcal{N}(0,1)$
- **Step 1: Select Basis Functions**
	- *Choose Legendre polynomials* $L_i$ over $\xi_1$
	- *Choose Hermite polynomials* $H_i$ over $\xi_2$
- **Step 3: Take all possible combinations**
$$
\begin{aligned}
& \Phi_0\left(\xi_1, \xi_2\right)=L_0\left(\xi_1\right) H_0\left(\xi_2\right)=1 \\
& \Phi_1\left(\xi_1, \xi_2\right)=L_1\left(\xi_1\right) H_0\left(\xi_2\right)=\xi_1 \\
& \Phi_2\left(\xi_1, \xi_2\right)=L_0\left(\xi_1\right) H_1\left(\xi_2\right)=\xi_2 \\
& \Phi_3\left(\xi_1, \xi_2\right)=L_1\left(\xi_1\right) H_1\left(\xi_2\right)=\xi_1 \xi_2 \\
& \Phi_4\left(\xi_1, \xi_2\right)=L_2\left(\xi_1\right) H_0\left(\xi_2\right)=\frac{3}{2} \xi_1^2-\frac{1}{2} \\
& \Phi_5\left(\xi_1, \xi_2\right)=L_0\left(\xi_1\right) H_2\left(\xi_2\right)=\xi_2^2-1\end{aligned}
$$

	The Number of polynomials is give by
$$
n=\frac{\left(n_{\mathrm{in}}+p\right)!}{n_{\mathrm{in}}!p!}
$$

	where $n_\text{in}\rightarrow$ no. of variables, $p\rightarrow$ degree of expansion (here both are $2$)
- **Step 3: Represent $X$ as a Series Expansion:**

$$
X \approx \sum_{i=0}^{\infty} q_i \Phi_i\left(\zeta_1, \zeta_2\right)
$$

## Case 2 
Consider $Y_i=u(t_i)$ denote a random solution to different points in time $t_i$ 
- **Step 1: gPC Surrogate Model**   
$$
\gamma \approx \widetilde{\mathcal{M}}(\boldsymbol{\xi})=\sum_{i=0}^n q_i \Phi_i(\boldsymbol{\xi})
$$

- **Step 2: Approximate Moments using gPC coefficient $q_i$**
$$
\tilde{M}^k[r] \approx \sum_{i=0}^n q_i^k
$$

- **Step 3: Evaluate gPC Surrogate $\widetilde{\mathcal{M}}$ with different input Random Variables.**

> Note:  $q_i$ is calculated using methods like [[240723 non-Intrusive Surrogate Modeling|non-Intrusive Surrogate Modeling]]


