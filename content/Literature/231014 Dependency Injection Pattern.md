Status: #finished 
## Definition
It is a way of using Objects of other Classes by creating an object externally and passing it as an argument. 
## Example
```python
class Weapon:
    def __init__(self, name):
        self.name = name

class Player:
    def __init__(self, name, weapon):    # weapon argument is added as a placeholder
        self.name = name
        self.weapon = weapon

    def attack(self):
        print(f"{self.name} attacks with {self.weapon.name}!")

# We create the weapon externally
player_weapon = Weapon("Bow")

# We inject the weapon into the Player class
player = Player("Archer", player_weapon)
player.attack()
```
**Without Dependency Interjection**
```python
class Weapon:
    def __init__(self, name):
        self.name = name

class Player:
    def __init__(self, name):
        self.name = name
        self.weapon = Weapon("Sword")    # Player class depends on Weapon()

    def attack(self):
        print(f"{self.name} attacks with {self.weapon.name}!")
        
player = Player("Hero")
player.attack()
```



---
# References
