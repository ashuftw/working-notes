  
## Definition
Laplace Transformation is an Integral Transformation which transforms a function of the time domain $f(t)$ into a function of the Laplace Frequency to give $F(s)$.

$$
\boxed{
\mathcal{L}\{f(t)\}=\int_0^{\infty} f(t) e^{-s t} d t=F(s)
}
$$

where, $t\rightarrow$ Time domain, $f(t)\rightarrow$ Generalized frequency and $s\rightarrow$ Laplace Frequency domain. 
## Use case
The Laplace Transform is used to solve a particularly hairy Differential Equation. It transforms the D.E into an Algebraic equation in terms of a complex variable $s$. Once the variable is solved for $s$, an Inverse Laplace Transform can be applied to get the solution for $f(t)$.






