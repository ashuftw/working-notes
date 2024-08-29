---
title: Interface Segregation Principle
draft: false
tags:
---
  
## Definition 
In a program having multiple sub-classes, each sub-class should be exposed only to the information or functionality that it requires from the super-class. This is achieved by creating a unique interface between two. 

Thus when one of the sub-classes requires a new functionality, the remaining sub-classes don't need to be updated. 

Note: ISP is an instance of [[230613 Dependency Inversion Principle|Dependency Inversion]].

## Example 
![[Pasted image 20230802175947.png|center]]
![[Pasted image 20230802180019.png|center]]




