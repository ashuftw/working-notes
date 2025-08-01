---
title: Shortcuts for finding Eigenvalues & Eigenvectors
draft: false
tags: 
date: 2025-07-15
---
### 1. **Special Matrix Types**

**Diagonal Matrix** 
$$
\begin{pmatrix} a & 0 \\ 0 & b \end{pmatrix}
$$

- Eigenvalues: $\lambda_1 = a$, $\lambda_2 = b$ (just read off diagonal)
- Eigenvectors: $v_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$, $v_2 = \begin{pmatrix}0 \\ 1 \end{pmatrix}$ 

**Upper/Lower Triangular** 
$$
\begin{pmatrix} a & b \\ 0 & c \end{pmatrix}
$$


- Eigenvalues: $\lambda_1 = a$, $\lambda_2 = c$ (diagonal entries)

### 2. **2×2 Matrix Quick Formula**

For any 
$$
\begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$


- $\lambda_{1,2} = \frac{\text{trace}}{2} \pm \sqrt{\left(\frac{\text{trace}}{2}\right)^2 - \det}$
- Where trace = $a + d$ and det = $ad - bc$

### 3. **Symmetric Matrix Properties**

- All eigenvalues are **real**
- Eigenvectors are **orthogonal**
- For $\begin{pmatrix} a & b \\ b & c \end{pmatrix}$, if $b = 0$ → already diagonal!

### 4. **Common Exam Patterns**

**Pattern 1:** 
$$
\begin{pmatrix} a & a \\ a & a \end{pmatrix}
$$


- $\lambda_1 = 2a$, $\lambda_2 = 0$
- $v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $v_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

**Pattern 2:** 
$$
\begin{pmatrix} a & b \\ b & a \end{pmatrix}
$$


- $\lambda_1 = a + b$, $\lambda_2 = a - b$
- $v_1 = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$, $v_2 = \begin{pmatrix} 1 \\ -1 \end{pmatrix}$

### 5. **Eigenvector Shortcuts**

For $2\times2$, once you have $\lambda$:

- Pick any row of $(A - \lambda I)$
- If row is $[p \quad q]$, then eigenvector is $\begin{pmatrix} q \ -p \end{pmatrix}$
- Example: If row is $[3 \quad 2]$, then $v = \begin{pmatrix} 2 \ -3 \end{pmatrix}$

### 6. **Quick Checks**

- Sum of eigenvalues = trace (sum of diagonal)
- Product of eigenvalues = determinant
- For covariance matrices: all eigenvalues ≥ 0

### 7. **KL Expansion Specific**

- Always order eigenvalues **largest to smallest**
- If $C_X$ is diagonal → eigenvectors are standard basis vectors
- For uncorrelated variables (off-diagonal $= 0$), KL expansion is trivial