---
title: Basic vs Extended Regular Expressions
draft: false
tags: 
date: 2025-06-28
---
- **BRE**: **`? + | ( ) { }`** are REGULAR characters → need `\` to activate (called [[250628 Escaping|Escaping]])
- **ERE**: **`? + | ( ) { }`** are METACHARACTERS → need `\` to make literal
  
**Example**:  

- BRE: `\+` means one or more 
- ERE: `+` means one or more