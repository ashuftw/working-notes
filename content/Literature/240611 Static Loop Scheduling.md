---
title: Static Loop Scheduling
draft: false
tags:
---
## 1. Blocking
**Blocking (Chunk Scheduling)** is a common static scheduling strategy where the outer iterations are divided into contiguous chunks (blocks) and assigned to a processor.

**How it works:**
- Divide the total number of iterations into fixed-size chunks.
- Assign each chunk to a different processor.
- Outer Loop is parallelized

**Example:** If you have 100 iterations and 4 processors, each processor gets a block of 25 consecutive iterations.
![[Pasted image 20240621121105.png|center]]
Where, 
 - `numProcesses` -> Total number of Processors in the Machine.
 - `N` -> Total number of iterations to be performed. 
- `For Parallel` (Pseudocode) just means that the `for` loop is executed in parallel. 
## 2. Tiling
**Tiling (Cyclic Scheduling)** distributes loop iterations i(inner loop), ensuring that each processor gets iterations spread throughout the loop.

**How it works:**

- Divide the iterations into tiles.
- Assign iterations to processors in a cyclic manner, such that each processor gets every $n-$th iteration (where $n$ is the number of processors).
- Inner loop is parallelized. 

**Example:** If you have 100 iterations and 4 processors, Processor 0 gets iterations 0, 4, 8, 12, ..., Processor 1 gets iterations 1, 5, 9, 13, ..., and so on.
![[Pasted image 20240621122602.png|center]]

*In tiling the vector size is equal to tile size.*

> **Note**: Blocking is used in *Distributed Memory Parallelization (MPI)*. Tiling is used in *Vector Parallelization.*



