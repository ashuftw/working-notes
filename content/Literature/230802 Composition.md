---
title: Composition
draft: false
date: 2023-08-02
---

## Definition
It is a concept in [[230516 Object Oriented Programming|Object-Oriented Programming]] allows a class to leverage the behaviors and functionalities of other classes without directly inheriting from them.

This is achieved by by including one or more instances of other classes (i.e. creating **objects**) as part of its internal structure. 

## Example
```Python
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()
    def start(self):
        print("Car starting...")
        self.engine.start()

my_car = Car()    # Car starting...
my_car.start()    # Engine started
```

