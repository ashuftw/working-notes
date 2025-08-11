---
title: Divide and Conquer Approach
draft: true
tags: 
date: 2025-08-04
---
Instead of having one Master that is responsible for communication. One can divide the communication load by having a communicator-worker pair. At the end of each step the number of processes is halved. Note: All the ranks perform work, but they are merely accumulated in the each individual master. 
![[../Files/Pasted image 20250805170918.png|center|500]]
You are given the following serial C++ program (`main_serial.cpp`) that calculates an approximation of pi by performing numerical integration of a quarter circle.

[[250805 Serial Program to Numerically Approximate Pi|Serial Program to Numerically Approximate Pi]]

```cpp
#include <mpi.h>
// ... other necessary includes and helper functions like integral() are defined elsewhere ...

int main(int argc, char **argv)
{
    // --- MPI and variable setup ---
    int number_of_processes;
    int my_rank;
    MPI_Init(&argc,&argv);
    MPI_Comm_rank(MPI_COMM_WORLD,&my_rank);
    MPI_Comm_size(MPI_COMM_WORLD,&number_of_processes);

    double result = 0.0;
    double local_integral = 0.0;
    const long number_of_intervals = 5040 * 100000;
    const double global_a = 0.0;
    const double global_b = 1.0;

    // --- Local Calculation ---
    // Each process calculates its portion of the integral
    const long local_number_of_intervals = number_of_intervals / number_of_processes;
    const double local_interval_width = (global_b - global_a) / (double)number_of_processes;
    const double local_a = global_a + my_rank * local_interval_width;
    const double local_b = local_a + local_interval_width;
    local_integral = integral(local_a, local_b, local_number_of_intervals);

    result += local_integral; // Each process starts with its own result

    // --- Aggregation: Your code goes here! ---
    //
    // Implement the Divide and Conquer (tree-based) communication pattern
    // using MPI_Send and MPI_Recv to combine the 'result' from all
    // processes onto rank 0.
    //


    // --- Final Output ---
    if (my_rank == 0)
    {
        // ... code to print the final result and error ...
    }
    MPI_Finalize();
    return 0;
}
```
## Solution
```cpp
MPI_Status status;
double receive_buffer;

// --- Divide and Conquer Communication ---

// Receiving loop for processes that act as communicators
for(int offset = 1; (offset < number_of_processes-my_rank) && (my_rank % (offset * 2) == 0); offset *= 2)
{
    MPI_Recv(&receive_buffer, 1, MPI_DOUBLE, my_rank + offset, 0, MPI_COMM_WORLD, &status);
    result += receive_buffer;
}

// Sending logic for processes that act as workers
if (my_rank != 0)
{
    int offset = 1;
    while (my_rank % (offset * 2) == 0)
    {
	    offset *= 2;
    }
    MPI_Send(&result, 1, MPI_DOUBLE, my_rank - offset, 0, MPI_COMM_WORLD);
}
```