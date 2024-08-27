---
title: Abstract Factory Pattern
draft: false
tags:
---
  
## Definition
It is an [[230812 Object Creational pattern|Object Creational pattern]] that enables a user to create objects without exposing how they are actually instantiated or by referring to the concrete class. It does this by introducing the **FactoryClass** which provides an interface that delegates this process. 

## Advantages or benefit
It creates families of related objects while keeping code loosely coupled and avoiding dependency on specific implementations.

## Example
```python
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class AnimalFactory:
    def create_animal(self, animal_type):
        if animal_type == "dog":
            return Dog()
        elif animal_type == "cat":
            return Cat()
        else:
            raise ValueError(f"Unknown animal type: {animal_type}")
```

## Usage of the Factory Pattern
```python
if __name__ == "__main__":
    animal_factory = AnimalFactory()
												# Otherwise	
    dog = animal_factory.create_animal("dog")   # dog = Dog()
    cat = animal_factory.create_animal("cat")   # cat = Cat()

    print(dog.speak())  # Output: Woof!
    print(cat.speak())  # Output: Meow!
```
Objects `dog` and `cat` were created without refererring to their concrete classes. `Dog` and `Cat` 

