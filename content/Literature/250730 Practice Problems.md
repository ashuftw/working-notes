---
title: Practice Problems
draft: true
tags: 
date: 2025-07-30
---
## GPC (Mock 2025)
Consider a model $Y=\mathcal{M}(\boldsymbol{X})=\mathcal{M}(\boldsymbol{X}(\boldsymbol{\xi}))$. For a simple model function $\mathcal{M}\left(X_1, X_2\right)=3 X_1+2 X_2^2+1.5$, use a non-intrusive projection approach to find the coefficients $q_i$ of a linear gPC Ansatz
$$
Y \approx q_0+q_1 \Phi_1(\boldsymbol{\xi})+q_2 \Phi_2(\boldsymbol{\xi}) .
$$

An expansion for the random vector $\boldsymbol{X}$ is already given as
$$
\boldsymbol{X}(\boldsymbol{\xi})=\left[\begin{array}{l}
1 \\
1
\end{array}\right]+\left[\begin{array}{l}
\xi_1 \\
\xi_2
\end{array}\right]
$$
where $\xi_1 \sim \xi_2 \sim \mathcal{U}(-1,1)$ are independent. Choose the required polynomials accordingly.

Hint: to compute expectations over $\xi_1, \xi_2$, you can use the formula
$$
\mathbb{E}\left[g\left(\xi_1, \xi_2\right)\right]=\int_{\Xi_{\xi_2}} \int_{\Xi_{\xi_1}} g\left(\xi_1, \xi_2\right) f_{\boldsymbol{\xi}}\left(\xi_1, \xi_2\right) d \xi_1 d \xi_2
$$
where $g$ is an arbitrary function.


### Solution
 For the coefficients there holds
$$
q_i=\frac{\mathbb{E}\left[M(\boldsymbol{X}(\boldsymbol{\xi})) \Phi_i(\boldsymbol{\xi})\right]}{\mathbb{E}\left[\Phi_i^2(\boldsymbol{\xi})\right]}
$$

We have, $X_1= 1 + \xi_1$, $X_2= 1 + \xi_2$ 

Inserting the expansion for $\boldsymbol{X}$ into $Y$ yields
$$
\begin{aligned}
Y & =3\left(1+\xi_1\right)+2\left(1+\xi_2\right)^2+1.5=3+3 \xi_1+2+2 \xi_2^2+4 \xi_2+1.5 \\
& =6.5+3 \xi_1+4 \xi_2+2 \xi_2^2
\end{aligned}
$$

As we have a vector of two uniformly distributed random variables, we need a linear gPC in multiple dimensions. Hence with [[250430 Askey Scheme|Legendre polynomials]]:
$$
\begin{aligned}
& \Phi_0\left(\xi_1, \xi_2\right)=L_0\left(\xi_1\right) L_0\left(\xi_2\right)=1 \\
& \Phi_1\left(\xi_1, \xi_2\right)=L_1\left(\xi_1\right) L_0\left(\xi_2\right)=\xi_1 \\
& \Phi_2\left(\xi_1, \xi_2\right)=L_0\left(\xi_1\right) L_1\left(\xi_2\right)=\xi_2 \\
\end{aligned}
$$
### Calculating Expectations for a Uniform Distribution
Given a random variable $\xi$ that is uniformly distributed on the interval $[-1, 1]$, its Probability Density Function (PDF) is:
$$f(\xi) = \frac{1}{2}, \quad \text{for } \xi \in [-1, 1]$$
The general formula for the expected value of a function $g(\xi)$ is:
$$E[g(\xi)] = \int_{-1}^{1} g(\xi)f(\xi)d\xi$$
1. **Expectation of $\xi$**
	$$
	E[\xi] = \int_{-1}^{1} \xi \cdot \frac{1}{2} \,d\xi 
	= \frac{1}{2} \left[ \frac{\xi^2}{2} \right]_{-1}^{1} = 0
	$$

2. **Expectation of $\xi^2$**
	$$
	E[\xi^2] = \int_{-1}^{1} \xi^2 \cdot \frac{1}{2} \,d\xi 
	= \frac{1}{2} \left[ \frac{\xi^3}{3} \right]_{-1}^{1} = \frac 1 3 
	$$

3. **Expectation of** $\xi^3$
	$$
	E[\xi^3] = \int_{-1}^{1} \xi^3 \cdot \frac{1}{2} \,d\xi 
	= \frac{1}{2} \left[ \frac{\xi^4}{4} \right]_{-1}^{1}  =0
	$$
and therefore
$$
\begin{gathered}
q_0=\frac{\mathbb{E}[Y * 1]}{\mathbb{E}\left[1^2\right]}=\mathbb{E}\left[6.5+3 \xi_1+4 \xi_2+2 \xi_2^2\right]=6.5+2 / 3 , \\
q_1=\frac{\mathbb{E}\left[Y * \xi_1\right]}{\mathbb{E}\left[\Phi_1^2\right]}=\frac{\mathbb{E}\left[6.5 \xi_1+3 \xi_1^2+4 \xi_2 \xi_1+2 \xi_2^2 \xi_1\right]}{\mathbb{E}\left[\xi_1^2\right]}=3  \\
q_2=\frac{\mathbb{E}\left[Y * \xi_2\right]}{\mathbb{E}\left[\Phi_2^2\right]}=\frac{\mathbb{E}\left[6.5 \xi_2+3 \xi_1 \xi_2+4 \xi_2^2+2 \xi_2^3\right]}{\mathbb{E}\left[\xi_2^2\right]}=\frac{4 / 3}{1 / 3}=4 
\end{gathered}
$$

**Note: $\mathbb E[\xi_1\cdot\xi_2]=\mathbb E[\xi_1]\mathbb E[\xi_2]=0$**