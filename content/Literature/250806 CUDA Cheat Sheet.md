---
title: CUDA Cheat Sheet
draft: true
tags: 
date: 2025-08-06
---
### In CUDA, what does the `<<<A, B>>>` syntax mean when launching a kernel?
- `A` -> number of blocks in the grid (Grid Dimension).
- `B` -> number of threads in each block (Block Dimension).
- **Total number of threads** launched is `A * B`.

### How do you launch a CUDA kernel to process a 1D array of `N` elements, assuming the kernel uses a simple index: 
```cpp 
int i = threadIdx.x;
```

Use one block with `N` threads.
```cpp
kernel_name<<<1, N>>>(...);
```


### What is `threadIdx.x` in a CUDA kernel?
It's a built-in variable that holds the **unique ID** of the **current thread** *within its block*. The IDs range from `0` to `(threads per block) - 1`.


### What is the standard formula to calculate a unique, global thread ID `i` in a 1D grid?
```cpp
int i = blockIdx.x * blockDim.x + threadIdx.x;
```
### What do the built-in variables `blockIdx.x` and `blockDim.x` represent in CUDA?
- `blockIdx.x`: The unique ID of the current thread's block.
- `blockDim.x`: The number of threads in a block (the value specified at launch).
![[../Files/Pasted image 20250806171223.png|center]]
[[private/Excalidraw/Drawing 2025-08-06 17.06.25.excalidraw.md#^group=mcBnDGKH5T919u4mpUy8j|source]]