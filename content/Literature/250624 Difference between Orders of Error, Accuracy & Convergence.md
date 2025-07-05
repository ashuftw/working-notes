---
title: Difference between Orders of Error, Accuracy & Convergence
draft: false
tags: 
date: 2025-06-24
---
## Key Differences

### Degree of Accuracy $(K)$
Used for **quadrature formulas** - the maximum degree of polynomials that are integrated exactly.

### Order of Consistency $(q)$
Used for **ODE methods** - The order of consistency tells us how quickly the **local** error of a numerical method decreases as we make the step size smaller. It is the power of $h$ in the local truncation error: $\tau = O(h^q)$.

### Convergence Order
The power of $h$ in the **global** error bound (multiple steps)- often equals consistency order for stable methods.

## Summary Table

| Term                         | Context               | Definition                                         | Example                 |
| ---------------------------- | --------------------- | -------------------------------------------------- | ----------------------- |
| **Degree of Accuracy $(K)$** | Numerical Integration | Max polynomial degree integrated exactly           | Trapezoid rule: $K = 1$ |
| **Consistency Order $(q)$**  | ODE Methods           | Power in local error: $\tau = O(h^q)$              | Euler method: $q = 1$   |
| **Convergence Order**        | ODE Methods           | Power in global error: $\|y(t_i) - y_i\| = O(h^q)$ | Euler method: order $1$ |

## Quick Examples

- **Simpson's rule**: Degree of accuracy K = 3 (integrates cubics exactly)
- **Euler method**: Consistency order q = 1 (local error ~ h²)
- **RK4**: Consistency order q = 4 (local error ~ h⁵)
