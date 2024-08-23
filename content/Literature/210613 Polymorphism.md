Status: #finished 

**Polymorphism** is a feature of [[230613 Object Oriented Programming|Object Oriented Programming]] which allows objects to perform different functions based on the context (Class/Subclass) they are called in. In Python, this is mainly done using **Method Overriding**. 

**Inbuilt Polymorphic Objects**
```python
# len() being used for a string
print(len("geeks"))               # Output: 5
# len() being used for a list
print(len([10, 20, 30]))          # Output: 3
```
**User Defined Objects**
``` python
# Base class
class Animal:
    def speak(self):
        print("An animal makes a sound.")
# Inherited class
class Dog(Animal):
    def speak(self):
        print("The dog barks.")
class Cat(Animal):
    def speak(self):
        print("The cat meows.")

# Creating objects
animal = Animal()
dog = Dog()
cat = Cat()

# Calling the speak method
animal.speak()  # Output: "An animal makes a sound."
dog.speak()     # Output: "The dog barks."
cat.speak()     # Output: "The cat meows."
```




---
# References
1. https://www.geeksforgeeks.org/polymorphism-in-python