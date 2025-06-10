---
title: Steady State DAC Equations
draft: true
tags: 
date: 2024-10-16
---

## 2D Diffusion Equation

$$
\frac{\partial Ca}{\partial t}+u_d\frac{\partial Ca}{\partial x} =D_{AB}\left(\frac{\partial^2 Ca}{\partial y^2}\right)
$$

## Discretize Time with Forward Differerence  and Space with Central Difference

$$
\frac{Ca_{i, j}^{(n+1)}-Ca_{i, j}^{(n)}}{\Delta t}+u_d\left[\frac{Ca^{(n)}_{i+1,j}-Ca^{(n)}_{i-1,j}}{2 \Delta x}\right]=D_{AB}\left[\frac{Ca_{i, j+1}^{(n)}-2 Ca_{i, j}^{(n)}+Ca_{i, j-1}^{(n)}}{(\Delta y)^2}\right]
$$

Where 
- $n\rightarrow$ time
- $i \rightarrow$ x 
- $j\rightarrow$ y

### Rearranging

$$
Ca_{i, j}^{(n+1)}=Ca_{i, j}^{(n)} - \Delta t\left(u_d\left[\frac{Ca^{(n)}_{i+1,j}-Ca^{(n)}_{i-1,j}}{2 \Delta x}\right]  - D_{AB} \left[\frac{Ca_{i, j+1}^{(n)}-2 Ca_{i, j}^{(n)}+Ca_{i, j-1}^{(n)}}{(\Delta y)^2}\right]\right)
$$

[Source](https://scipython.com/book/chapter-7-matplotlib/examples/the-two-dimensional-diffusion-equation/)