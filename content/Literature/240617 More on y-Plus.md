Status: #finished 
## Law of the Wall
![[Pasted image 20240617115457.png]]

### Viscous Sub-layer ($0<y^+<5$)
We know that the Turbulence at the wall is zero. Therefore regardless of what the flow is, away from the wall, there is always going to be a small layer next to the wall where the flow is laminar. The flow is viscous dominant, therefore linear.  

### Buffer Layer ($5<y^+<30$) 
Here the flow is cannot be said to be neither perfectly linear nor exponential. Therefore it is beneficial to use a (Wall) function to spit out the values that should be used at the edge of the Buffer Layer. 

### Log-Law region ($30<y^+ <300$)
Flow is majorly turbulent. Makes use of the Turbulence model selected in the simulation.

## Calculating Cell height
Formula for $y^+$ 

$$
y^{+} = \frac{y u_\tau}{\nu}
$$

Rearranging

$$
y=\frac{y^{+} \nu}{u_\tau}
$$

Given a kinematic viscosity $\nu=1 \times 10^{-5} \mathrm{~m}^2 / \mathrm{s}$ (typical for air), and $y^{+}=30$ :

$$
y=\frac{30 \times 1 \times 10^{-5}}{0.05}=0.006 \mathrm{~m}=6 \mathrm{~mm}
$$






---
# References
