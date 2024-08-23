Status: #finished 

The Moment Generating function is a Mathematical tool that can establish a relation between the Moment and the PDF of a Random variable. 

**Mathematically** $$\begin{aligned}
M_X(t)&=\mathbb  E[e^{tX}]
\\
&= \mathbb E\left[1+t X^1+\frac{t^2}{2 !} X^2+\frac{t^3}{3 !} X^3...\right]
\\ 
&= 1+t \mathbb E^1[X]+\frac{t^2}{2 !} \mathbb E^2[X]+\frac{t^3}{3 !} \mathbb E^3[X]
\end{aligned}$$
$$\boxed{M_X(t)=1+t \mathbb{M}^1[X]+\frac{t^2}{2 !} \mathbb{M}^2[X]+\frac{t^3}{3 !} \mathbb{M}^3[X]}$$
**Note**: If all the moments of a Random variable is known, then the PDF of a Random variable can be calculated using the moment generating function. However the relation is complicated, hence omitted here. 





---
# References
