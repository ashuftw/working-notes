  
## Use case 
It is used to improve the accuracy of a Numerical Method to a higher order by combining results from different step sizes.  
## Mathematically 

$$
\boxed{
A_e=\frac{2^k\left[A(h / 2)-A(h)\right]}{2^k-1}
}
$$


Here, 
- $k\rightarrow$is the order of convergence. 

> Note: The $k$ is increased by two for every iteration. 
> ![[Pasted image 20240709121917.png]]

| Quadrature Method | Order of Convergence |
| ----------------- | -------------------- |
| Left Hand Rule    | $O(h)$               |
| Midpoint Rule     | $O(h^2)$             |
| Trapezoidal Rule  | $O(h^2)$             |
| Simpson's Rule    | $O(h^4)$             |
