---
title: Review and comparison of two OpenFOAM solvers - rhoCentralFoam and sonicFoam
draft: true
tags:
  - 🔬Paper
date: 2024-10-06
authors: Maria Laura Canteros, Jiří Polanský
---

## Introduction 
- Incompressible flow assumptions are valid for flows with [[Mach Number]] $< 0.3$
- However, for high speed flows the simplification leads to inaccurate representation of the flow physics. Example [^1]
- Paper aims to explain said solvers and compare the ISO 9300 case. 

## 1. rhoCentralFoam
- [[241006 Segregated Solution Algorithm|Segregated density solver]] for High Speed, Compressible flows. 
- Uses a density-based approach with explicit central schemes for convection and an operator-splitting method to handle viscous terms.[^3]
- Suitable for high-speed aerodynamic applications, considering transonic and supersonic flow [^2]
## 2. sonicFoam
- Segregated Solver that use the [[241006 PIMPLE Algorithm|PIMPLE Algorithm]]. 
- Pressure based approach
## Results 
- rhoCentralFoam is more senstive to the initial condition . 
- rhoCentralFoam captures a sharper shock wave. However the velocity field is very similar to sonicFoam.


[^1]: ISO 9300:2022, Measurement of Gas Flow by
[^2]: https://help.sim-flow.com/solvers/rho-central-foam
[^3]: [[Implementation of semi-discrete, non-staggered central schemes in a colocated, polyhedral, finite volume framework, for high-speed viscous flows]]