---
title: Order of Consistency
draft: false
date: 2023-06-28
---
## Intuition

The order of consistency tells us how quickly the error of a numerical method decreases as we make the step size smaller.

## Examples from ODE Methods:

1. **Euler Method (Order 1)**
- $\mathrm{T}(\mathrm{t}, \mathrm{h})=\mathrm{O}(\mathrm{h})$
- Halving $\mathrm{h} \rightarrow$ error reduces by factor 2
- Simple but not very accurate
2. **Euler-Heun Method (Order 2)**
- $\mathrm{T}(\mathrm{t}, \mathrm{h})=\mathrm{O}\left(\mathrm{h}^2\right)$
- Halving $\mathrm{h} \rightarrow$ error reduces by factor 4
- Much more accurate than Euler
3. **Classical Runge-Kutta (Order 4)**
- $\mathrm{T}(\mathrm{t}, \mathrm{h})=\mathrm{O}\left(\mathrm{h}^4\right)$
- Halving $\mathrm{h} \rightarrow$ error reduces by factor 16
- Very high accuracy

## Definition  to be corrected

![[../Files/Pasted image 20230703100657.png|center]]