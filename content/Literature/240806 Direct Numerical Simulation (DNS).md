---
title: Direct Numerical Simulation (DNS)
draft: false
date: 2024-08-06
---

## Use case
It a Method of Turbulence Modeling where are all the Turbulent scales are resolved directly i.e, without averaging or using a turbulence model. 
## Requirements
- Mesh and Time resolution should be in the dissipative scale. 
- Very High order schemes with super-low-dissipation
- Proper boundary conditions that supply instabilities. 
- Large spatial and temporal domain that doesn't constrain the development of Turbulence.
## Effects of a Coarse mesh
![[../../Private/Excalidraw/Drawing 2024-08-07 12.11.52.excalidraw#^group=G90mDwXiWDqobDEIEoROX|center|700]]
- The smaller eddies in the Dissipative scale are not simulated. 
- This means that the Energy dissipation occurs at a smallest *simulated scale* (which given the mesh is bigger than the dissipative scale). 
- Thus the bigger vortices rotate faster than normal to accommodate for this. This is non-physical and creates numerical instabilities. 

