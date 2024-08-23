Status: #finished 
### [[240214 General Solution of the for a Differential Equation in Matrix Form|Homogeneous Solution]]
$$q_h(t)=V D(t) c$$
### Particular Solution
$$q_p(t)=V D(t) c(t)$$

$$\begin{aligned} q'_p(t)&= V D'(t) c(t)+V D(t) c'(t)\\
&=V \Lambda D'(t) c(t)+V D(t) c'(t)\end{aligned}$$
> Note: *$D(t)$ is a diagonal matrix with entries $e^{\lambda_1 t}, e^{\lambda_2 t}, \ldots, e^{\lambda_n t}$ . Through differentiation $\lambda$ gets multiplied for each element. It can be conveniently represented by $\Lambda$ where each diagonal element is an eigen value.*

Similar to the [[221120 Solution method for Variation of Constants|1-D case]], 
$$q'_p(t)-V \Lambda D'(t) c(t)=V D(t) c'(t)$$
$$
\Rightarrow V D(t) c'(t) = P(t)
$$
Integrate each element of to get $c(t)$
### Solution 
$$q = q_h + q_p$$


---
# References
