---
title: Question B - KLE
draft: true
tags:
date: 2025-08-26
---
A random process is described by a random vector $X = (X_1, X_2, X_3)^T$. The components are given as:
- $X_1 \sim N(1, 2)$
- $X_2 \sim N(2, 3)$
- $X_3 \sim N(2, 3)$

The variables $X_2$ and $X_3$ are correlated with $\operatorname{Cov}(X_2, X_3) = a \neq 0$, while $X_1$ is uncorrelated with $X_2$ and $X_3$. $\mathbb E[X_1, X_i], \, i\in 2,3$

The goal is to describe the input vector using the Karhunen-Loève Expansion (KLE).

#### (a) Covariance Matrix
**Write the covariance matrix $C_X$. What properties does this matrix have, and what do you know *a priori* about its eigenvalues and eigenvectors?**

Based on the problem statement, the covariance matrix $C_{ij} = Cov(X_i, X_j)$ should be:
 $$
 C_X = \begin{pmatrix} 4 & 0 & 0 \\ 0 & 9 & a \\ 0 & a & 9 \end{pmatrix}
 $$


**Properties of $C_X$:**
- **Symmetric**: $C_X = C_X^T$, because $Cov(X_i, X_j) = Cov(X_j, X_i)$.
- **Positive Semidefinite**: For any vector $z$, the quadratic form $z^T C_X z \ge 0$.

**A Priori Knowledge:**
- The eigenvalues are **real and non-negative** ($\lambda_i \ge 0$).
- Eigenvectors from distinct eigenvalues are **mutually orthogonal**.

---

#### (b) Karhunen-Loève Expansion
The KLE can be written in the form $X(\theta) = \mu + A \xi(\theta)$. Express the complete KLE for the vector $X$.

We find the eigenvalues and eigenvectors of $C_X$. Due to its block-diagonal structure:
- **1st Eigenvalue/Eigenvector:** $\lambda_0 = 4$ with $v_0 = \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$
- **2nd & 3rd Eigenvalues/Eigenvectors:** From the $\begin{pmatrix} 9 & a \\ a & 9 \end{pmatrix}$ block, we get:
    - $\lambda_1 = 9+a$ with $v_1 = \begin{pmatrix} 0 \\ 1/\sqrt{2} \\ 1/\sqrt{2} \end{pmatrix}$
    - $\lambda_2 = 9-a$ with $v_2 = \begin{pmatrix} 0 \\ 1/\sqrt{2} \\ -1/\sqrt{2} \end{pmatrix}$

With the mean vector $\mu = (1, 2, 2)^T$, the KLE 
$$
X = \mu + \sum \sqrt{\lambda_i} v_i \xi_i
$$
We have
$$
X(\theta) = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} + \sqrt{4} \begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix} \xi_0(\theta) + \sqrt{9+a} \begin{pmatrix} 0 \\ 1/\sqrt{2} \\ 1/\sqrt{2} \end{pmatrix} \xi_1(\theta) + \sqrt{9-a} \begin{pmatrix} 0 \\ 1/\sqrt{2} \\ -1/\sqrt{2} \end{pmatrix} \xi_2(\theta)
$$
In matrix form $X = \mu + A\xi$:
$$
X(\theta) = \begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix} + \begin{pmatrix} 2 & 0 & 0 \\ 0 & \frac{\sqrt{9+a}}{\sqrt{2}} & \frac{\sqrt{9-a}}{\sqrt{2}} \\ 0 & \frac{\sqrt{9+a}}{\sqrt{2}} & -\frac{\sqrt{9-a}}{\sqrt{2}} \end{pmatrix} \begin{pmatrix} \xi_0(\theta) \\ \xi_1(\theta) \\ \xi_2(\theta) \end{pmatrix}
$$

---
#### (c) Optimal Truncation
**Determine the integer value of the parameter $a \in \{0, 1, \dots, 8\}$ such that:**
1.  **The properties of a covariance matrix are preserved.**
2.  **A truncated KLE, reduced to only two random variables, achieves the best possible approximation of the original vector $X$.**

**Justify your choice of $a$.**

We need to find the best $a \in \{0, 1, \dots, 8\}$.

1.  **Preserve Covariance Properties**: Eigenvalues must be non-negative. The only critical condition is $\lambda_2 = 9-a \ge 0 \implies a \le 9$, which is satisfied for the given range of $a$.

2.  **Achieve Best Approximation**: The **best approximation** retains the two largest eigenvalues. We need to choose $a$ to maximize their sum (the captured variance). The eigenvalues are $\lambda_0 = 4$, $\lambda_1 = 9+a$, and $\lambda_2 = 9-a$.
    - $\lambda_1$ is always the largest. We compare $\lambda_0$ and $\lambda_2$.

    - **Case 1: $a \le 5$**
        - Here, $9-a \ge 4 \implies \lambda_2 \ge \lambda_0$.
        - The two largest eigenvalues are $\lambda_1$ and $\lambda_2$.
        - Captured Variance: $V_{cap} = \lambda_1 + \lambda_2 = (9+a) + (9-a) = 18$.

    - **Case 2: $a > 5$**
        - Here, $9-a < 4 \implies \lambda_0 > \lambda_2$.
        - The two largest eigenvalues are $\lambda_1$ and $\lambda_0$.
        - Captured Variance: $V_{cap} = \lambda_1 + \lambda_0 = (9+a) + 4 = 13+a$.
            - If $a=6, V_{cap} = 19$.
            - If $a=7, V_{cap} = 20$.
            - If $a=8, V_{cap} = 21$.

Comparing the cases, the maximum captured variance is **21**, achieved when **$a=8$**. 

---
#### (d) Mean Squared Error
**Using the optimal value of $a$ found in part (c), what is the Mean Squared Error (MSE), $E[\|X - X_{truncated}\|^2]$, of the resulting two-term approximation?**

The MSE of the truncation is the sum of the discarded eigenvalues. For our optimal choice of $a=8$, the eigenvalues are:
- $\lambda_1 = 9+8 = 17$ (Kept)
- $\lambda_0 = 4$ (Kept)
- $\lambda_2 = 9-8 = 1$ (**Discarded**)

The MSE is the value of the discarded eigenvalue.
$$
MSE = \lambda_2 = 1
$$

---