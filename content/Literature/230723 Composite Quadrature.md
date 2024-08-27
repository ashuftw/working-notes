Status: #finished
It is a [[230507 Quadrature|Quadrature]] where the domain $x\in[a,b]$ is split into multiple grid points $i=0,1,2\dots N$ with $a = x_0 < x_1 < \dots < x_N = b$

$$
\boxed{
\int_a^b f(x) \mathrm{d} x=\sum_{i=0}^{N-1} \int_{x_i}^{x_{i+1}} f(x)\ \mathrm{d}x
}
$$

We sum only till $(N-1)$ because $i=N$ is the end point and $x_{N+1}$ doesn't exist.  
## Example 
| Quadrature rule | Composite Quadrature | Fixed Step |
| -------- |  --------- |------- |
| Left Rectangle| $\sum_{i=0}^{N-1}f\left(x_i\right)\left(x_{i+1}-x_i\right)$|$h\sum_{j=0}^{J-1}f\left(x_j\right)$       |
|||
| Midpoint  |  $\sum_{j=0}^{J-1}f\left(\frac{x_{j+1}+x_j}{2}\right)\left(x_{j+1}-x_j\right)$ |$h \sum_{j=0}^{J-1} f\left(\frac{x_{j+1}+x_j}{2}\right)$        |
|||
|Trapezoid| $\sum_{j=0}^{J-1}\left(x_{j+1}-x_j\right) \frac{f\left(x_j\right)+f\left(x_{j+1}\right)}{2}$  | $\frac{h}{2} \sum_{j=0}^{J-1}\left(f\left(x_j\right)+f\left(x_{j+1}\right)\right)$|
|Simpson's|| $\frac{h}{6} \sum_{j=0}^{J-1}\left(f\left(x_j\right)+4 f\left(\frac{x_j+x_{j+1}}{2}\right)+f\left(x_{j+1}\right)\right)$|

