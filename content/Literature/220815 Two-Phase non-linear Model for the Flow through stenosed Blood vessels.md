---
title: Two-Phase non-linear Model for the Flow through stenosed Blood vessels
draft: false
date: 2022-08-15
---

Mar 2022
    

Tags: [[Multiphase flow]] [[Blood flow]] [[Journal Paper]]

# Two-Phase non-linear Model for the Flow through stenosed Blood vessels
*D. S Sankar, Usik Lee*

## Introduction
- **Blood**
   Suspension of cells in Plasma. 
- **Behaviour**
  - Approximated as Newtonian in a large artery.
  - Non-Newtonian in small diameter arteries (0.02 mm-0.1 mm), at low shear rates ($\dot \gamma<10 \ s^{-1}$)
  - Flow through a narrow artery has a peripheral layer of Plasma (Newtonian) and a core region of RBCs (non-Newtonian).
  - Velocity profile at a narrow artery cannot be accurately measured using a Newtonian model.  
  - For realistic description of blood flow, 2 fluid model is required.[^1]
  >  The velocity profiles in the arterioles having diameter less than 0.1 mm are generally explained fairly by the Casson and Herschel-Bulkley fluid models. However, the velocity profiles in the arterioles whose diameters less than 0.0650 mm do not conform to the Casson fluid model, but, can still be explained by the Herschel-Bulkley model".[^2]
## Mathematical Formulation
- **Assumptions**
  - Artery is axially symmetric with mild stenosis, walls are rigid. 
  - Flow is laminar, pulsatile and fully developed. (Plug flow in the centre)
  - Blood is incompressible. 
  - Radial velocity is negligibly small for small $R_e$ Hence neglected.
- **Essential Nomenclature**

$$
\begin{array}{c c}
\hline
 \textbf{Nomenclature} &    \\ 
\hline
	u_H & \text{Velocity of core}    \\
	u_N & \text{Velocity of periphery}    \\
	\tau_H & \text{Shear Stress of core}    \\
	\tau_N & \text{Shear Stress of periphery}    \\
	\alpha_H & \text{Pulsatile Reynolds Number of core}    \\
	\alpha_N & \text{Pulsatile Reynolds Number of periphery}    \\
	\alpha_N & \text{Pulsatile Reynolds Number of periphery}    \\
\hline
\end{array}
$$


- **Domain**
![[Pasted image 20220315162014.png|center]]
[^6]
$$
\beta =\dfrac{\text{core radius}}{\text{normal artery radius}}=0.95
$$

At $\beta=1$, the model reduces to single-fluid model
Stenosis at periphery $0.05<\delta_p<0.3$

  R coordinates for Peripheral Region
  ![[Pasted image 20220316135104.png|center]]
  R coordinates for the core region 
  ![[Pasted image 20220316135154.png|center]]
- **Boundary Conditions**
  - Because Plug flow is assumed at the center.
  ![[Pasted image 20220316135434.png|center]]
  - No slip at wall ($R(z)\rightarrow$ End of stenosed peripheral region)
  ![[Pasted image 20220316135725.png|center]]
  -  Interface between core and peripheral regions have same velocity ($R_1(z)\rightarrow$ end of stenosed core region)
  ![[Pasted image 20220316140746.png|center]]
  - Temporal Component for Pulsatile behavior (0<A<1, but used 0.2<A<0.5 to pronounce the effect)
  ![[Pasted image 20220316141524.png|center]]
  - Inlet velocity as a function of radius 
	  - At Periphery $\zeta = \alpha_H ^2$   
	  ![[Pasted image 20220316141838.png|center]]
	  - At core
		  ![[Pasted image 20220316141922.png|center]]
	- Pulsatile Reynolds Number ratio $\alpha=\dfrac{\alpha_N}{\alpha_H}$
		- $0<\alpha<1\approx 0.5$[^3]
	- Reynolds Number
		- $0<\alpha_H<1$, but used $0.5 \ \& \ 0.25$  
  
- **Transport Properties**
  - Core: [[220613 Herschel-Bulkley Equation]]
	  $\dot \gamma <$ 10 (s$^{-1}$)
	  For n < 1, take n = 0.95 [^4]
	  For n > 1, take n = 1.05
	  Healthy:
			0.1 <$\theta$< 0.3 
	  Unhealthy:
			0.05<$\theta$<0.15 (yield stress is 5 times in diseased state[^5])
	  


---
# References
[^1]: Bugliarello, G, Sevilla, 1., 1970, "Velocity Distribution and Other Characteristics of Steady and Pulsatile Blood Flow in Fine Glass Tubes," Biorheology, Vol.7, pp. 85~ 107
[^2]: N., 1978, "Influence of Plasma Layer on Steady Blood Flow in Micro Vessels," Japanese Journal ofAppliedPhysics, Vol. 17, pp. 203~ 214. 
[^3]: D.S. Sankar, U. Lee, Two-fluid nonlinear mathematical model for pulsatile blood flow through catheterized arteries, J. Mech. Sci. Technol. 23 (2009) 1650–1669.
[^4]: Sankar D. S., Hemalatha, K., 2006, "Pulsatile Flow of Herschel-Bulkey Fluid Through Stenosed ArteriesA Mathematical Model," International Journal of Non-Linear Mechanics, Vol. 41, pp. 979~990.
[^5]: S. Chakravarthy, A. Datta, P.K. Mandal, Analysis of nonlinear blood flow in a stenosed flexible artery, Int. J. Eng. Sci. 33 (1995) 1821–1837.
[^6]: V.P. Srivastava, M. Saxena, Two-layered model of Casson fluid flow through stenotic blood vessels: applications to the cardiovascular system, J. Biomech. 27 (1994) 921–928.
