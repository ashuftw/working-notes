---
title: Expected Value
draft: false
date: 2023-05-05
---

## Definition
It is the average value (mean) of a random experiment. 

### Expected Value for
1. **Discrete Random variable **
$$
\mathbb{E}[X]:=\sum_{i=1}^n X(\theta_i) \cdot P(X(\theta_i))
$$

2. **Continuous Random variable**
 
$$
\begin{aligned}\mathbb{E}[X]&:=\int_{\Theta} X(\theta) d \mathbb{P}(\theta)
 \\ &\text{or}\\
 \mathbb{E}[X]&:=\int_{-\infty}^{\infty} x f_X(x) \mathrm{d} x
 \end{aligned}
$$


where, $n\rightarrow$ size of sample space, $\theta\rightarrow$ sample space, $X\rightarrow$random variable, $x=X(\theta)$, $P\rightarrow$ Probability & $f_X\rightarrow$ PDF

### Linearity of Expectation 

$$
\mathbb E[A+B]=\mathbb E[A]+\mathbb E[B]
$$





---
# References
1. https://brilliant.org/wiki/expected-value/
2. Uncertainty Analysis Script Pg.12 