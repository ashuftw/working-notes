---
title: Leaf Hydraulics and Transpiration
draft: false
tags:
date: 2026-06-02
---
## Leaf anatomy 
![[../Files/Pasted image 20260721201852.png|center|500]]
![[../../Files/Pasted image 20260602115031.png|center|600]]
The opening of the guard cells are influenced by the following factors
- CO$_2$ 
- Water vapour 
- Sunlight 
- Wind-speed at the leaf surface (in relation the boundary layer) also has an impact. 
## Functioning of the guard cells

![[../Files/Pasted image 20260722102107.png|center|500]]


> [!NOTE] 
> The stomata also opens up to other gases that may be harmful for the plant. We know that the mechanism is due to hormones but what exactly triggers this mechanism is not known. 

## Fick's law of diffusion 
The physical processes at the leaf are governed by diffusion
$$
J=-D \frac{d \varphi}{d x}
$$
$$
\text{Diffusive flux = }-\text{Diffusivity}\times \text{Concentration gradient}
$$
#### Transpiration
$$
\text{How fast water exits= }\text{Stomatal conductance}\times \text{Dryness of air}
$$
#### Photosynthesis
$$
\text{How fast CO}_2 \text{ enters= }\text{Stomatal conductance}\times \text{Concentration difference of CO}_2
$$

> [!QUESTION] Catch
> The stomatal conductance $g$ for water is measured to be 1.6 times that of CO$_2$
> $$g_{\mathrm{s}, \mathrm{CO}_2}=\frac{1}{1.6} g_{\mathrm{s}, \mathrm{H}_2 \mathrm{O}}$$
> The difference is because of the fact that water molecules are smaller and have lesser molar weight (18$\text g$ compared to 44$\text g$ of CO$_2$)

## Leaf water balance
![[../Files/Pasted image 20260722123419.png|center|148]]

where, 

$$
\overbrace{C_L \frac{d \Psi_L}{d t}}^{\substack{\text{rate at which stored} \\ \text{water in
leaf is changing}}}=Q_{S \rightarrow L}-E
$$
$C_L\rightarrow$ leaf capacitance 
$E\rightarrow$ evaporation 
$Q_{\text S\rightarrow\text L}$ stand for flow from soil to leaf

## Stomatal conductance 
The models improve in 3 stages:
1. **Empirical** 
	- Jarvis: start open, multiply penalties. No carbon link.
		- *Guesses how open the pore is from the weather alone. Just fits the observed response to light, heat, dryness and CO$_2$ never asks why the plant opens the pore in the first place.*
2. **Semi-empirical** 
	- Ball–Berry: open $\propto$ photosynthesis (adds the carbon link). 
		- *Stomata open in step with how much carbon the leaf is fixing, this is why they open. They close in dry air or high CO$_2$ to save water.*
	- Leuning: minor tweak for dry air.
		- *Same idea as Ball–Berry, just a more realistic response to dry air.*
3. **Optimisation** 
	- Cowan–Farquhar: maximise carbon, minimise water.
		- *Stops fitting curves and assumes the plant is smart: open only as much as gives the most carbon for the least water lost. A cost–benefit principle, not a fitted rule.*
	- Medlyn: makes it usable.
		- *Turns that principle into a practical formula you can actually compute with.*

> [!NOTE] Bell-berry model caveat
> ![[../Files/Pasted image 20260722205316.png|center|400]]
>  The model is not suitable for low carbon uptake because Ball–Berry ties opening to photosynthesis, it breaks down when photosynthesis is near zero (night, shade, stress). It wrongly predicts near-closed stomata when they're actually still open.


> [!question] Are stomata really optimising?
> Optimising" means the plant acts as if trying to get the most carbon for the least water lost. Stomata behave close to optimally but that in itself isn't proof and since they  can't predict the future or react instantly, we can't say they truly optimise. So: we don't know.
