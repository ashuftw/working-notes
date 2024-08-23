Status: #finished  
## Parallel Computing
### Limiting factors 
- Data dependencies => Can force you to do some task sequentially. 
- Start-up 
- Bottlenecks: access to shared / slow resources. 
- Communication
- Resources required for management. 
### Q1: How much faster can a problem be solved using $N$ cores instead of 1. 
### Strong Scaling 
- Constant Problem size, varying number of workers (cores)
	![[Pasted image 20240419095349.png]]
- However, A compute Problem in reality
![[Pasted image 20240419100237.png]]
- **Serial Compute time**
	$T_s=S+P$
- **Parallel Compute time**
	$T_P=S+\frac P N$
- **Andahl's Law** for Speed-up (under *Strong Scaling*)
	![[Pasted image 20240425162157.png]]
	
### Q2: How much more work can be done in parallel instead of in serial. 
![[Pasted image 20240419102240.png]]

## Roofline Model
![[Pasted image 20240419103039.png]]
### Q3: How fast can a task be executed? 
![[Pasted image 20240419113154.png]]
### Roofline Graph
![[Pasted image 20240419113228.png]]
![[Pasted image 20240419113243.png]]
![[Pasted image 20240419113301.png]]
![[Pasted image 20240419113322.png]]
![[Pasted image 20240419113334.png]]
![[Pasted image 20240419113348.png]]
![[Pasted image 20240419113359.png]]
![[lecture-3_annotated.png]]
![[Pasted image 20240419113446.png]]
---
# References
