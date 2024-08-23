Status: #finished 
## Interpolation Error at a point $\xi$
$$
\boxed{
r(x) = -\frac{w(x)}{(N+1)!} f^{(N+1)}(\xi(x^*))
}
$$

Where,
- **Error:** $r(x) = p(x) - f(x)$
- **Newton Polynomial:** $w(x) = \prod_{i=0}^N (x - x_i)$
- **Order of Polynomial** -> $N$  
- **Number of points** -> $N+1$
- $f^{(N+1)}(\xi(x^*))$ -> Derivative of function $f$ at point $\xi$ in the domain. 
## Maximum Interpolation error
$$
|r(x)| \leq \frac{|\omega(x)|}{(N+1) !} \cdot M_{N+1} \quad \text { with } \quad M_{N+1}=\max _{x \in[a, b]}\left|f^{(N+1)}(x)\right| .
$$

In general, this estimation of $|r(x)|$ does not get better with increasing $N$.

## Solution Method
![[230720 Solution method to find Interpolation Error.png]]
	
	




---
# References
