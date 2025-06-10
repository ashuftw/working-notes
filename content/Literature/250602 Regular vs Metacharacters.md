---
title: Regular vs Metacharacters
draft: true
tags: 
date: 2025-06-02
---

### Regular Characters

They are literal characters that match themselves exactly in a pattern. They represent the actual character you want to find.

**Examples:**

- `a` matches the literal letter "a"
- `5` matches the literal digit "5"

### Metacharacters

They are special characters that have predefined meanings and functions in regular expressions. They don't match themselves literally but instead control how the pattern matching works.

**Common metacharacters include:**
- `.` - matches any single character
- `^` - matches the beginning of a line
- `$` - matches the end of a line
- `*` - matches 0 or more of the preceding character
- `+` - matches 1 or more of the preceding character
- `?` - matches 0 or 1 of the preceding character
- `[]` - defines a character set
- `()` - creates groups
- `|` - logical OR operator