---
title: Flashcards on Numerical Computation of Moments
draft: false
tags:
date: 2025-09-04
---
#### What is the fundamental difference between **Monte Carlo integration** and **Quadrature** for computing an expected value?

-   **Monte Carlo**: Uses **random points** and equal weights ($w_i = 1/K$).
-   **Quadrature**: Uses deterministically chosen **nodes** ($x^{(i)}$) and specific **weights** ($w^{(i)}$) to optimize accuracy for a given number of points.

--- 
#### How does **quadrature** extend from a **single** input variable to **multiple** **dimensions**? What is this construction called?

By taking all possible combinations of the one-dimensional nodes for each variable. This creates a multi-dimensional grid of points.

This construction is called a **Tensor Product Rule**.

---
#### In the context of **quadrature**. What is the main drawback of **tensor product rules**, and what is a common strategy to mitigate it?

The main drawback is the **"curse of dimensionality"**, where the total number of points ($n_{qu;1} \cdot n_{qu;2} \cdot ...$) grows exponentially with the number of input dimensions, making it computationally infeasible.

A strategy to mitigate this is using **Sparse Grids**, which intelligently leave out less significant points from the full tensor grid.
![[Files/Pasted image 20250904145547.png]]

---

#### How does Quadrature fit into the "non-intrusive" approach to uncertainty quantification?

Quadrature is non-intrusive because it treats the computational model $\mathcal{M}(x)$ as a "black box." It only requires model evaluations at the specified quadrature points and does not require any modification of the model's internal code.

---
#### Can quadrature be used only to calculate the first moment? Why or why not?

No, that is incorrect.

**Any statistical moment is an integral**, and quadrature is a tool for approximating integrals. To compute a **higher-order moment**, you simply apply the quadrature rule to the appropriate function.

For the **k-th raw moment**, $\mathbb{E}[\mathcal{M}(X)^k]$, the quadrature formula is:
$$
\mathbb{M}^{k}[Y] \approx \sum_{i=1}^{n_{qu}}(\mathcal{M}(x^{(i)}))^{k}w^{(i)}
$$
By calculating these moments (mean, variance, etc.), one can construct an approximate PDF for the model output.

---
#### Both **FOSM** and **Quadrature** approximate moments. Why would you choose Quadrature over FOSM?

You would choose Quadrature for higher accuracy, especially when the model is non-linear or input uncertainties are large.

-   **FOSM** is a linearization that works well only for small uncertainties.
-   **Quadrature** can achieve high accuracy by using more points and can capture complex, non-linear model behavior without relying on derivatives.

--- 
#### When would choosing the First-Order Second-Moment (FOSM) method be better than using Quadrature for uncertainty quantification?

FOSM is a better choice for problems with **many input variables (high dimensionality)** combined with **small input uncertainties**.

This is because of the fundamental trade-off between computational cost and accuracy:

##### FOSM
-  **Pro:** Very cheap. Its computational cost does **not** grow exponentially with the number of input dimensions.
-  **Con:** It's a linearization. Its accuracy is only reliable for small input uncertainties and for models that are nearly linear. It also requires calculating model derivatives.

##### Quadrature
-  **Pro:** Can be highly accurate, even for very non-linear models.
-  **Con:** Suffers from the **"curse of dimensionality."** The number of model evaluations needed grows exponentially with the number of dimensions, quickly becoming computationally infeasible.

**Conclusion:** In a high-dimensional problem, a Quadrature rule might be too computationally expensive to even run. In this scenario, FOSM is the more practical, and therefore better, choice, as long as the input uncertainties are small enough for its approximation to be valid.