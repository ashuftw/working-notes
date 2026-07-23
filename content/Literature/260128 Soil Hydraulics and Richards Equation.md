---
title: Soil Hydraulics and Richards Equation
draft: false
tags:
date: 2026-04-28
---

> [!TIP] Water behaviour
> ![[../Files/Pasted image 20260718154631.png|center|350]]
> Water flows towards increasing negative water potential.

## Improving on the Darcy's law 
Previously we had assumed the soil to be saturated, implying that the conductivity ($K$) was a constant. However in reality the conductivity of the soil is determined by the saturation level of the soil. 
![[../Files/Pasted image 20260718161140.png|center|350]]

$$
K \rightarrow K(\theta)  \text { or } K(\Psi)
$$
Where $\theta$ is water content and $\Psi$ is the soil water potential
The updated Darcy's law
$$\boxed{
q=-K(\Psi) \Psi
}$$
where $q$ is the water flux (flow of water through the soil per unit area, per unit time)

> [!Tip] Coductivity of the soil drops in a non-linear fashion
> **Texture**! 
> Soil has a wide range of pore sizes. When there's suction, the large pore drain first. Since the large pores also channel more water, the conductivity drop is steep in the beginning gets progressively flatter. ![[../Files/Pasted image 20260428115643.png]]

> [!NOTE] 
> The texture of the soil is what impacts it's conductivity

## Richardson's equation  
By applying the conservation of mass to Darcy's law we get:
$$
  \begin{aligned}
  \frac{\partial \theta}{\partial t} &= \nabla \cdot q \\ \\
  \frac{\partial \theta}{\partial t} &= \nabla \cdot K(\Psi)\,\nabla\Psi
  \end{aligned}
$$
![[../Files/Pasted image 20260718221701.png|center|500]]
It is able to accurately capture the non-linear distribution of the water content in the soil. When a soil has been recently wetted, the layer on top is much wetter (near-saturated) while the soil below stays relatively dry separate by a sharp wetting front. 


## Tilia Cordata in Braunschweig
From measurements compared to the park, the trees in the street seemed to draw more water even though the soil is sealed around the tree. Reasons
- more competition in park 
- heat in the sealed zone 
- soil is better because it was artificially put there by the city

> [!QUESTION] If soil sets the operating water potential, why do plants still differ in their Ψ50-values?
> **Safety**: Plants evolve to match the dryness of its own habitat's soil which varies wildly. 
> **Active functioning** : It also depends on the hormones and the stomata regulation.