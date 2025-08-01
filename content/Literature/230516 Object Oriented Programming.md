---
title: Object Oriented Programming
draft: false
date: 2023-05-16
---
## **Key Concepts**

1. **Data Encapsulation:** Bundles data and methods within an object, hiding internal details and providing controlled access to the data.
2. **Inheritance:** Enables a new class to inherit properties and behaviors from an existing class, promoting code reusability and hierarchical organization.
3. **Polymorphism:** It allows objects to perform different functions based on the context (Class/Subclass) they are called in. In Python, this is mainly done using **Method Overriding**.
4. **Data Abstraction:** Hides implementation details, exposing only essential features of an object, improving code manageability and maintainability.
5. [[230802 Composition|Composition]]: It allows a class to leverage the behaviors and functionalities of its component classes without necessarily inheriting from them. This is done by including the other class in the body of the object. 

## Intention of class structure, access protection, and abstract classes
- **Class Structure**: The intention is to create blueprints (classes) for objects, which promotes code reuse and establishes a natural hierarchy between related classes.
 - **Access Protection**: The primary goal is to protect data from unrestricted access and modification. By using access specifiers (`private`, `protected`, `public`), it enforces data hiding, a core principle of encapsulation that enhances security and program stability.
- **Abstract Classes**: The intention is to define a common interface for a group of subclasses while hiding complex implementation details. An abstract class cannot be instantiated on its own; it serves as a template that forces its child classes to implement specific methods, ensuring a consistent structure and improving code maintainability.
