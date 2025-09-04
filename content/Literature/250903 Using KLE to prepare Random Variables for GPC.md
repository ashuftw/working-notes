---
title: Using KLE to prepare Random Variables for GPC
draft: false
tags:
date: 2025-09-03
---
### Problem: A Model with Correlated Inputs 

Let's imagine you have a simple engineering model that takes two uncertain inputs, $X_1$ and $X_2$.

$$
Y = \mathcal{M}(X_1, X_2) = X_1^2 + X_2
$$

Now, suppose your experimental data tells you that $X_1$ and $X_2$ are **correlated**. For instance, they might both be related to the ambient temperature. We can describe this relationship using a **covariance matrix**.

Let's say the inputs are Gaussian random variables with a mean of zero and the following covariance matrix $C_X$:

$$
C_X = \begin{pmatrix} 1.0 & 0.8 \\ 0.8 & 1.0 \end{pmatrix}
$$

The non-zero off-diagonal terms (0.8) indicate a strong positive correlation between $X_1$ and $X_2$.

> [!info] PCE Challenge
> You want to build a PCE for $Y$, but the standard method requires the inputs to be **independent**. You can't just create a basis by multiplying 1D Hermite polynomials for $X_1$ and $X_2$ because their correlation complicates their joint probability distribution.

***

### Solution: Applying the KL Expansion 

The KL expansion transforms our correlated vector $X = (X_1, X_2)^T$ into a new vector $\xi = (\xi_1, \xi_2)^T$ whose components are **uncorrelated** standard normal random variables.

The transformation is given by the formula from the notes:

$$
X = \mu_X + L\xi
$$

Since our mean $\mu_X$ is zero, this simplifies to $X = L\xi$. The matrix $L$ is calculated from the eigenvalues and eigenvectors of the covariance matrix $C_X$.

1.  **Eigendecomposition of $C_X$**: We find the eigenvalues ($\lambda_1, \lambda_2$) and eigenvectors ($v_1, v_2$) of our covariance matrix. For the matrix above, this gives:
    * $\lambda_1 = 1.8$, $\lambda_2 = 0.2$
    * $v_1 = \begin{pmatrix} 0.707 \\ 0.707 \end{pmatrix}$, $v_2 = \begin{pmatrix} -0.707 \\ 0.707 \end{pmatrix}$

2.  **Construct the Transformation**: We use these to build the $L$ matrix and find the relationship between $X$ and $\xi$:

	$$
	\begin{pmatrix} X_1 \\ X_2 \end{pmatrix} = L \begin{pmatrix} \xi_1 \\ \xi_2 \end{pmatrix} = \begin{pmatrix} 0.949 & -0.316 \\ 0.949 & 0.316 \end{pmatrix} \begin{pmatrix} \xi_1 \\ \xi_2 \end{pmatrix}
	$$

    This gives us our original variables as a function of the new, uncorrelated ones:

	$$
	X_1 = 0.949\xi_1 - 0.316\xi_2
	$$


	$$
	X_2 = 0.949\xi_1 + 0.316\xi_2
	$$


***

### Build PCE with the new random variables

Now we have a new set of variables, $\xi_1$ and $\xi_2$, which are **independent** and follow a standard normal distribution. We can substitute their expressions back into our original model:

$$
Y = (0.949\xi_1 - 0.316\xi_2)^2 + (0.949\xi_1 + 0.316\xi_2)
$$

This defines a new, equivalent model $\hat{\mathcal{M}}(\xi_1, \xi_2)$ that is a function of independent variables.

**Now, building the PCE is simple:**
Because $\xi_1$ and $\xi_2$ are independent normal variables, we can use a standard PCE basis built from products of 1D **Hermite polynomials** ($H$):

$$
Y \approx \sum_{i=0}^{p} \sum_{j=0}^{p} q_{ij} H_i(\xi_1) H_j(\xi_2)
$$

The coefficients $q_{ij}$ can now be calculated easily using standard methods like [[250729 Quadrature to Approximate Expected Value|quadrature]] or [[240723 non-Intrusive Projection|non-Intrusive Projection]] that work perfectly for independent variables.

The KL expansion served as the essential data preprocessing step that "unlocked" the problem, allowing us to use the powerful and efficient machinery of Polynomial Chaos Expansion.