---
title: 2D Wave equation
draft: false
date: 2022-10-20
---

![[Pasted image 20221021220509.png|center]]

$$
y=A\cos \left(\frac{2\pi}{\lambda}x\pm\frac{2\pi}{T}t+\phi\right)
$$

## Wave Equation Formulation

### 1. Function in Space

The amplitude is maximum at $(x = 0)$, implying the function is cosine.

Initial form:
$$y = A \cos \theta$$

The cosine resets at intervals of $2\pi$, i.e., $x = \lambda$ (wavelength):
$$y = A \cos \left(\frac{2\pi}{\lambda}x\right)$$

### 2. Function in Time

The cosine resets at intervals of $2\pi$, i.e., $t= T$ (time period):
$$y = A \cos \left(\frac{2\pi}{\lambda}x \pm \frac{2\pi}{T}t\right)$$

> **Note:** The temporal part gets a $\pm$ because the wave could be moving forward or backward.

## 3. Final Equation

$$\boxed{y = A \cos \left(\frac{2\pi}{\lambda}x \pm \frac{2\pi}{T}t + \phi\right)}$$

Where:
- $A$: Amplitude
- $\lambda$: Wavelength
- $T$: Time period
- $\phi$: Phase shift
- $x$: Position in space
- $t$: Time

--- 
# References

[The equation of a wave | Physics | Khan Academy](https://www.youtube.com/watch?v=9WZM68aVnGk)