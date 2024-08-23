May 2022
Status: #finished  

Tags: [[OpenFOAM]]

# Wedge Boundary condition

Wedge is different from the [symmetry boundary condition](https://www.simscale.com/docs/simulation-setup/boundary-conditions/symmetry/) in the sense that the wedge BC applies the Navier-Stokes equations in cylindrical coordinates whereas the latter applies in cartesian coordinates. One big advantage of wedge is that it allows for the rotational flow around the axis and this is possible only because the fluxes and normal components are not assumed as zero.



---
# References
- https://www.simscale.com/docs/simulation-setup/boundary-conditions/wedge/