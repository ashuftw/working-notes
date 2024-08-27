---
title: Strategy Pattern
draft: false
tags:
---
   
## Definition 
It is a behavioural pattern that encapsulates each algorithm in a family of algorithms being used in a program. The encapsulation allows the program to chose any of the algorithms without having to modify the code used in the algorithm.

## GoF Template
![[Pasted image 20230816164023.png]]
1. **Strategy:** This is an interface or abstract base class that defines a family of interchangeable algorithms.
    
2. **Concrete Strategies:** These are the concrete implementations of the strategies, each providing a specific algorithm.
    
3. **Context:** This holds a reference to a strategy object and uses it to perform a certain task. The context can switch between different strategies dynamically.


