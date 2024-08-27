  
## Objective
A protocol is an informal interface that contains a set of methods or rules that a class needs to adhere to.

### Note: 
- **Interface** is a layer of abstraction between the Superclass and the Subclass. 
- We say *informal* 'cause it is not strictly needed. It is just a way of writing code that is self-documenting, hence preventing errors. 

![[Pasted image 20230801152922.png]]
## Syntax 
```python
from typing import Protocol

class Ant(Protocol):
	def do_your_job(self) -> None:
		raise NotImplementedError("Subclasses must implement the 'do_your_job' method")`
```



