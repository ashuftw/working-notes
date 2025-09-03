---
title: Supervised non-Parametric Estimation
draft: false
tags: 
date: 2025-08-15
---
Supervised non-Parametric Estimation is a way to determine the probability distribution of different classes of data without assuming a predefined shape for that distribution, like a bell curve.The two main techniques for non-parametric probability density estimation are:
1.  [[250815 Kernel-Based Method for Supervised non-Parametric Estimation (Parzen Windows)|Kernel-Based Method]] (or Parzen Windows).
2.  [[250815 k-Nearest-Neighbor Estimation|k-Nearest-Neighbor (k-NN) Estimation]]

## Key-Differences
-   **Kernel-Based Method**:
    -   **Fixed**: The volume $V_T$ of the region is fixed (though it's a function of the total sample size T).
    -   **Data-Dependent**: The number of samples $k_T$ within the volume depends on the local density of the data.

-   **k-Nearest-Neighbor (k-NN) Method**:
    -   **Fixed**: The number of samples $k_T$ to be considered is fixed.
    -   **Data-Dependent**: The volume $V_T$ of the region expands or contracts to enclose exactly $k_T$ samples, thus depending on the local data density.