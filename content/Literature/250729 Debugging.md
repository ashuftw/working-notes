---
title: Debugging
draft: true
tags: 
date:
---
What is a bug?
---
A bug is a problem or error in a program that causes it to produce unintended results, behave incorrectly, or crash entirely.

***

What are the different kinds of errors and when are they easy to deal with?
---
The two main types of errors are:
- **Syntax Errors**: These violate the rules of the programming language (e.g., a missing semicolon). They are **easy to deal with** because the compiler detects them automatically and points them out before the program can even run.
- **Semantic/Logic Errors**: These occur when the code is syntactically correct but does not perform the intended action (e.g., using `-` instead of `+`). They are **harder to deal with** because the compiler cannot detect them, requiring manual debugging to find the source of the incorrect logic.

***

What are the main debugging approaches?
---
There are two primary approaches to debugging:
1.  **Calling Output Functions**: Manually adding print statements (like `std::cout`) into the code to display the values of variables or to track the program's flow. This is simple but requires adding and removing code.
2.  **Using a Debugger**: Employing a dedicated program (like GDB) to observe the code's runtime behavior. A debugger allows you to pause the program at any point, step through the code line-by-line, and inspect the state of variables without changing the source code.

***

How do you use a GDB debugger?
---
To use the GNU Debugger (GDB), you follow a general process:
1.  **Compile with Debug Symbols**: Compile your code using the `-g` flag (e.g., `g++ -g -o main main.cpp`).
2.  **Start GDB**: Run the debugger on your compiled program (`gdb main`).
3.  **Set Breakpoints**: Tell the debugger where to pause execution using the `break` command (e.g., `break 12` or `break main`).
4.  **Run the Program**: Start the execution inside the debugger with the `run` command.
5.  **Control Execution**: Once paused at a breakpoint, you can step through the code line-by-line (`next` or `step`) or continue to the next breakpoint (`continue`).
6.  **Inspect Variables**: Check the value of any variable at any point with the `print` command (e.g., `print my_variable`).

***

What is profiling and what is Valgrind?
---
**Profiling** is a form of dynamic analysis that measures a program's runtime behavior, such as its memory usage, CPU utilization, and execution time. The goal is to identify performance bottlenecks and opportunities for optimization.

**Valgrind** is a popular open-source tool used for profiling. Its most common feature, **Memcheck**, is specifically used to detect memory-related errors, such as memory leaks, which occur when a program fails to free memory it no longer needs.