---
title: Networks Problem Set
draft: true
tags: 
date:
---
### 3. Latency and Bandwidth Calculation (10 Points)
Consider a data transfer scenario between two processes on a distributed system. The network has a **latency of 5 microseconds** and a **bandwidth of 2 Gigabytes per second**.
*   a) If a single 1 MB message is transferred, how long will it take?
*   b) If 10 separate 1 MB messages are transferred sequentially (one after another), what is the total transfer time?
*   c) If all 10 MB of data are collected and sent as one single 10 MB message, how long will the transfer take?
*   Explain the difference in results between b) and c).
Briefly compare a **Linear network** and a **Ring (1D Torus) network** with N nodes, in terms of their **diameter** and **number of connections**.
### Solution
*   a) **Single 1 MB message**:
    *   1 MB = 1,048,576 bytes.
    *   Bandwidth = 2 GB/s = 2 * 1024 * 1024 * 1024 bytes/s = 2,147,483,648 bytes/s.
    *   Time for data transfer = (1,048,576 bytes) / (2,147,483,648 bytes/s) ≈ 0.00048828 seconds = 488.28 microseconds.
    *   Total time = Latency + Data Transfer Time = 5 µs + 488.28 µs = **493.28 microseconds**.
*   b) **10 separate 1 MB messages**:
    *   Each message takes 493.28 µs (from part a).
    *   Total time = 10 messages * 493.28 µs/message = **4932.8 microseconds** (or approximately 4.93 milliseconds).
*   c) **One single 10 MB message**:
    *   Total size = 10 MB = 10 * 1,048,576 bytes = 10,485,760 bytes.
    *   Time for data transfer = (10,485,760 bytes) / (2,147,483,648 bytes/s) ≈ 0.00488281 seconds = 4882.81 microseconds.
    *   Total time = Latency + Data Transfer Time = 5 µs + 4882.81 µs = **4887.81 microseconds** (or approximately 4.89 milliseconds).
*   **Explanation**: The key difference between scenarios b) and c) lies in the impact of **latency**. Latency represents the fixed overhead incurred for initiating each communication event.
    *   In scenario b), the 5 µs latency is incurred for **each of the 10 individual messages**, leading to a cumulative latency overhead of 10 * 5 µs = 50 µs.
    *   In scenario c), the data is aggregated into a **single large message**, so the 5 µs latency is only incurred **once**.
    *   This demonstrates that **collecting data and sending it in fewer, larger transfers can significantly reduce the overall transfer time** by minimizing the impact of latency overhead, especially when dealing with many small messages where latency can dominate the transfer time.

## Bandwidth and Latency
 Your network is said to have a latency of one microsecond and a bandwidth of 1 Gigabyte per second. The total time of transferring 16 buffers of identical length between the same two processes takes 30 microsecond. How long will the transfer take if all data is collected and sent in one event? 
### Solution 
The total time for a data transfer is the sum of **latency** and the time taken to transfer the **data size over bandwidth**.

1.  **Determine Data Transfer Time Per Buffer:**
    -   Given: Latency, $L = 1 \micro \text s$, $16$ individual buffers take $30 \micro \text s$.
    -   For $16$ individual transfers, each incurs latency: $$16 * (L + T_\text{data per buffer}) = 30 \micro \text s$$
    -   Substituting $L = 1 \micro \text s$: $$T_\text{data per buffer} = 0.875 \text s$$ .

2.  **Calculate Total Time for One Event:**
    *   If all data is sent in one event, latency is incurred only once.
    *   Total data transfer time for 16 buffers = $$16 * T_\text{data per buffer} = 16 * 0.875 \micro \text s = 14 \micro \text s$$
    *   **Total Time (one event) = Latency + Total Data Transfer Time** $= 15\micro \text s$