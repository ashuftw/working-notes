---
title: Gauss's Divergence Theorem(L)
draft: false
date: 2022-05-19
---

## Gauss's Divergence Theorem

![[Pasted image 20220508174314.png|center|300]]

>**Definition:**
>The flux of a vector field $\vec F$ through a closed surface $S$ is equal to the integral of the divergence  $\nabla \cdot \vec F$ over the entire enclosed volume $V$.

$$
\boxed{\int\int\int_V dV=\int\int_S \vec F\cdot \vec  n\ dS }
$$

**Why it's true**
The local divergence in the every point in the field may be represented as follows 
![[Pasted image 20220508182910.png|center|300]]
- Assuming the vector field is continuous, and the grid is infinitesimally fine, the fluxes in the opposite direction of each neighbour-owner pair, cancel each other out. 
- When each sub volume is integrated, the only divergence vectors that remain belong to the cells without neighbours i.e. along the surface.
  ![[Pasted image 20220508183206.png|center|300]]
- Note: The integral of all the divergence vectors along the surface is nothing but the **flux** through the surface.

>**I don't understand this:**
>To calculate the volume of an irregular shape, we can set the divergence as 1 and the surface integral gives us the area.

---

# References

1. https://www.youtube.com/watch?v=TORt20_HjMY&t=38s
