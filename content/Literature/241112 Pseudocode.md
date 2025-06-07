---
title: DAC Modeling Pseudocode
draft: true
tags: 
date: 2024-11-12
---

1. Initialize concentration field, adsorbed quantities, and parabolic velocity profile
2. For each timestep:
   - Calculate concentration changes due to advection and diffusion
	   - Update concentration  
	   - Calculate adsorption at walls and update boundary conditions
   - Apply inlet/outlet conditions
   - Prepare for next timestep by updating variables