  
## Intuition 
The [[240417 Fourier Transform|Fourier Transform]],  $\mathcal F\{f(t)\cdot g(t)\} \ne \mathcal F\{f(t)\}\cdot \mathcal F\{g(t)\}$ . Instead it is given by the convolution operation "$*$"
## Mathematically 
$\mathcal{F}\{f(t)\}=F(\omega)$ and $\mathcal{F}\{g(t)\}=G(\omega)$, then 

$$
\mathcal{F}\{f(t) \cdot g(t)\}=(F * G)(\omega)
$$

The convolution of $F(\omega)$ and $G(\omega)$ is defined as:

$$
(F * G)(\omega)=\int_{-\infty}^{\infty} F(\nu) G(\omega-\nu) d \nu
$$

Here, $\nu$ iterates over all possible frequency components:
- $F(\nu)$ is the value of the Fourier Transform of one function at the frequency $\nu$.
- $G(\omega-\nu)$ is the value of the Fourier Transform of the other function, shifted by $\nu$, evaluated at $\omega$.

The product $F(\nu) G(\omega-\nu)$ is then integrated over all frequencies. What this does is to sum up all possible interactions between different frequency components of the two functions, where $\nu$ allows each frequency component of $F$ to interact with a correspondingly shifted component of $G$. This "shifting" and summing up are essential to the convolution process, determining how the frequency content of one function modifies that of another.



