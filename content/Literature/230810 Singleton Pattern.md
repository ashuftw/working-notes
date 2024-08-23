Status: #finished 
## Definition 
It is a **creational pattern** that ensure that a class has only one instance and has a global access point. 
## Example 
> Note: Implementation detail isn't that important. 

```python
class Singleton(object):
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print('Creating the object')
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

a = Singleton()
b = Singleton()    # The same instance of the object is used because of the if-statement
assert a is b

# However above example isn't thread safe. 
import threading

class ThreadSafeSingleton:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instance is None:
            with cls._lock:
                # Another thread could have created the instance
                # before we acquired the lock. So check that the
                # instance is still nonexistent.
                if not cls._instance:
                    cls._instance = super(ThreadSafeSingleton, cls).__new__(cls)
        return cls._instance

```

---
# References
