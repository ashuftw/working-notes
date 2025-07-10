---
title: Method of Lines
draft: true
tags: 
date: 2025-07-09
---
It is a technique for solving PDEs by:

1. **Discretizing only the spatial derivatives** (keeping time continuous)
2. Converting the PDE into a **system of ODEs**
3. Solving the ODEs with standard ODE methods

### Where to find it in the lecture notes:

Look for **Section 3.2: "Discretization in one dimension"** (page 44-49 in the script). Specifically:

- **"Method of lines semi-discretization in space"**
- The heat equation example: $u_t = u_{xx}$

The script shows:

```
Approximate values: u_j(t) ≈ u(t, x_j)
∂u/∂t(t, x_j) ≈ u'_j(t)
∂²u/∂x²(t, x_j) ≈ [u_{j-1}(t) - 2u_j(t) + u_{j+1}(t)]/Δx²
```

This gives the ODE system: $$u'_j(t) = \frac{1}{\Delta x^2}[u_{j-1}(t) - 2u_j(t) + u_{j+1}(t)]$$

### Key concept:

- **Finite differences**: Full discretization in space AND time
- **Method of lines**: Only discretize space, then use ODE solvers for time

The wave equation follows the same principle but needs conversion to first-order form first (as shown in my solution).

**Note:** The script uses German term "Linienmethode" - it's the same concept!## Method of Lines (Linienmethode)

The **Method of Lines** is a technique for solving PDEs by:

1. **Discretizing only the spatial derivatives** (keeping time continuous)
2. Converting the PDE into a **system of ODEs**
3. Solving the ODEs with standard ODE methods

### Where to find it in the lecture notes:

Look for **Section 3.2: "Discretization in one dimension"** (page 44-49 in the script). Specifically:

- **"Method of lines semi-discretization in space"**
- The heat equation example: $u_t = u_{xx}$

The script shows:

```
Approximate values: u_j(t) ≈ u(t, x_j)
∂u/∂t(t, x_j) ≈ u'_j(t)
∂²u/∂x²(t, x_j) ≈ [u_{j-1}(t) - 2u_j(t) + u_{j+1}(t)]/Δx²
```

This gives the ODE system: $$u'_j(t) = \frac{1}{\Delta x^2}[u_{j-1}(t) - 2u_j(t) + u_{j+1}(t)]$$

### Key concept:

- **Finite differences**: Full discretization in space AND time
- **Method of lines**: Only discretize space, then use ODE solvers for time

The wave equation follows the same principle but needs conversion to first-order form first (as shown in my solution).

**Note:** The script uses German term "Linienmethode" - it's the same concept!