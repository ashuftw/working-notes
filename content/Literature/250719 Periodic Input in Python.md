---
title: Periodic Input in Python
draft: false
tags: 
date: 2025-07-19
---
## Wave Function
$$u(t) = A \cdot \text{sgn}\left(\sin\left(\frac{2\pi t}{T}\right)\right)$$

- $A$ -> Amplitude
- `sign()` -> **signum** function that returns $\pm1$ (for a square wave)
- T -> Period
### Code
```python
def rectangular_input(t):
    return 0.1 * np.sign(np.sin(np.pi * t / 50))

```