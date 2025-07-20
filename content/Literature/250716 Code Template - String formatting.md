---
title: Code Template - String formatting
draft: false
tags: 
date: 2025-07-16
---
## 1. f-strings 

```python
name = "Alice"
age = 25
value = 3.14159

# Insert variables 
f"Hello {name}, you are {age} years old"
# Format the variables 
f"Pi is approximately {value:.2f}"
f"Percentage: {0.85:.1%}"
f"Scientific: {1234:.2e}"
```
## 2. Common Format Specifiers

|Format|Description|Example|Output|
|---|---|---|---|
|`:.2f`|2 decimal places|`f"{3.14159:.2f}"`|`3.14`|
|`:.0f`|No decimals|`f"{3.14159:.0f}"`|`3`|
|`:d`|Integer|`f"{42:d}"`|`42`|
|`:.1%`|Percentage|`f"{0.85:.1%}"`|`85.0%`|
|`:.2e`|Scientific notation|`f"{1234:.2e}"`|`1.23e+03`|
|`:>10`|Right align, width 10|`f"{'hi':>10}"`|`hi`|
|`:<10`|Left align, width 10|`f"{'hi':<10}"`|`hi`|
|`:^10`|Center align, width 10|`f"{'hi':^10}"`|`hi`|

## 3. Padding and Alignment

```python
# Zero padding for numbers
f"{42:05d}"        # "00042"
f"{3.14:08.2f}"    # "00003.14"

# String alignment
f"{'text':>10}"    # "      text"
f"{'text':<10}"    # "text      "
f"{'text':^10}"    # "   text   "
```

## 4. Quick Reference for Numbers

```python
x = 1234.5678
f"{x:.2f}"     # 1234.57 (2 decimals)
f"{x:,.2f}"    # 1,234.57 (with commas)
f"{x:8.2f}"    # " 1234.57" (width 8, right aligned)
f"{x:08.2f}"   # "01234.57" (zero padded)
```

## 5. Date/Time Formatting

```python
from datetime import datetime
now = datetime.now()
f"{now:%Y-%m-%d}"      # 2025-07-16
f"{now:%H:%M:%S}"      # 14:30:45
f"{now:%B %d, %Y}"     # July 16, 2025
```

## 7. Exam-Ready Quick Tips

- **Always use f-strings** for new code (fastest, most readable)
- **Remember the colon** before format specifiers: `{value:.2f}`
- **Common patterns**: `.2f` (decimals), `,.0f` (integers with commas), `.1%` (percentages)
- **Width and alignment**: `>` (right), `<` (left), `^` (center)
- **Zero padding**: `05d` for integers, `08.2f` for floats