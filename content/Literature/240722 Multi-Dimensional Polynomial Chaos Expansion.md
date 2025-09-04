---
title: Multi-Dimensional Polynomial Chaos Expansion
draft: false
date: 2024-07-22
---
## Case 1 

$\xi=\left(\xi_1, \xi_2\right)^{\top} ;\, \xi_1 \sim \mathcal{U}(-\sqrt{3}, \sqrt{3})$ and $\xi_2 \sim \mathcal{N}(0,1)$

Using the generalized Polynomial Chaos (gPC) Expansion



$$
X(\theta)=\sum_{i=0}^{\infty} q_i \Phi_i(\xi(\theta))
$$



**Step 1: Select Basis Functions**
- For Uniform Distribution choose **Legendre** polynomials $L_i$ over $\xi_1$
	- $\mathrm{L}_0\left(\xi_1\right)=1$
	- $\mathrm{L}_1\left(\xi_1\right)=\xi_1$
	- $\mathrm{L}_2\left(\xi_1\right)=(3 / 2) \xi_1{ }^2-1 / 2$
	- $\mathrm{L}_2\left(\xi_1\right)=\frac 1  2(3\xi_1{ }^2-1 )$
- For Gaussian Distribution choose **Hermite** polynomials $H_i$ over $\xi_2$
	- $\mathrm{H}_0\left(\xi_2\right)=1$
	- $\mathrm{H}_1\left(\xi_2\right)=\xi_2$
	- $\mathrm{H}_2\left(\xi_2\right)=\xi_2{ }^2-1$

**Step 2: Calculate the number of Polynomials**



$$
n=\frac{\left(n_{\mathrm{in}}+p\right)!}{n_{\mathrm{in}}!p!}= \frac{(2+2)!}{2!\cdot2!}=6
$$



where $n_\text{in}\rightarrow$ no. of input variables (we have 2 *germs*), $p\rightarrow$ degree of expansion (here both are $2$)
**Step 3: Take all possible combinations**



$$
\begin{aligned}
& \Phi_0\left(\xi_1, \xi_2\right)=L_0\left(\xi_1\right) H_0\left(\xi_2\right)=1 \\
& \Phi_1\left(\xi_1, \xi_2\right)=L_1\left(\xi_1\right) H_0\left(\xi_2\right)=\xi_1 \\
& \Phi_2\left(\xi_1, \xi_2\right)=L_0\left(\xi_1\right) H_1\left(\xi_2\right)=\xi_2 \\
& \Phi_3\left(\xi_1, \xi_2\right)=L_1\left(\xi_1\right) H_1\left(\xi_2\right)=\xi_1 \xi_2 \\
& \Phi_4\left(\xi_1, \xi_2\right)=L_2\left(\xi_1\right) H_0\left(\xi_2\right)=\frac{3}{2} \xi_1^2-\frac{1}{2} \\
& \Phi_5\left(\xi_1, \xi_2\right)=L_0\left(\xi_1\right) H_2\left(\xi_2\right)=\xi_2^2-1\end{aligned}
$$



**Step 3: Represent $X$ as a Series Expansion**
The gPC expansion of the model function $M(\xi)$ up to total polynomial degree 2 is:



$$
X=M(\xi) \approx q_0 \Phi_0(\xi)+q_1 \Phi_1(\xi)+q_2 \Phi_2(\xi)+q_3 \Phi_3(\xi)+q_4 \Phi_4(\xi)+q_5 \Phi_5(\xi)
$$



Substituting the polynomial expressions:



$$
X=M(\xi) \approx q_0+q_1 \xi_1+q_2 \xi_2+q_3\left(\frac{3}{2} \xi_1^2-\frac{1}{2}\right)+q_4 \xi_1 \xi_2+q_5\left(\xi_2^2-1\right)
$$



The coefficients $\mathrm{q}_0$ through $\mathrm{q}_5$ would be determined using methods like [[240723 non-Intrusive Projection|non-intrusive projection]], stochastic collocation, or regression with data from model evaluations.

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

> Note:  $q_i$ is calculated using methods like [[240723 non-Intrusive Projection|non-Intrusive Surrogate Modeling]]