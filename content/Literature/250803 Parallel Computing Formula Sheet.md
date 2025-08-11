---
title: Parallel Computing Formula Sheet
draft: true
tags: 
date: 2025-08-03
---
## 1. Performance Metrics

### Speedup

$S = \frac{T_{sequential}}{T_{parallel}} = \frac{T_s}{T_p}$

### Amdahl's Law

$S = \frac{s + p}{s + \frac{p}{N}}$

Where:

- $s$ = serial fraction
- $p$ = parallel fraction
- $N$ = number of processors
- Note: $s + p = 1$

### Master-Slave Scalability Issue

When $s = O(N^{-1})$: $S = \frac{O(N^{-1}) + p}{O(N^{-1}) + \frac{p}{N}} = O(N^{-1})$

### Efficiency

$E = \frac{S}{N} = \frac{T_s}{N \cdot T_p}$

### Strong Scaling

- Fixed total problem size
- Measure speedup as processors increase

### Weak Scaling

- Problem size increases proportionally with processors
- Ideal: constant execution time
- Measure efficiency as problem and processors scale

### Total Time with Latency & Bandwidth

$T_{total} = Latency + \frac{Data\ Size}{Bandwidth}$

For multiple messages: $T_{multiple} = n \cdot Latency + \frac{Total\ Data}{Bandwidth}$

For single consolidated message: $T_{single} = Latency + \frac{Total\ Data}{Bandwidth}$

## 2. Network Topologies

### Hypercube Properties

- Degree = $d$ (for $d$-dimensional hypercube)
- Number of nodes = $2^d$
- Diameter = $d$
- Each node has $d$ neighbors

### Hypercube Distance

- Distance = number of bit positions that differ (Hamming distance)
- Example: `01101111` to `01011100`
    - XOR: `00110011` → 4 bits differ → distance = 4

### Path in Hypercube

- Flip one differing bit at a time to create shortest path

### Network Diameter

- Maximum distance between any two nodes in the network
- Minimum number of hops needed in worst case

## 3. Arithmetic Intensity

### Definition

$$Arithmetic\ Intensity = \frac{FLOPS}{Memory\ Bytes\ Transferred}$$

### Matrix-Vector Multiplication (m×n matrix × n×1 vector)

- FLOPS = $m \times n$ multiplications + $m \times (n-1)$ additions = $m \times (2n-1)$
- Memory transfers = $m \times n$ matrix elements + $n$ vector elements + $m$ result elements
- For single precision float (4 bytes):
    - Memory = $4 \times (m \times n + n + m)$ bytes

### Example: 8×8 matrix × 8×1 vector

- FLOPS = $8 \times 8 + 8 \times 7 = 64 + 56 = 120$ operations
- Memory = $4 \times (64 + 8 + 8) = 320$ bytes
- Arithmetic Intensity = $\frac{120}{320} = 0.375$

## 4. Matrix Operations

### Row-Major Matrix Access

For matrix element $a_{ij}$ in row-major storage: $$Index = i \times N + j$$

Where $N$ is the number of columns

### Matrix Multiplication Formula

$$c_{ij} = \sum_{k=1}^{N} a_{ik} \cdot b_{kj}$$

In code: `C[i*N+j] = Sum(A[i*N+k]*B[k*N+j], k=0,N-1)`

## 5. Memory & Cache

### Memory Access Time

- Fast index should match data layout
- Row-major (C/C++): iterate over last index fastest
- Column-major (Fortran/MATLAB): iterate over first index fastest

### Cache Miss Penalty

- L1 cache: ~4 cycles
- L2 cache: ~10 cycles
- L3 cache: ~40 cycles
- Main memory: ~100-300 cycles

## 6. MPI Communication

### Blocking Communication Time

$$T_{comm} = Latency + \frac{Message\ Size}{Bandwidth}$$

### Non-blocking Communication

- Can overlap computation with communication
- Total time = $\max(T_{computation}, T_{communication})$

### Collective Operations Complexity

- Broadcast: $O(\log N)$
- Scatter/Gather: $O(N)$ for master-slave, $O(\log N)$ for tree-based
- Reduce: $O(\log N)$ for tree-based

## 7. Divide & Conquer vs Master-Slave

### Master-Slave

- Master receives from $N-1$ slaves
- Time complexity: $O(N)$

### Divide & Conquer (Tree)

- Each node receives from at most $\log_2(N)$ nodes
- Time complexity: $O(\log N)$

## 8. Peak Performance

### Theoretical Peak FLOPS

$$Peak\ FLOPS = Cores \times Clock\ Speed \times Operations\ per\ Cycle$$

For vectorized operations: $$Peak\ FLOPS = Cores \times Clock\ Speed \times Vector\ Width \times 2$$

(Factor of 2 for FMA - Fused Multiply-Add)

### Phoenix Cluster Example

- CPU: 2 × Intel Xeon (10 cores each) × 2.4 GHz
- Peak = $20 \times 2.4 \times 10^9 \times Vector\ Width \times 2$ FLOPS

