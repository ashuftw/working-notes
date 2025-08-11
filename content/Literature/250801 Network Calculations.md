---
title: Network Calculations
draft: true
tags: 
date: 2025-08-01
---
## 6 Dimensional Hypercube
A parallel computing system is designed with a **6-dimensional hypercube network**.
*   a) How many compute nodes are there in this network?
*   b) What is the **degree** of each node in this network?
*   c) What is the **diameter** of this network?
*   d) Write down the shortest path between node **001010** and node **111000** in the format `xxxxxx → xxxxxxx → ⋯ → xxxxxxx`. Explain the principle used.
### Solution
-   a) **Number of nodes**:  
 Number of nodes $N =$ $2^D$ => $N = 2^6 = 64$ **nodes**.
-   b, c) **Degree & Diameter**: Dimension  = Degree = Diameter = $6$.
-   d) **Shortest path**: The distance between nodes in a hypercube is determined by the **Hamming distance**, which is the number of non-matching bits in their binary indices. A shortest path is achieved by changing **one bit at a time**.
    *   Node $1$: `001010`
    *   Node $2$: `111000`
    *   Differing bits (from left to right):
        *   Bit $0$: `0` vs `1`
        *   Bit $1$: `0` vs `1`
        *   Bit $4$: `1` vs `0`
    *   The Hamming distance is 3. A possible shortest path is:
        `001010 → 101010 → 111010 → 111000`
        (This path sequentially flips the first, second, and fourth bits from the left, aligning with the principle of changing one bit at a time).
## 8 Dimensional Hypercube
A network is organized in an 8-dimensional hypercube. Each node is indexed according to its position. 
- a) How long is the shortest path between the nodes `01101111` and `01011100`? 
- b) Write down the path in the format `01101111 → xxxxxxxx → ⋯ → 010111100`.
### Solution
We need to Find the [[250801 Hamming Distance|Hamming Distance]]. 
Comparing given node indices to find the differing bits:
*   Node 1: `01101111`
*   Node 2: `01011100`

Comparing each bit from left to right:
*   Bit 0: `0` vs `0` (Match)
*   Bit 1: `1` vs `1` (Match)
*   **Bit 2: `1` vs `0` (Difference)**
*   **Bit 3: `0` vs `1` (Difference)**
*   Bit 4: `1` vs `1` (Match)
*   Bit 5: `1` vs `1` (Match)
*   **Bit 6: `1` vs `0` (Difference)**
*   **Bit 7: `1` vs `0` (Difference)**

There are **4 differing bits**. Therefore, the Hamming distance is 4, and the **shortest path length is 4**.
A possible shortest path, obtained by flipping one differing bit at a time, is:
`01101111 → 01001111 → 01011111 → 01011101 → 01011100` 