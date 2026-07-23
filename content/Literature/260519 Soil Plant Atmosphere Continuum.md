---
title: Soil Plant Atmosphere Continuum
draft: false
tags:
date: 2026-05-19
---
## Gibbs free energy of water revisited
$$
\Psi=\Psi_g+\Psi_p+\Psi_{\Omega}+\Psi_m
$$
where, 
- $\Psi_g\rightarrow$ gravitational potential 
- $\Psi_p\rightarrow$ pressure potential (xylem)
- $\Psi_\Omega\rightarrow$ osmotic potential (cell)
- $\Psi_m \rightarrow$ matric potential (soil)

| Hydraulic Conductivity                                                                                    | Hydraulic conductance                                                                  |
| --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------- |
| It is an intrinsic property of the object's material no matter how the size of mass of the object changes | It is a property dependent on the object under question.                               |
| Example the conductivity of oak is the same                                                               | The same oak can have different conductance based on the measured location in the tree |
| Units: m/s                                                                                                | Units: m³/sPa                                                                          |

**Normalised hydraulic conductance (m/sPa)**
It is the the hydraulic conductance normalised to the sapwood area or total leaf area. 

## Ohm's Law Analogy 
![[../Files/Pasted image 20260721174453.png|center|350]]
The **Ohm's-law analogy** makes the SPAC tractable: flow is driving force divided by resistance, with water potential difference playing the role of voltage and sap flow the role of current.
$$
Q= \overbrace{K(\Psi)\,\Delta\Psi}^{\substack{\text{Darcy's
  law}\\\text{analogy}}}=\underbrace{\frac{1}{R(\Psi)}\Delta \Psi }_{\substack{\text{Ohm's
law}\\\text{analogy}}}
$$
- **Resistance acts in series:** along the pathway soil → root → stem → leaf. Water must cross every step, so the resistances add.
- **Conductance acts in parallel:** within a segment the many conduits side by side in a stem. Their conductances add.


## Consequences
**Resistance**
In series the largest resistance controls the whole flow. One bottleneck anywhere in the chain limits the entire plant, no matter how good the other segments are. This is why drought is dangerous from two directions at once: drying soil raises $R_{RS}$ (soil–root), while embolism raises $R_P$ (plant, via PLC). It is also the basis of *hydraulic segmentation* cheap, replaceable organs like leaves are built as the high-resistance link, so they fail first and protect the expensive stem.
**Conductance**
The parallel arrangement enables redundancy. Losing a few conduits to embolism only removes a few parallel paths, so conductance drops gradually rather than collapsing as a whole.
