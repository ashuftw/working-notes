---
title: strainRateFunction
draft: false
date: 2022-05-20
---

May 2022
   

Tags: [[OpenFOAM]] [[Viscosity model]]

# 220520 strainRateFunction
The viscosity is modeled as a function of strain rate.

> transportModel  strainRateFunction;  
    strainRateFunctionCoeffs  
    {  
        function polynomial ((a b) (c d));  
    }

Corresponds to
$$
\nu=a\times \dot \gamma^{b}+c\times \dot \gamma^{d}
$$




---
# References
1. https://cfd.direct/openfoam/user-guide/v7-boundaries#x25-1840005.2.3.4
2. https://cfd.direct/openfoam/user-guide/v7-boundaries#x25-1840005.2.3.4