## 9. Bandwidth Limit

### Definition

A calculation is bandwidth-limited when: $$\frac{Peak\ FLOPS}{Peak\ Memory\ Bandwidth} > Arithmetic\ Intensity$$

### When Bandwidth Dominates

- Low arithmetic intensity operations
- Large data sets that don't fit in cache
- Streaming applications

## 10. SIMD Execution

### Conditional Execution in SIMD

- Both branches are executed
- Results are masked based on condition
- Performance = time of longest branch

### Example

```
if (condition) {
    // Path A: 5 operations
} else {
    // Path B: 3 operations  
}
```

SIMD time = 5 operations (maximum of both paths)

## 11. Common Constants

### Data Type Sizes

- `float`: 4 bytes
- `double`: 8 bytes
- `int`: 4 bytes (typically)

### Common Latencies (approximate)

- Network latency: ~1 μs
- Memory latency: ~100 ns
- Cache latency: ~1-10 ns

### Common Bandwidths

- Network: ~1-100 GB/s
- Memory: ~10-100 GB/s
- Cache: ~100-1000 GB/s

## 12. Pi Calculation (Numerical Integration)

### Sequential Version

$\frac{\pi}{4} \approx \frac{1}{N} \sum_{i=0}^{N-1} \sqrt{1 - \left(\frac{i + 0.5}{N}\right)^2}$

### Parallel Version (R processes)

$\frac{\pi}{4} \approx \frac{1}{N} \sum_{r=0}^{R-1} \sum_{i=r \cdot \frac{N}{R}}^{(r+1) \cdot \frac{N}{R} - 1} \sqrt{1 - \left(\frac{i + 0.5}{N}\right)^2}$

Where:

- $N$ = total number of intervals
- $R$ = number of processes
- Each process computes $\frac{N}{R}$ intervals

## 13. Ghost Layers / Halo Exchange

### Communication Pattern for 2D Domain Decomposition

1. Even ranks exchange with right, odd with left
2. Even ranks exchange with left, odd with right
3. Even ranks exchange with bottom, odd with top
4. Even ranks exchange with top, odd with bottom

### Computation Order

1. Compute interior nodes (independent of ghost layers)
2. Exchange ghost layer data
3. Compute boundary nodes (dependent on ghost layers)

## 14. CUDA Programming

### Thread Indexing

Global thread index in 1D: $index = blockIdx.x \times blockDim.x + threadIdx.x$

Global thread index in 2D: $i = blockIdx.x \times blockDim.x + threadIdx.x$ $j = blockIdx.y \times blockDim.y + threadIdx.y$

### CUDA Limits

- Max threads per block: 1024
- Max blocks in grid: $2^{31}-1$ (65535 per dimension)
- Warp size: 32 threads (fixed)
- Z-dimension limited to 64 threads

### Kernel Launch

```cuda
function<<<numBlocks, threadsPerBlock>>>(args);
```

### Warp Divergence

- All 32 threads in a warp execute together
- Branching serializes execution
- Time = max(time of all branches)

## 15. Synchronization Concepts

### Mutex (Mutual Exclusion)

- Ensures only one thread accesses critical section
- Operations: lock(), unlock()
- More expensive than atomics

### Atomic Operations

- Indivisible operations on shared memory
- Examples: atomic_add, atomic_compare_exchange
- Generally faster than mutex for simple operations

### Race Condition Avoidance

1. **Mutex/Locks** - serializes access to critical section
2. **Atomic operations** - for simple read-modify-write
3. **Lock-free algorithms** - using atomic operations
4. **Thread-local storage** - avoid sharing when possible

## 16. Memory Architecture

### NUMA (Non-Uniform Memory Access)

- Multiple processors with local memory
- Access to local memory is faster
- Access to remote memory is slower
- Important for thread/process placement

### Memory Hierarchy Performance

- Register: ~1 cycle
- L1 cache: ~4 cycles
- L2 cache: ~10 cycles
- L3 cache: ~40 cycles
- Main memory: ~100-300 cycles
- Remote NUMA memory: ~300-500 cycles

## Quick Reference for Exam Problems

1. **Speedup calculation**: Always check if problem is embarrassingly parallel or has dependencies
2. **Network transfers**: Count number of messages × latency + total data/bandwidth
3. **Arithmetic intensity**: Count all operations and all memory transfers separately
4. **Hypercube paths**: Use XOR to find differing bits, flip one at a time
5. **Master-slave bottleneck**: Serial portion grows with number of workers
6. **Cache optimization**: Keep working set within cache size, access memory sequentially
7. **Pi calculation**: Divide intervals equally among processes, sum partial results
8. **Ghost layers**: Overlap communication with computation of interior nodes
9. **CUDA indexing**: Always use `blockIdx*blockDim + threadIdx`
10. **Warp divergence**: Time = longest branch path
11. **Strong vs Weak scaling**: Strong = fixed problem size, Weak = scaled problem size
12. **SIMD conditionals**: Both branches execute, results are masked