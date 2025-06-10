---
title: File Permissions
draft: false
tags: 
date: 2025-05-15
---
![[content/Files/Pasted image 20250515130213.png|center|600]]

## Levels of permissions:

- **Read**: Display content of file
- **Write**: Make changes to file/folder
- **Execute**: Run programs (compiled binaries)
- Representation:  rwxrwxrwx or 777

> Note: There exists a special pseudo permission called [[250515 Sticky bits|Sticky bits]] which is used to prevent accidental deletions. 

## Types of permissions:

- **User**
- **Group**
- **Other**
![[content/Files/Pasted image 20250515132446.png|center|600]]

## Example

1. Remove write permission for **group** and **others**
2. Add execute permissions to all
	![[content/Files/Pasted image 20250515133301.png]]
