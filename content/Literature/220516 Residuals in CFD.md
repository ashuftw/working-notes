May 2022
  

Tags: [[CFD]]

# Residuals in CFD

- CFD codes use iterative approach to solve the solution matrix. 
- Consider a CFD solution of [[Heat conduction in a 1D bar without a heat source]].
	![[Pasted image 20220516165644.png|center|750]]
-  The solution matrix for a bar with 5 cells
	 ![[Pasted image 20220516171108.png|center|300]]
	 
$$
AT=B
$$
$A\rightarrow$ Heat flux gradient, $T\rightarrow$ Temperature & $B\rightarrow$ Heat source
- The Matrix equation for residual is defined as
	 ![[Pasted image 20220516172618.png|center|500]]
$$
AT-B=r
$$

- Once the Temperature field is calculated, each value can be substituted and the residuals can be obtained. 
- As $r\rightarrow 0$, the solution gets more accurate.
- From the matrix definition, the residual is vector give the local error in each cell. 
- Note that the residual has the same units as the quantity calculated by the solution algorithm.
- In general ![[Pasted image 20220516173700.png|center|750]]  
**Representative residual**
- Since the residual vector contains the error for every cell in the mesh, it is not feasible to monitor it against iteration. A representative residual is a scalar that represents the residual for all the cells in the mesh. 
- The three norms in calculating the residuals are as follows:
	- **$L_1$ norm:** It's the mean of all the residuals components 
$$
r=\frac{1}{N}\sum_{i=0}^n |r_i|
$$

		- This norm has no bias.
	- $L_2$ **norm:** Mean magnitude of all the components of the residual vector $\approx$ **RMS** 
$$
r=\left(\frac{1}{N}\sum_{i=0}^n |r_i|^2\right)^{1/2}
$$
 
		- A property of this norm is that it has a bias towards large values. So if you have a solution with a few bad cells, the effect of it on the representative residual is magnified.
	- $L_\infty$ **norm:** Takes the maxima of the residual vector 
$$
r=\text{max}|r_i|
$$

-    
---
# References
1. https://www.youtube.com/watch?v=v9OnNeYH4Ok&
2. 