---
title: Quadratures - Accuracy and Error Table
draft: false
tags: 
date: 2025-06-24
---
## **Essential Quadrature Rules**

| **Rule**                 | Points | degree of Polynomial $(N)$ | **Degree of Accuracy** $(K)$ | Order of Error/Consistency $(q)$ |
| ------------------------ | ------ | -------------------------- | ---------------------------- | -------------------------------- |
| **Left/Right Rectangle** | 1      | 0                          | $0$                          | $O(h)$                           |
| **Midpoint**             | 1      | 0                          | $1$                          | $O(h^2)$                         |
| **Trapezoid**            | 2      | 1                          | $1$                          | $O(h^2)$                         |
| **Simpson/Kepler**       | 3      | 2                          | $3$                          | $O(h^4)$                         |
$K = 0-1-1-3$, **Order of Error** $= 1-2-2-4$
### **Degrees of Accuracy:**
- **Rectangle rules**: K = 0 (only integrates constants exactly)
- **Trapezoid & Midpoint**: K = 1 (integrates up to linear functions exactly)
- **Simpson/Kepler**: K = 3 (integrates up to cubic functions exactly)

### **Composite Rules:**

- **Summed Rectangle**: Error = O(h), halving h → error ÷ 2
- **Summed Trapezoid**: Error = O(h²), halving h → error ÷ 4
- **Summed Simpson**: Error = O(h⁴), halving h → error ÷ 16

**Note**: Rectangle rules are the simplest but least accurate. Midpoint rule is surprisingly good (same error order as trapezoid despite using only 1 point!).

--- 
