---
title: Command Pattern
draft: false
tags:
---
  
## Definition 
It is a behavioural pattern that encapsulates requests into objects. Thus clients can be parameterized with different requests which can also be queued and logged which allows for undoing actions.  
## GoF Template

![[Pasted image 20230816163711.png|center]]
1. **Command:** This is an interface or abstract class that defines the `execute` method, which encapsulates a specific action.
    
2. **Concrete Command:** These are the concrete implementations of the `Command` interface, each encapsulating a specific action and maintaining a reference to the object that performs the action (the receiver).
    
3. **Receiver:** This is the object that actually performs the action when the `execute` method of a command is called.
    
4. **Invoker:** This is responsible for maintaining a collection of commands and calling their `execute` methods.




