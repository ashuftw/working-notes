Status: #finished 

**Lemma**: An $\text n^\text{th}$ order differential equation written in explicit form can be written as a system of $\text n$ first order differential equations.
**Proof**
	We have
	$$y^{(n)}=f(t, y, y\prime, y\prime\prime..., y^{(n-1)})$$
	Defining function $q$ such that 
	$$\begin{aligned}
	y &= q_0 \\
	q_0\prime &=q_1 = y\prime \\
	&.\\
	&.\\
	&.\\
	q\prime_{(n-2)}&=q_{(n-1)}\\
	q\prime_{(n-1)}&=q_n=f(t, q_0,q_1,...q_{n-1})
	\end{aligned}$$
This is useful because computers are good at solving first order systems of equations.[^1]

---
# References
[^1]: [4.1 Reducing a higher order DE to a system | DarrenOng](https://www.youtube.com/watch?v=K_Oa-tY2dWw)1
