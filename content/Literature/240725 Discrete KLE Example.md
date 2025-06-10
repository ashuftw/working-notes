---
title: Discrete KLE Example
draft: false
date: 2024-07-25
---
Given are two random variables $X_1 \sim \mathcal{N}(2,0.5)$ and $X_2 \sim \mathcal{N}(3,1.5)$. They can be represented as a vector $\binom{X_1}{X_2}$. There holds $\mathbb{E}\left[X_1 X_2\right]=6$.
Using the KL expansion, find $\binom{X_1}{X_2}=f\binom{\xi_1}{\xi_2}$ with $\xi_1, \xi_2 \sim \mathcal{N}(0,1)$.

## Solution

### Step 1: Find Mean & covariance

$$
\operatorname{Cov}[X]=\left[\begin{array}{ll}
\operatorname{Var}\left[X_1\right] & \operatorname{Cov}\left[X_1, X_2\right] \\
\operatorname{Cov}\left[X_2, X_1\right] & \operatorname{Var}\left[X_2\right]
\end{array}\right]
$$

$$
\operatorname{Cov}\left[X_1, X_2\right]=E\left[X_1 X_2\right]-E\left[X_1\right] E\left[X_2\right]=6-2 \cdot 3=0
$$

So the covariance matrix becomes:

$$C_X=\left(\begin{array}{cc}0.5 & 0 \\ 0 & 1.5\end{array}\right)$$

### Step 2: Find Eigenvalues and Eigenvectors

Since $C_X$ is already diagonal (uncorrelated random variables), the eigenvalues are simply the diagonal elements. Ordered from largest to smallest (important!):
- $\lambda_1=1.5$
- $\lambda_2=0.5$

The eigenvectors are:
- $v_1=\binom{0}{1}$ (corresponding to $\lambda_1=1.5$ )
- $v_2=\binom{1}{0}$ (corresponding to $\lambda_2=0.5$ )

So, $V=\left(\begin{array}{ll}0 & 1 \\ 1 & 0\end{array}\right)$ and $E=\left(\begin{array}{cc}1.5 & 0 \\ 0 & 0.5\end{array}\right)$

### Step 3: Construct the KL expansion

The KL expansion is given by:

$$
X=\mu_X+V E^{1 / 2} \xi
$$

where, $E^{1 / 2}=\left[\begin{array}{cc} \sqrt{1.5} & 0 \\ 0 & \sqrt{0.5} \end{array}\right]$

Therefore:

$$
\left[\begin{array}{l}
X_1 \\
X_2
\end{array}\right]=\left[\begin{array}{l}
2 \\
3
\end{array}\right]+\left[\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right]\left[\begin{array}{cc}
\sqrt{1.5} & 0 \\
0 & \sqrt{0.5}
\end{array}\right]\left[\begin{array}{l}
\xi_1 \\
\xi_2
\end{array}\right]
$$

Simplifying:

$$
\begin{aligned}
& {\left[\begin{array}{l}
X_1 \\
X_2
\end{array}\right]=\left[\begin{array}{l}
2 \\
3
\end{array}\right]+\left[\begin{array}{cc}
0 & \sqrt{0.5} \\
\sqrt{1.5} & 0
\end{array}\right]\left[\begin{array}{l}
\xi_1 \\
\xi_2
\end{array}\right]} \\
& {\left[\begin{array}{l}
X_1 \\
X_2
\end{array}\right]=\left[\begin{array}{l}
2 \\
3
\end{array}\right]+\left[\begin{array}{l}
\sqrt{0.5} \xi_2 \\
\sqrt{1.5} \xi_1
\end{array}\right]}
\end{aligned}
$$

### Final KL expansion is:

$$
\boxed{X_1=2+\sqrt{0.5}\xi_2}\ \quad \& \quad \boxed{X_2=3+\sqrt{1.5} \xi_1}
$$

Where $\xi_1$ and $\xi_2$ are independent standard normal random variables, i.e., $\xi_1, \xi_2 \sim \mathcal{N}(0,1)$.
