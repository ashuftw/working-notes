---
title: OOP Template
draft: false
tags: 
date: 2025-07-20
---

```python
class MyClass:
    def __init__(self, param):
        self._protected = param
    
    @property
    def protected(self):
        return self._protected
    
    @protected.setter
    def protected(self, value):
        self._protected = value
```