  
## Objective
![[Pasted image 20240221153015.png]]

- Key step is to identify the reference frame velocity $V_\text{RF}$  . 
- The Droplet Velocity $V_d$ gradually approaches to zero i.e the Moving reference frame is caught up to it's position. 
- The "correction" of the MRF is achieved through the use of a feedback loop to reduce the error. 

## Step 1: Find the Center of the Droplet (copy from BubbleInterTrackFoam line 72, 96  Create Bubble.H)
**Position of the Droplet**[^1]

$$
\begin{align}
\text{Centroid}&=\frac{\text{Volume of Droplet Weighted with the Position Vector}}{\text{Volume of the Droplet}}\\
x_{\mathrm{d}}(t)&=\frac{\int_{\Omega} x \alpha(\mathbf{x}, t) \mathrm{d} V}{\int_{\Omega} \alpha(\mathbf{x}, t) \mathrm{d} V}
\end{align}
$$

Where $x$ is the position vector

## Step 2 Calculate the Reference frame velocity required to center the droplet ($x_d(t) =0$)
**Corrected Position of droplet** 

$$
x_{\mathrm{d}}(t)=x_{\mathrm{d}}(0)+\int_0^t\left(v_{\mathrm{d}}-v_{\mathrm{RF}}\right) \mathrm{d} t
$$

**Error in each time step**: Maybe having error zero in first try isn't ideal. 

$$
e_x(t)=x_{\mathrm{d}}(t)-x^{\mathrm{SP}}
$$

where $x^{SP}$ is the position of the domain's center .
## Step 3 Update Wall Condition
Subtract the Inlet velocity with the velocity of the reference frame. So that the newly adjusted input velocity along with the reference velocity will give the physical velocity. 
> Note: We have a steady simulation input boundary. So the Reference Velocity will always be lesser than or equal to the input velocity. 

## Step 4 

---
# References
[^1]: https://eng.libretexts.org/Bookshelves/Mechanical_Engineering/Mechanics_Map_(Moore_et_al.)/17%3A_Appendix_2_-_Moment_Integrals/17.2%3A_Centroids_of_Areas_via_Integration
