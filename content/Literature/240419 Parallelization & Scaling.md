---
title: Parallelization & Scaling
draft: false
date: 2024-04-19
---
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
	![[../Files/Pasted image 20240419095349.png|center]]
- However, A compute Problem in reality
![[../Files/Pasted image 20240419100237.png|center]]
- **Serial Compute time**
	$T_s=S+P$
- **Parallel Compute time**
	$T_P=S+\frac P N$
- **Andahl's Law** for Speed-up (under *Strong Scaling*)
	![[../Files/Pasted image 20240425162157.png|center]]

### Q2: How much more work can be done in parallel instead of in serial. 

![[../Files/Pasted image 20240419102240.png|center]]

## Roofline Model

![[../Files/Pasted image 20240419103039.png|center]]

### Q3: How fast can a task be executed? 

![[../Files/Pasted image 20240419113154.png|center]]

### Roofline Model 

![[../Files/Pasted image 20240419113228.png|center]]

![[../Files/Pasted image 20240419113243.png|center]]

![[../Files/Pasted image 20240419113301.png|center]]

![[../Files/Pasted image 20240419113322.png|center]]

![[../Files/Pasted image 20240419113334.png|center]]

![[../Files/Pasted image 20240419113348.png|center]]

![[../Files/Pasted image 20240419113359.png|center]]

![[../Files/Pasted image 20240829125634.png]]

![[../Files/Pasted image 20240419113446.png|center]]