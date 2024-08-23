Status: #finished 
## Definition 
It states that Objects of a superclass should be replaceable with the objects of a subclass without affecting the correctness of the program. 

*"If S is a subclass of T, then an object of class T should be replaceable with an object of class S without altering the desirable properties of the program."*

## Example
![[Pasted image 20230806111608.png]]
> `bird` is an Object of `Bird()`
```python
class Bird:
    def fly(self):
        pass

class Sparrow(Bird):
    def fly(self):
        print("Sparrow is flying")

class Ostrich(Bird):
    def fly(self):
        raise ValueError("Ostrich cannot fly")

bird = Bird()
sparrow = Sparrow()
ostrich = Ostrich()

def make_bird_fly(bird):
    bird.fly()

make_bird_fly(sparrow)  # This works as expected, Sparrow can fly
make_bird_fly(ostrich)  # As expected, this raises an exception - Ostrich can't fly
```



---
# References
Vimdot code
```bash
digraph G {
    rankdir=BT;  // Top-to-bottom layout

    // Nodes (Classes and Function)
    Bird [shape=box, label="Bird"];
    Sparrow [shape=box, label="Sparrow"];
    Ostrich [shape=box, label="Ostrich"];
    make_bird_fly [shape=diamond, style=filled, color=lightblue, label="make_bird_fly(bird)"];

    // Edges (Inheritance and Function Calls)
    Sparrow -> Bird;
    Ostrich -> Bird [label="inherits"];
    make_bird_fly -> Bird [style=dashed, label="calls"];
    make_bird_fly -> Sparrow [style=dashed];
    make_bird_fly -> Ostrich [style=dashed];
}

```
