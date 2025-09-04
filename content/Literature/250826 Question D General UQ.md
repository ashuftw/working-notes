---
title: Question D General UQ
draft: true
tags:
date:
---
**The task is to compute the sound pressure at a certain location inside the passenger cabin. The cabin is a cube of dimensions $[l_1,l_2,l_3]$ and co-ordinates $[r_1,r_2,r_3]$.** 

**We have a black-box solver that solves the pressure field $p(r_1,r_2,r_3)$ for the whole box. The solver takes as arguments, the co-ordinates, Young's Modulus of the Walls and Air density.** 
![[../Files/Pasted image 20250831114622.png|400]]

1. **Write down a formula defining the quantity of interest relating to the model input parameters**

	$$
	Y = \frac{1}{d_1 d_2 d_3}\int_{\frac{-d_1}{2}}^{\frac{d_1}{2}} \int_{\frac{-d_2}{2}}^{\frac{d_2}{2}}\int_{\frac{-d_3}{2}}^{\frac{d_3}{2}} P(r_1,r_2,r_3)\,dr_1dr_2dr_3
	= M(X) $$
	Note: We do integrate because we care about the average
	2. **Specify the model input distribution and justify as much as possible**
	Input vector reads
	$$X=(E,\rho)$$
	where,
	- $\rho\sim\mathcal U(\rho_1, \rho_2)$
	- $E\sim \mathcal L \mathcal N(\mu_E,\sigma_E)$ are independent (non physical connection)
	Note: The log normal distribution is chosen to ensure positive values.
	3. **With formulas, show how moments of the quantity of interest can be approximated. Justify the method**
	The output is a spatial average (will depend smoothly on the inputs) and the model only depends on two parameters. Hence, a quadrature method is chosen. (Quadrature approximates the integral accurately for two parameters)
	4. **Now the Young's Modulus is modeled as a Gaussian random field $E(r,\theta)$ with $D\in \mathbb R^3,\, \theta\in \mathbb \Theta$**
	What can you do to handle this field as in put and which method would you choose to compute moments of the quantity of interest.



