## Question A 
1. **Name at least 3 properties of a CDF**

	$$
	F_X(x),\, F:\mathbb R\rightarrow [0,1]
	$$


- $F$ is right continuous 
- $F$ is non-decreasing
- $\lim_{x\to-\infty}F_X(x)=0$
---

2. **Compute $P(a\le X \le b)$ , $a<b$ and $a,b\in R$ with given CDF and PDF** 

- $P(a\le X\le e) = F_X(b)-F_X(a)$ 
- $P(a\le X\le e) = \int_a^b f_X(x)\, dx$
---
3. **When representing a non-normally distributed random vector with the KLE or the gPC expansion, what is the advantage of using a gPC expansion.** 

---
4. **Why are the formulas for Mean and Variance from FOSM just approximations.**

	The output model is approximated only with the first order Taylor Approximation
---
5. **How does the curse of dimensionality affect the gPC method, if you use the non-intrusive projection method for gPC. Write down the equation of projection**


- The gPC coefficients are obtained via $q_i=\frac{\mathbb{E}\left[\mathcal{M}(\cdot) \Phi_i(\cdot)\right]}{\mathbb{E}\left[\Phi_i(\cdot)^2\right]}$
- To calculate the numerator and denominator we use a quadrature method, which lacks the curse of dimensionality. 
- Number of nodes is typically chosen such that the polynomial in the denominator could be calculated exactly. 
---
6. **What does the accuracy of (non-Intrusive projection) gPC depend on? Name at least two properties** 	

- Polynomial Degree. 
- Degree of the chosen quadrature rule. 

