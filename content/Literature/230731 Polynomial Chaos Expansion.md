  
## Definition
It is a way to represent Random Variables with a *general probability distribution* through polynomials over random variables with well known distributions like Gaussian, Uniform etc. 

Let $X$ be a random variable with arbitrary $\operatorname{PDF} f_X$, for which the mean value and variance exist $(\mathbb{E}[X], \mathbb{V}[X]<\infty)$. 
Using the PC Expansion

$$
X(\theta)=\sum_{i=0}^{\infty} q_i \Phi_i(\xi(\theta))
$$


$$
\boxed{X=\sum_{i=0}^{\infty} q_i \Phi_i(\xi)}
$$


where, 
- $\xi \sim \mathcal{N}(0,1)$ 
- $\Phi_i\rightarrow$  **Hermite polynomials**.

| Hermit Polynomial  | Value                |
| ------------------ | -------------------- |
| $H_0(\xi)$         | 1                    |
| $H_1(\xi)$         | $\xi$                |
| $H_2(\xi)$         | $\xi^2 - 1$          |
| $H_3(\xi)$         | $\xi^3 - 3\xi$       |
| $H_4(\xi)$         | $\xi^4 - 6\xi^2 + 3$ |
| ...                | ...                  |



**Note** 
- Each $\xi$ term is called a germ.
- The Hermite Polynomials are orthogonal to the the germ. 


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
![[Pasted image 20240605153508.png]]




