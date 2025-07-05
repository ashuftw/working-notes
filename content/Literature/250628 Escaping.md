---
title: Escaping
draft: false
tags: 
date: 2025-06-28
---
Escaping is a functionality in Regex that allows you to turn [[250602 Regular vs Metacharacters|Regular Characters]] into [[250602 Regular vs Metacharacters|Metacharacters]] and vice versa.  

In [[250628 Basic vs Extended Regular Expressions|BRE]] escaping is done by prepending "$\backslash$" to the character.

**Example**
- "$\backslash \mathbf .$" matches an actual period
- "$\backslash \mathbf w$" matches word characters


> **Note**: Escaping is critical for matching special characters like ., *, ?, etc.