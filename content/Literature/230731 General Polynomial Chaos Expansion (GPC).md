---
title: General Polynomial Chaos Expansion
draft: false
date: 2023-07-31
---
## Definition

It is a way to express Random Variables as a linear expansion using [[250429 Orthogonality|Orthogonal]] polynomials of simpler random variables (called the *germ*)

## Formula

Let $X$ be a random variable with arbitrary $\operatorname{PDF} f_X$, for which the mean value and variance exist $(\mathbb{E}[X], \mathbb{V}[X]<\infty)$. 
Using the generalized Polynomial Chaos (gPC) Expansion
$$
X(\theta)=\sum_{i=0}^{\infty} q_i \Phi_i(\xi(\theta))
$$

$$
\boxed{X=\sum_{i=0}^{\infty} q_i \Phi_i(\xi)}
$$



Where, 
- $q_i$ are deterministic coefficients (also called PC coefficients). They encode important information about distribution and act as weights. 
- $\Phi_i$ are Orthogonal Polynomials (e.g.**Hermite polynomials**)
- $\xi \sim \mathcal{N}(0,1)$ is the germ  
- Each $\xi$ term is called a germ.
- The Polynomials are orthogonal to the the germ. 

**Note:** The choice of the Orthogonal Polynomials ($\Phi_i$), depends on the distribution of the germ $\xi$. According to the [[250430 Askey Scheme|Askey Scheme]]

## Example

Random Variable



$$
X \sim \mathcal{N}(2,1)
$$



Polynomial Chaos expansion



$$
X=2+\xi
$$



 Where,  $\xi \sim \mathcal{N}(0,1)$
 
![[../Files/Pasted image 20240605153508.png|center|400]]

