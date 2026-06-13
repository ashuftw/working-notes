---
tags: [DAC, numerics, boundary-conditions, ghost-cell]
aliases: [Ghost cell, Wall BC]
---

# Ghost Cell Handling (Wall Adsorption BC)

> [!abstract] In one line
> A **ghost cell** is a fake cell just outside the domain whose value we *choose*
> so that the boundary behaves the way we want. At the wall, we choose it so the
> CO₂ diffusing to the wall equals the CO₂ the wall adsorbs.

## What is a ghost cell?

The solver only updates *interior* cells, but the update stencil needs a neighbour
on each side. At the edge there is no real neighbour, so we add one **ghost cell**
and write a value into it every timestep to encode the boundary condition.

```
 gas (interior)        wall
 ... | C_{n-2} | C_{n-1} |  C_n   |
                  ^node     ^ghost cell (outside the domain)
                          surface is here →|
```

- $C_{n-1}$ = last **real** gas cell (next to the wall)
- $C_n$ = the **ghost** cell (we invent its value)

## The physics at the wall

Two CO₂ flows must balance at the wall:

1. **Diffusion** bringing CO₂ from the gas to the wall
2. **Adsorption** taking CO₂ into the solid: rate $= k_s\,(q^* - q)$

where $q$ = current wall loading, $q^*$ = equilibrium loading.

## Old way (simple, but fragile)

Assume a **fixed** equilibrium loading $q_e$ and write the ghost cell directly:

$$
C_n = C_{n-1} - \frac{\Delta r}{2 D_{AB}}\, k_s\,(q_e - q)
$$

> [!warning] The problem
> If the adsorption term is large, the subtraction can push $C_n$ **below zero**
> (a negative concentration — unphysical). The model then misbehaves
> (oscillations, fake early breakthrough).

## New way (robust)

Don't assume $q_e$. Instead solve for the **surface concentration** $C_s$ so that
diffusion = adsorption, *then* set the ghost cell to it.

**Step 1 — solve for $C_s$ (kept $\ge 0$):**

$$
\underbrace{\frac{2 D_{AB}}{\Delta r}\,(C_{n-1} - C_s)}_{\text{diffusion to wall}}
=
\underbrace{k_s\,\big(q^*(C_s) - q\big)}_{\text{adsorption}}
$$

Here $q^*(C_s)$ is the **Toth loading evaluated at the surface value** (not a constant).
One nonlinear equation → solved with a few Newton iterations.

**Step 2 — set the ghost cell:**

$$
C_n = C_s
$$

> [!tip] Why it can't go negative
> We bracket the solution in $[0,\ \text{high}]$, so $C_s \ge 0$ always — and since
> $C_n = C_s$, the ghost cell is never negative.

## The two are the same equation

The old formula is just the new one with $q^*$ frozen at $q_e$ **and** no $\ge 0$ guard:

$$
q^*(C_s) = q_e \;\Rightarrow\;
C_s = C_{n-1} - \frac{\Delta r}{2 D_{AB}} k_s (q_e - q)
$$

So the upgrade = (1) let $q^*$ follow the local concentration, (2) forbid negative $C_s$.

## Where it lives in the code

- `solvers.py` → `apply_boundary_conditions` (the `tsa_enabled` branch) — Step 1 Newton loop + Step 2 ghost cell.
- `toth_q_and_deriv` provides $q^*(C_s)$ and its slope for Newton.
- Old explicit formula kept in the `else` branch for legacy constant-$q_e$ runs.
