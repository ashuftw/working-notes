---
title: C++ Threads & OmpenMP
draft: false
tags: 
date: 2025-08-06
---
### What is a C++ thread?
A C++ thread represents a single thread of execution, allowing multiple functions to run concurrently. It is part of the C++ Standard Library and requires the `<thread>` header.

### How do you create and manage a C++ thread?
You can create a thread by declaring a `std::thread` object and passing a function to its constructor. The `join()` method is used to make the main thread wait for the created thread to finish its execution.

### What is a race condition?
A race condition occurs when multiple threads "race" to access and manipulate a shared variable, and the final result depends on the unpredictable order in which the threads' operations are executed.
```cpp
#include <iostream>
#include <thread>
#include <vector>

// Function where threads will race to increment the counter
void increment_counter() {
    for (int i = 0; i < 100000; ++i) {
        // RACE CONDITION: Multiple threads read and write to 'counter'
        // without synchronization, leading to lost updates.
        counter++;
    }
}

int main() {
    // Create two threads that run the same function
	int counter = 0;
    std::thread t1(increment_counter, std::ref(counter));
    std::thread t2(increment_counter, std::ref(counter));

    // Wait for both to finish
    if(t1.joinable) t1.join();
    if(t2.joinable) t2.join();

    // The final result will be unpredictable and less than 200000
    std::cout << "Final counter value: " << counter << std::endl;
    return 0;
}
```

### What is a mutex and how is it used to prevent race conditions?
A mutex (**mutual exclusion**) is a mechanism that blocks access to a shared resource. A thread acquires a lock on the mutex (`mtx.lock()`) before accessing the shared resource and releases the lock (`mtx.unlock()`) afterward, ensuring that only one thread can access the resource at a time.

```cpp
#include <mutex>

std::mutex mtx;
void increment(int& counter) {
    for (int i = 0; i < 100000; ++i) {
        mtx.lock();
        counter = counter + 1;
        mtx.unlock();
    }
}
// ... rest of the main function is the same


```
### What is an atomic operation and how is it used to prevent race conditions?
An atomic operation is a hardware-supported, thread-safe operation. Operations on atomic variables are indivisible and cannot be interrupted by other threads, thus avoiding race conditions.

```cpp
#include <atomic>

// function that increments a shared counter from a thread.
void increment(std::atomic<int>& counter) { // & implies that we refer the original counter, not a copy
    for (int i = 0; i < 100000; ++i) {
        counter++; // This is now an atomic operation
    }
}

int main() {
    std::atomic<int> counter(0); // Shared atomic integer initialized to 0 
    std::thread t1(increment, std::ref(counter));
    std::thread t2(increment, std::ref(counter));
    t1.join(); // wait till thread 't1' has finished its execution.
    t2.join(); 
    std::cout << "Counter value: " << counter << std::endl;
    return 0;
}
```
### Which is generally faster, a mutex or an atomic operation?
Atomic operations are usually faster than mutexes for preventing race conditions.

### Why are memory access patterns important for performance in multi-threaded applications?
The way threads access data in memory can significantly impact performance. Access patterns that lead to fewer cache misses are more efficient. When multiple threads access memory in a scattered way, it can cause cache misses and slow down the program.

### How can you map threads to data to improve memory access patterns?
You can map threads to data in a way that minimizes cache misses. For example, in a 2D grid, having each thread process a contiguous block of data can be more efficient than having threads access scattered elements.

### What is OpenMP?
OpenMP is an API for multi-platform shared-memory parallel programming in C/C++ and Fortran. It uses compiler directives to mark code that should be run in parallel.

### How do you use OpenMP to parallelize a `for` loop?
You can use the `#pragma omp parallel for` directive before a `for` loop to instruct the compiler to parallelize its execution. You may also need to specify how variables are shared or kept private among threads using clauses like `default(shared)` and `private(var_list)`.

### What is an important environment variable to set when using OpenMP?
You should set the `OMP_NUM_THREADS` environment variable to specify the number of threads you want to use.

### In OpenMP, what is the difference between `shared` and `private` variables in a parallel loop? 
- **`shared`**: There is only one instance of the variable, and all threads see and can modify it (risk of race conditions!).    
- **`private`**: Each thread gets its own private copy of the variable. Changes made by one thread are not visible to others.
```cpp
int shared_variable = 100;
int private_variable = 0;

#pragma omp parallel for private(private_variable) shared(shared_variable)
for (int i = 0; i < 10; ++i) {
    // Inside this loop:
    // - There is only ONE 'shared_variable'. All threads access and modify the same one.
    // - Each thread gets its OWN 'private_variable'. Changes here are not seen by other threads.
}
```
### How do you safely perform a sum (or other reduction operations like product, max, min) on a shared variable in an OpenMP parallel loop?
```cpp
#pragma omp parallel for reduction(+:result)
// The '+' indicates summation.
```