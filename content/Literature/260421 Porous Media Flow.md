---
title: Porous Media Flow
draft: false
tags:
date: 2026-04-21
---
![[../Files/Pasted image 20260717134730.png|center|800]]

> [!Question] What physically changes when water moves from soil into the Xylem?
> In soil the movement of water is driven by capillary action. In the Xylem the transport is due to the negative pressure potential caused by transpiration.
 

### Preferential flow & Darcy's law 
It's when water flows through macro-pores created by earthworms, roots etc. One can lump these effects and describe the flow using Darcy's law.	
![[../../Files/Pasted image 20260421114916.png|center]]
$$\boxed{
v_f=-K \frac{\Delta \psi}{\Delta \ell} \approx-K \frac{\partial \psi}{\partial \ell}}
$$

where, $K \rightarrow$ hydraulic conductivity ($m/sPa$)

> [!NOTE]
> The Darcy velocity gives the average velocity of the fluid with which it crosses a specific length of the porous media. 
> ![[../../Files/Pasted image 20260421115527.png|400]]

The Darcy equation is used for the Plant and the Soil in order to simplify the system. It represents a statistical mean of many Poiseuille flows.
![[../../Files/Pasted image 20260421120029.png|center|500]]
## Porosity 
The soil is considered to be a a porous medium. It's conductivity is then dependent on porosity & packing density. 
$$
n=\frac{\text { volume of the pore space }}{\text { volume of the REV }}
$$
where, $n\rightarrow$ porosity, $\text{REV}\rightarrow$ representative elementary volume

To calculate the porosity. One takes a small volume of the soil and measures the pore space. Naturally, larger the sample, more accurate is the measurement. 


> [!Warning] Note 
> The core assumption of the soil conductance (based on potential) falls apart when you have a crack or micro pore. Then all the flow is through that crack or pore (bypass)

### Relationship between Porosity & Conductivity
High porosity does not necessarily mean high conductivity. **Connectedness** also plays an important role. If pores are tine or poorly connected (like clay) then the conductivity is low. 
## **Soil water retention curve**
It give the relationship between the amount of water $\theta$ and the amount pressure ($h$) needed to be applied (suction) to remove the water. 
![[../../Files/Pasted image 20260421122733.png|center]]
From right to left: As suction increases, the soil with the higher porosity ($n=2$), give up water much faster than its counterpart. 

## Conductivity curve
It gives the relationship between the conductivity ($K$) and the suction ($h$). 
![[../../Files/Pasted image 20260421122847.png|center]]

Conductivity decreases as the water content due to suction decreases  


> [!NOTE] 
> Soil conductivity is mainly dependent on saturation:
> - saturated = low conductivity and vice versa. 

## Vulnerability curve
![[../../Files/Pasted image 20260421123242.png|center|600]]
- $y = 0\rightarrow$ all are safe 
- $y=100\rightarrow$ all are dead (fail)
- $\text P50\rightarrow$  water potential where 50% of the xylem is failed. 

**Embolism:** As water potential becomes more negative cavitation become more likely leading to embolism.

## Soil-Plant-Atmosphere Continuum


![[../../Files/Pasted image 20260421124201.png|300]]

> [!QUESTION] Why does water move through the roots instead of evaporating in the air directly?
> Evaporation requires energy (phase change) and Potential flow doesn't require external energy 

> [!QUESTION] If xylem and soil are both porous media, why are plants not just extensions of soil conductivity? 
> Behaviour of flow in soil dependent on water content and the flow is passive. In plants the flow is guided by the active regulation of the stomata which cannot close forever to prevent carbon starvation. Additionally the behaviour is also guided be embolism. 

