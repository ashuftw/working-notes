---
title: Parallel Computing Flashcards
draft: true
tags: 
date: 2025-07-28
---
What is the core idea of parallel computing?
---
Using more than one CPU core or computer to solve a problem, which leads to faster execution.

***

What are the two primary memory models in parallel computing?
---
1.  **Shared Memory**: Multiple processors (threads) share access to the same memory space. Best for parallelizing tasks on a single machine (intra-node).
2.  **Distributed Memory**: Each processor has its own private memory. They communicate by explicitly sending messages to each other. Best for tasks distributed across multiple machines in a cluster (inter-node).

***

What is OpenMP and what is it typically used for?
---
OpenMP (Open Multi-Processing) is an API for **shared-memory** programming. It is used to distribute tasks among the cores of a single node (**intra-node**) by adding simple compiler directives (pragmas) to the code, often to parallelize loops.

***

What is MPI and what is it typically used for?
---
MPI (Message Passing Interface) is a standard for **distributed-memory** programming. It's used for communication between different nodes in a cluster (**inter-node**) by passing messages. The programmer must explicitly specify how and when communication happens.

***

Can OpenMP and MPI be used together?
---
Yes, they can be combined in a hybrid model. MPI is used for communication between different nodes, and OpenMP is used to parallelize the workload across the cores within each single node.

***

What is "granularity" in parallel computing?
---
Granularity is the ratio of computation time to communication time.
- **High granularity (coarse-grained)**: A task involves a lot of computation and infrequent communication. This is generally more efficient.
- **Low granularity (fine-grained)**: A task involves little computation and frequent communication, which can lead to significant overhead.

***

What is an "embarrassingly parallel" problem?
---
A problem that can be easily split into parallel tasks that require minimal or no communication or dependency between them. This is the ideal scenario for parallelization.

***

What is an "inherently serial" problem?
---
A problem that cannot be effectively parallelized because its steps have sequential dependencies. The overhead required for communication would be greater than the benefit of parallelization.

***

What does Amdahl's Law tell us about parallelization?
---
It states that the maximum speedup of a program is limited by its serial (non-parallelizable) part. No matter how many processors you add, the program can never run faster than the time it takes to execute the serial portion.
> Note: Additional overhead for parallel execution due to initialization and communication between
processes

***

What is "scalability" and what is "ideal scaling"?
---
**Scalability** measures how a program's performance improves as the number of processors increases. **Ideal scaling** occurs when the speedup is directly proportional to the number of cores added (e.g., using 100 cores makes the program 100 times faster).

***

What are the main goals of load balancing in domain decomposition?
---
1.  **Equal Workload**: Ensure every processor has roughly the same amount of work to do, preventing some processors from being idle while others are still working.
2.  **Minimized Communication**: Minimize the boundary surface between sub-domains to reduce the amount of data that needs to be communicated between processors.

***

What is the primary parallelization strategy used in CFD solvers like OpenFOAM?
---
**Domain Decomposition**. The simulation mesh (domain) is divided into multiple sub-domains, and each processor is assigned one sub-domain to work on.

***

How does OpenFOAM handle parallel code execution?
---
It uses a communication layer (PStream) that allows the same solver code to run in both serial and parallel modes. Communication between processor boundaries is handled as a special type of boundary condition, hiding the parallel complexity from the top-level solver code.