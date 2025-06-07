---
title: Comparative Study of OpenFOAM Solvers on Separation Pattern and Separation Pattern Transition in Overexpanded Single Expansion Ramp Nozzle
authors: T. Yu, Y. Yu, Y. P. Mao, Y. L. Yang, S. L. Xu
year: 2023
tags:
  - 🔬Paper
draft: true
---
- **Aim**: Study flow separation in an expanding nozzle. 
- Both solvers where tested against experimental data. 
- For this particular case, sonicFoam is concluded to not be a good choice of a solver. 
- FLuent > rhoCentralFoam > sonicFoam in predicting the separation point
- Both solvers make accurate prediction the pressure at the walls.
- Both solvers make an early prediction of the separation. But rhoCentralFoam is better. 
- Structure of the shock was predicted accurately by both solvers.
- SonicFoam doesn't capture the pressure rise after the separation bubble. Hence it's not a good fit for the scenario. 
