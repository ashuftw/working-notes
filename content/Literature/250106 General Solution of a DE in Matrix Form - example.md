---
title: General Solution of a DE in Matrix Form - example
draft: false
tags: 
date: 2025-02-06
---

# Determine the Real General Solution

We are given the system of differential equations:

$$
\mathbf{q}' = \begin{bmatrix} 0 & 1 \\ -4 & 0 \end{bmatrix} \mathbf{q} + \begin{bmatrix} 0 \\ 1 \end{bmatrix}
$$

## Step 1: Solve the Homogeneous System

The homogeneous part is:

$$
\mathbf{q}' = A\mathbf{q}, \quad \text{where } A = \begin{bmatrix} 0 & 1 \\ -4 & 0 \end{bmatrix}
$$

### Finding Eigenvalues:

The characteristic equation is:

$$
\det(A - \lambda I) = \begin{vmatrix} -\lambda & 1 \\ -4 & -\lambda \end{vmatrix} = (-\lambda)(-\lambda) - (1)(-4) = \lambda^2 + 4 = 0
$$

Solving for $\lambda$:

$$
\lambda_{1,2} = \pm 2i
$$

### Finding Eigenvectors:

For $\lambda = 2i$:

$$
(A - 2iI) \mathbf{v} = 0
$$

$$
\begin{bmatrix} -2i & 1 \\ -4 & -2i \end{bmatrix} \begin{bmatrix} v_1 \\ v_2 \end{bmatrix} = \begin{bmatrix} 0 \\ 0 \end{bmatrix}
$$

Solving:

$$
-2i v_1 + v_2 = 0 \quad \Rightarrow \quad v_2 = 2i v_1
$$

Choosing $v_1 = 1$, we get:

$$
\mathbf{v}_1 = \begin{bmatrix} 1 \\ 2i \end{bmatrix}
$$

> Note: we have flexibility in choosing $v_1$ because eigenvectors are not unique - they can be scaled by any non-zero constant and still remain eigenvectors.

For $\lambda = -2i$, the eigenvector is:

$$
\mathbf{v}_2 = \begin{bmatrix} 1 \\ -2i \end{bmatrix}
$$

### Constructing the General Homogeneous Solution:

Using Euler's formula $e^{2it} = \cos(2t) + i\sin(2t)$, we get:

$$
\mathbf{q}_h(t) = c_1 \begin{bmatrix} \cos(2t) \\ -2\sin(2t) \end{bmatrix} + c_2 \begin{bmatrix} \sin(2t) \\ 2\cos(2t) \end{bmatrix}
$$

where $c_1, c_2$ are real constants.

---

## Step 2: Find a Particular Solution

Since the inhomogeneous term is constant, assume a constant solution:

$$
\mathbf{q}_p = \begin{bmatrix} a \\ b \end{bmatrix}
$$

Substituting into the equation:

$$
\begin{bmatrix} 0 & 1 \\ -4 & 0 \end{bmatrix} \begin{bmatrix} a \\ b \end{bmatrix} + \begin{bmatrix} 0 \\ 1 \end{bmatrix} = \mathbf{0}
$$

> Note: If $\mathbf q$ is constant $\mathbf q'$ is $0$

This gives:

$$
\begin{cases}
a + 0 = 0 \quad \Rightarrow \quad a = 0 \\
-4a + 0 + 1 = 0 \quad \Rightarrow \quad b = -\frac{1}{4}
\end{cases}
$$

Thus, the particular solution is:

$$
\mathbf{q}_p = \begin{bmatrix} 0 \\ -\frac{1}{4} \end{bmatrix}
$$

---

## Step 3: General Solution

$$
\mathbf{q}(t) = c_1 \begin{bmatrix} \cos(2t) \\ -2\sin(2t) \end{bmatrix} + c_2 \begin{bmatrix} \sin(2t) \\ 2\cos(2t) \end{bmatrix} + \begin{bmatrix} 0 \\ -\frac{1}{4} \end{bmatrix}
$$

where $c_1, c_2$ are arbitrary real constants.

---
