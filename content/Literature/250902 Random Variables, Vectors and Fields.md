---
title: Random Variables, Vectors and Fields
draft: false
tags:
date: 2025-09-02
---
## Illustrative context: Design of Turbine blad

- **Manufacturing**. The thickness of the composite material used for the blade might vary slightly from the design specification of $L$. We can describe this uncertainty with a Normal distribution centered at $L$.
- **Wind is unpredictable**. While we know the average wind speed at the turbine's location, the exact force hitting the blade at any given moment fluctuates. This force also varies along the length of the blade—the wind hitting the tip is different from the wind hitting the base.
- **Material properties** of the blade's internal support spar, like its Young's modulus and density, are not known with perfect precision.

### Random Variable
A single uncertain value, like blade thickness $T$.
Modeled with a probability distribution:
$$T \sim \mathcal{N}(\mu_T, \sigma_T)$$


### Random Vector
A set of uncertain values, like material density $\rho$ and stiffness $E$.
Modeled as a vector $X$ with a joint distribution:
$$ X = \begin{bmatrix} \rho \\ E \end{bmatrix} \sim \mathcal{N}(\mu_X, C_X) $$

### Random Field
An uncertain quantity varying in space, like wind load $p$ along the blade's length $r$.
Modeled as a random function $p(r)$:
$$ p(r) = \mu_p(r) + \sum_{i=1}^{\infty} \sqrt{\lambda_i} \phi_i(r) \xi_i $$
This is a Karhunen-Loève expansion, representing the field with a mean function $\mu_p(r)$ and random deviations.


![An animated GIF from the web](https://upload.wikimedia.org/wikipedia/commons/6/62/Exp_series.gif)

