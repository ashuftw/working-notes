Status: #finished 
[[230507 Quadrature]]
## Definition
![[Pasted image 20231130103848.png]]


|         | Quadrature   | Sampling Points  ($N+1$)    | Order $(N)$    | Degree of Correctness $K$|  
|     --- | ------------------  |   --   | ---              | -------------- | 
|**Newton-Cotes Formula**           | Left/Right Rectangle Rule| 1 |0 |0       | 
|         | Trapezoidal Rule   |  2   | 1                   | 1              |
|         | Simpson's Rule     | 3    | 2                   | 3              | 
|**Gauss-Legendere Rules**    | Midpoint Rule  | 1       | 0     | 1        | 

### Note for Newton-Cotes Formula
- **Even Sampling Points** -> Exactly Integrate up to an Order 1 less than the number of Sampling points. Ex: $2,4 \dots$ 
- **Odd Sampling Points** -> Exactly Integrates up to an Order equal to the number of Sampling points. Ex: $3, 5  \dots$

Questions I have 
- What is Order of Accuracy?
- What is K? 
- What is Number of Sampling points?
- Fill in the table properly
 

---
# References
- Griffith - Numerical Method for Engineers Pg. 247

