---
title: GPC Example
draft: false
tags: 
date: 2025-07-31
---
![[../Files/Pasted image 20250731180605.png]]
## 1. Calculation of gPC Coefficients

The gPC expansion is given by $\mathcal{M}(X) \approx \sum_{i=0}^{3} q_i \Phi_i(X)$.
The coefficients $q_i$ are found using the projection formula:
$$
q_i = \frac{E[\mathcal{M}(X)\Phi_i(X)]}{E[\Phi_i(X)^2]}
$$
The problem states the Legendre polynomials $\Phi_i(X)$ are **normalized**, which means their expected square is one: $E[\Phi_i(X)^2] = 1$. Therefore, the formula simplifies to:
$$
q_i = E[\mathcal{M}(X)\Phi_i(X)] = E[X^2 \Phi_i(X)]
$$
We will use the general rule for expectations of powers of $X$: $E[X^n] = \frac{1}{n+1}$ for even $n$, and $0$ for odd $n$.

$$
q_0 = E[X^2 \cdot \Phi_0(X)] = E[X^2 \cdot 1] = E[X^2] = \frac{1}{2+1} = \frac{1}{3}
$$

$$
q_1 = E[X^2 \cdot \Phi_1(X)] = E[X^2 \cdot \sqrt{3}X] = \sqrt{3}E[X^3] = \sqrt{3} \cdot 0 = 0
$$

$$
q_2 = E[X^2 \cdot \Phi_2(X)] = E\left[X^2 \cdot \frac{\sqrt{5}}{2}(3X^2 - 1)\right] = \frac{\sqrt{5}}{2} E[3X^4 - X^2]
$$
Using linearity of expectation:
$$
q_2 = \frac{\sqrt{5}}{2} (3E[X^4] - E[X^2]) = \frac{\sqrt{5}}{2} \left(3\left(\frac{1}{5}\right) - \frac{1}{3}\right) = \frac{\sqrt{5}}{2} \left(\frac{3}{5} - \frac{1}{3}\right)
$$
$$
= \frac{\sqrt{5}}{2} \left(\frac{9-5}{15}\right) = \frac{\sqrt{5}}{2} \left(\frac{4}{15}\right) = \frac{2\sqrt{5}}{15}
$$
This can also be written as $\frac{2}{3\sqrt{5}}$.
$$
q_3 = E[X^2 \cdot \Phi_3(X)] = E\left[X^2 \cdot \frac{\sqrt{7}}{2}(5X^3 - 3X)\right] = \frac{\sqrt{7}}{2} E[5X^5 - 3X^3]
$$
Since both terms are odd powers, their expectations are zero:
$$
q_3 = \frac{\sqrt{7}}{2}(0 - 0) = 0
$$

---

## 2. Statistics from gPC Coefficients

With the coefficients known, we can easily calculate the statistics of the model output $Y = X^2$.

### Mean Value
The mean is given by the first coefficient, $q_0$.
$$
E[Y] = E[X^2] = q_0 = \frac{1}{3}
$$

### Variance
The variance is the sum of the squares of all higher-order coefficients ($i \geq 1$).
$$
V[Y] = V[X^2] = \sum_{i=1}^{\infty} q_i^2 = q_1^2 + q_2^2 + q_3^2
$$
$$
= 0^2 + \left(\frac{2\sqrt{5}}{15}\right)^2 + 0^2 = \frac{4 \cdot 5}{225} = \frac{20}{225} = \frac{4}{45}
$$

### Raw Second Moment
The raw second moment is the sum of the squares of *all* coefficients ($i \geq 0$).
    $$ \mathbb{E}[Y^2] = \mathbb{V}[Y] + (\mathbb{E}[Y])^2 = \sum_{i=1}^{P} q_i^2 + q_0^2 $$
$$
E[Y^2] = E[(X^2)^2] = E[X^4] = \sum_{i=0}^{\infty} q_i^2 = q_0^2 + q_1^2 + q_2^2 + q_3^2
$$
$$
= \left(\frac{1}{3}\right)^2 + \left(\frac{2\sqrt{5}}{15}\right)^2 = \frac{1}{9} + \frac{4}{45} = \frac{5}{45} + \frac{4}{45} = \frac{9}{45} = \frac{1}{5}
$$
This result is consistent with the direct calculation of $E[X^4] = \frac{1}{4+1} = \frac{1}{5}$.