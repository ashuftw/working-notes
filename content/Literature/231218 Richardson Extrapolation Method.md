Status: #finished 
## Use case
It is an Error correction technique that improves the result of the an Integration by improving the integral itself. (As opposed to doing so through iterations)

## Derivation 
An integral $I$ can be written as

$$
I=I(h)+E(h)
$$

Where $I(h)=$ Numerical approximation, $E(h)=$ the truncation error. 

Suppose we make to estimates step sizes $h_1$ and $h_2$ and we get the same values for the error. 

$$
I\left(h_1\right)+E\left(h_1\right)=I\left(h_2\right)+E\left(h_2\right)\tag{2}
$$

For the Trapezoid Rule, the error is $E \cong-\frac{b-a}{12} h^2 \bar{f}^{\prime \prime}$

Assume $f''$ is constant regardless of step size. Then the ratio of the errors is given by. 
$$
E\left(h_1\right) \cong E\left(h_2\right)\left(\frac{h_1}{h_2}\right)^2
$$
Substitution in eqn. $(2)$ 




