---
title: OOP Template
draft: false
tags: 
date: 2025-07-20
---

```python
# Basic Class
class Student:
    def __init__(self, name, course):
        self._name = name  # protected
        self.course = course
        self.semester = 1
    
    def enroll(self):
        # method implementation
        pass

# Inheritance
class GradStudent(Student):
    def __init__(self, name, course, thesis):
        super().__init__(name, course)
        self.thesis = thesis

# Magic Methods are methods that start with "__", they only take self as parameter
def __str__(self):
    return f"{self._name}, {self.course}"

# Property (if needed)
@property
def name(self):
    return self._name

# Create an instance
grad = GradStudent("Ahab", "Seafaring")

# Access attributes
print(grad.course)       # Output: Seafaring 
# Use the property
print(grad.name)         # Output: Ahab 
```


### Property(getter/setter)

```python
class Person:
    def __init__(self, age):
        self._age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value): # value parameter is required even if you don't use it
        if value >= 0:
            self._age = value
```