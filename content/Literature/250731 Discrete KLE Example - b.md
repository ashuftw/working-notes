---
title: Discrete KLE Example - b
draft: true
tags: 
date: 2025-07-31
---
We consider the following expansion:

$$
\mathbf{x} = \begin{bmatrix} 2 \\ 3 \end{bmatrix} + \begin{bmatrix} 1 \\ 0 \end{bmatrix} \xi_1 + \begin{bmatrix} 0 \\ 4 \end{bmatrix} \xi_2 + \begin{bmatrix} 1 \\ 0 \end{bmatrix} \left(\frac{3}{2}\xi_1^2 - \frac{1}{2}\right)
$$

where $\xi_i \sim U(-1,1)$ are independent and identically distributed (i.i.d). The goal is to compute the KLE. Therefore,

1.  Compute the expected value and the covariance matrix of the expansion.
2.  Compute the KLE by performing an eigendecomposition. If you are not sure whether your computed covariance matrix is correct, use this one to go on:
    $$
    C_X = \begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix} \quad (1)
    $$

Explain the difference between the original expansion and the KLE expansion.

**Hint**: The first three Legendre polynomials are $1, \xi, \frac{3}{2}\xi^2 - \frac{1}{2}$. Their expected values are $E[1]=1, E[\xi]=0, E[\frac{3}{2}\xi^2-\frac{1}{2}]=0$.

---

## 1. Expected Value and Covariance Matrix

First, we compute the necessary statistics of the random vector $\mathbf{x}$.

### Step 1: Define Component Equations
From the vector equation, we can write the scalar equations for $X_1$ and $X_2$:
* $X_1 = 2 + 1 \cdot \xi_1 + 1 \cdot \left(\frac{3}{2}\xi_1^2 - \frac{1}{2}\right) = \frac{3}{2}\xi_1^2 + \xi_1 + \frac{3}{2}$
* $X_2 = 3 + 4\xi_2$

### Step 2: Compute the Expected Value
The expected value $E[\mathbf{x}]$ is the vector of the individual expected values, $E[X_1]$ and $E[X_2]$. Using the hint that the Legendre polynomials have zero mean (for order > 0):
$$
E[\mathbf{x}] = E\left[ \begin{bmatrix} 2 \\ 3 \end{bmatrix} + \dots \right] = \begin{bmatrix} 2 \\ 3 \end{bmatrix}
$$
The mean is simply the zeroth-order (constant) term of the gPC expansion.

### Step 3: Compute the Variances
The variance is $V[X] = E[(X - E[X])^2]$.

* **Variance of $X_1$**:
    $$
    V[X_1] = E\left[ \left( (\frac{3}{2}\xi_1^2 + \xi_1 + \frac{3}{2}) - 2 \right)^2 \right] = E\left[ \left( \frac{3}{2}\xi_1^2 + \xi_1 - \frac{1}{2} \right)^2 \right]
    $$
    Expanding this and taking the expectation (using $E[\xi_1^n]$ rules) gives:
    $$
    V[X_1] = \frac{9}{4}E[\xi_1^4] - \frac{1}{2}E[\xi_1^2] + \frac{1}{4} = \frac{9}{4}\left(\frac{1}{5}\right) - \frac{1}{2}\left(\frac{1}{3}\right) + \frac{1}{4} = \frac{8}{15}
    $$

* **Variance of $X_2$**:
    $$
    V[X_2] = E\left[ ( (3 + 4\xi_2) - 3 )^2 \right] = E[(4\xi_2)^2] = 16E[\xi_2^2] = 16\left(\frac{1}{3}\right) = \frac{16}{3}
    $$

### Step 4: Compute the Covariance
The covariance is $\text{Cov}(X_1, X_2) = E[(X_1 - E[X_1])(X_2 - E[X_2])]$.
$$
\text{Cov}(X_1, X_2) = E\left[ \left( \frac{3}{2}\xi_1^2 + \xi_1 - \frac{1}{2} \right) (4\xi_2) \right]
$$
Because $\xi_1$ and $\xi_2$ are **independent**, we can separate the expectations:
$$
\text{Cov}(X_1, X_2) = E\left[ \frac{3}{2}\xi_1^2 + \xi_1 - \frac{1}{2} \right] \cdot E[4\xi_2] = (0) \cdot (0) = 0
$$

### Step 5: Assemble the Covariance Matrix
The covariance matrix $C_X$ is assembled from the variances and covariance:
$$
C_X = \begin{pmatrix} V[X_1] & \text{Cov}(X_1, X_2) \\ \text{Cov}(X_2, X_1) & V[X_2] \end{pmatrix} = \begin{pmatrix} \frac{8}{15} & 0 \\ 0 & \frac{16}{3} \end{pmatrix}
$$

---

## 2. Karhunen-Loeve Expansion (KLE)

The KLE represents the vector $\mathbf{x}$ using the eigenvalues and eigenvectors of its covariance matrix.

### Step 1: Eigendecomposition of the Covariance Matrix
Since $C_X$ is a **diagonal matrix**, its eigenvalues and eigenvectors are easy to find:
* **Eigenvalues ($\lambda_i$)**: The diagonal entries.
    * $\lambda_1 = \frac{8}{15}$
    * $\lambda_2 = \frac{16}{3}$
* **Eigenvectors ($\mathbf{\phi}_i$)**: The standard basis vectors.
    * $\mathbf{\phi}_1 = \begin{bmatrix} 1 \\ 0 \end{bmatrix}$
    * $\mathbf{\phi}_2 = \begin{bmatrix} 0 \\ 1 \end{bmatrix}$

### Step 2: Formulate the KLE
The general form of the KLE is $\mathbf{x} = \mathbf{\mu} + \sum_i \sqrt{\lambda_i}\mathbf{\phi}_i \eta_i$, where $\eta_i$ are new uncorrelated random variables with zero mean and unit variance.

Substituting our values:
$$
\mathbf{x} = \begin{bmatrix} 2 \\ 3 \end{bmatrix} + \sqrt{\frac{8}{15}}\begin{bmatrix} 1 \\ 0 \end{bmatrix} \eta_1 + \sqrt{\frac{16}{3}}\begin{bmatrix} 0 \\ 1 \end{bmatrix} \eta_2
$$
$$
\mathbf{x} = \begin{bmatrix} 2 + \sqrt{\frac{8}{15}}\eta_1 \\ 3 + \frac{4}{\sqrt{3}}\eta_2 \end{bmatrix}
$$
This is the final Karhunen-Loeve Expansion.

---

##  3. Difference Between the gPC and KLE Expansions

* **Linearity**: The original gPC expansion was **nonlinear** because it contained a $\xi_1^2$ term. The final KLE is, by definition, **linear** in its new random variables, $\eta_1$ and $\eta_2$.

* **Random Variables**: The gPC expansion was built on **independent** random variables ($\xi_1, \xi_2$). The KLE produces new random variables ($\eta_1, \eta_2$) that are guaranteed to be **uncorrelated**, which is a weaker statistical condition than full independence.