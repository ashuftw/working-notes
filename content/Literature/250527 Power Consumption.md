---
title: Power Consumption
draft: false
tags: 
date: 2025-05-27
---

## Energy equation:

![[../Files/Pasted image 20250527171803.png|center]]

$$
\dot{w}_{in}=\dot{w}_{DAC} = \underbrace{\frac{\dot m}{\rho} \Delta P_{DAC}}_\text{loss from DAC Filter} + \underbrace{\frac{1}{2}\dot m u_d^2}_\text{loss from Exit}
$$

where, 
- $u_d\rightarrow$ average velocity (parabolic profile)

## DAC cell is a laminar Poiseuille flow:

### Darcy-Weisbach equation for Pressure Drop 

$$\Delta P_{DAC} = f \frac{L}{d} \rho \frac{u_d^2}{2}$$

- $f$ = friction factor
- $L$ = length of channel
- $d$ = diameter of channel

For laminar flow in a circular channel:

$$f = \frac{64}{Re_d} = \frac{64\mu}{\rho u_d d}$$

where $Re_d$ is the Reynolds number and $\mu$ is dynamic viscosity.

### Power consumption

$$
\dot{w}_{DAC} = \dot m \cdot f=\dot{m} \cdot f \frac{L}{d} \frac{u_d^2}{2}
$$

Now substituting the mass flow rate for all channels:

$$\dot{m} = N \rho \frac{\pi d^2}{4} u_d$$

where:
- $N$ = number of cells/channels
- $\frac{\pi d^2}{4}$ = cross-sectional area of one channel

### Combining everything

$$\dot{w}_{DAC} = \left(N \rho \frac{\pi d^2}{4} u_d\right) \times \frac{64\mu}{\rho d u_d} \times \frac{L}{d} \times \frac{u_d^2}{2}$$

### Simplifying

$$\boxed{\dot{w}_{DAC} = 8\pi N \mu L u_d^2}$$

This shows that the power consumption is:
- Proportional to the number of channels ($N$)
- Proportional to viscosity ($\mu$) and length ($L$)
- Proportional to the square of velocity ($u_d^2$)
- Independent of the channel diameter (which canceled out)

### Work done per cell 

$$\boxed{\dot{w}_{cell} = 8 \pi \mu L u_d^2}$$

## Required power

$$
\Delta P_{DAC} = \frac{64 \mu}{\rho d u_d} \times \frac{L}{d} \times \rho \frac{u_d^2}{2}
$$

 $$
\boxed{\Delta P_\text{DAC}= \frac{64 \mu L u_d}{2 d^2}}
$$

## Optimization Problem 

![[../Files/Pasted image 20250527175903.png|center|400]]

$$
\Rightarrow \text{optimizing} \frac{\text{uptake/cell}}{\dot{w}_{cell}}
$$