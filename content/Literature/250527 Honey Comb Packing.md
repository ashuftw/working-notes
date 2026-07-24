---
title: Honeycomb Packing
draft: true
tags: 
date: 2025-05-27
---
![[../Files/Pasted image 20250527131308.png|center|800]]
- **$D$**: Honeycomb diameter (10 cm)
- **$d$**: Opening length/diameter
![[../Files/Pasted image 20250527131628.png|center|500]]
- **$t$**: Wall thickness = $t_m + 2t_{a}$
    - $t_m$: monolith thickness
    - $t_{a}$: adsorbent thickness
- **$N$**: Number of cells

## Cell Density Relationship 

Along $x-$direction



$$
D = \underbrace{n_x\cdot d }_\text{Opening}+ \underbrace{(n_x + 1)t}_\text{Monolith} = n_x(d + t) + t
$$



Therefore: 



$$
n_x = \frac{D - t}{d + t} \approx \frac{D}{d +t}
$$



## Cell Count for Different Honeycomb Types

- **Square Honeycomb**






	$$
	N_\text{square} =n_s^2
	$$






- **Circular honeycomb**






	$$
	\frac{\text{square}}{\text{dish}} = \frac{D^2}{\pi D^2/4} = \frac{4}{\pi} \approx 1.27
	$$






Therefore: 

$$
N_\text{circle} = \frac{N_s^2}{4/\pi} = \frac{\pi}{4} \frac{D^2}{(d + t)^2}
$$



## Adsorbent Surface Area

![[../Files/Pasted image 20250527135810.png|center|400]]



$$
S_a = 4 \times N_c \times d \times L
$$



Where:

- $4$: Number of walls per cell
- $N_c$: Number of cells
- $d$: Cell opening diameter
- $L$: Length of honeycomb