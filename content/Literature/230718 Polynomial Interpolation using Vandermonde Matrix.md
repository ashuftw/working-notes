  
For a system of $N+1$ points, the order is $N$

The following ansatz is said to be true

$$
y_i=\alpha_0+ \alpha_1 x_i \cdots \alpha_{N-1} x_i^{N-1} +  \alpha_N x_i^N, \quad i=0, \ldots, N
$$

> Eg. when $N=1$, $y_i=\alpha_1\ x_i+\alpha_0$
> 

In Matrix form

$$
\left(\begin{array}{c}
y_0 \\
y_1 \\
\vdots \\
y_N
\end{array}\right)=\underbrace{
\left(\begin{array}{ccccc}
1 & x_0 & x_0^2 & \cdots & x_0^N \\
1 & x_1 & x_1^2 & \cdots & x_1^N \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
1 & x_N & x_N^2 & \cdots & x_N^N
\end{array}\right)}_\text{Vandermond Matrix}\left(\begin{array}{c}
\alpha_0 \\
\alpha_1 \\
\vdots \\
\alpha_N
\end{array}\right)
$$

The Interpolation polynomial is then given by 

$$
p(x)=\alpha_0+\alpha_1 x+\cdots +\alpha_{N-1} x^{N-1}+\alpha_N x^N
$$

> Note: $i$ represents each point, it's much simpler to write it as a function (implicitly)






