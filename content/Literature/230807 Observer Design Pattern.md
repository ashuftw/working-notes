---
title: Observer Design Pattern
draft: false
tags:
---
  
## Definition 
It defines **One-to-Many** dependency between objects so that when objects change state all of it's dependencies are notified and updated immediately. 
- **One** -> Subject i.e that which is changing. It keeps a list of observers so that when there is a change in state, it notifies each of the many observers by iterating through the list. 
- **Many** -> Object i.e. the ones that are interested in the state of the subject. Once the notification is received, they perform/update their purpose.
## Example: 
- **Subject** -> Stocks, **Object** -> Calculation of Stock Prices

![[Pasted image 20230807125312.png]]
> Note: In this example the the **Many** is replaced by an interface in order to have dependency inversion. 

