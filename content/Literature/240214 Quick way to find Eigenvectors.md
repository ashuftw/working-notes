---
title: Quick way to find Eigenvectors
draft: false
tags: 
date: 2025-07-15
---

## Method

Once we have the eigenvalues of a given matrix, find the eigenvectors by solving:

$$
(\boldsymbol A-\lambda \boldsymbol{I}) {\boldsymbol{v}}=0
$$

The eigen vector can be found out by solving the matrix system. 

#### **Shortcut** 

If $(A - \lambda I) = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$, then $v = \begin{pmatrix} -b \\ a \end{pmatrix}$

## Example

- For $\lambda_1 = 2 + \sqrt{5}$
	Solve $(A - \lambda_1 I)v = 0$:



	$$
	\begin{pmatrix} 3-(2+\sqrt{5}) & 1 \\ 4 & 1-(2+\sqrt{5}) \end{pmatrix} = \begin{pmatrix} 1-\sqrt{5} & 1 \\ 4 & -1-\sqrt{5} \end{pmatrix}
	$$





	$$
	\boxed{v_1 = \begin{pmatrix} -1 \\ 1-\sqrt{5} \end{pmatrix}}
	$$


- For $\lambda_2 = 2 - \sqrt{5}$



	$$
	(A - \lambda_2 I) = \begin{pmatrix} 1+\sqrt{5} & 1 \\ 4 & -1+\sqrt{5} \end{pmatrix}
	$$




	$$
	\boxed{v_2 = \begin{pmatrix} -1 \\ 1+\sqrt{5} \end{pmatrix}}
	$$


