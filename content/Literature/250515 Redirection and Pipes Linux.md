---
title: Redirection and Pipes in Linux
draft: false
tags: 
date: 2025-05-15
---
## Redirection
The redirection operator (>) redirects the output of a command to a file instead of displaying it in the terminal.

**Redirect standard output to a file**
`command > filename` (overwrites file content) 
or 
`command >> filename` (appends to file)

**Redirect standard error to a file**  
`command 2> filename` (for stderr) 
or
`command > filename 2>&1` (both stdout and stderr)

**Use a file as input for a command**  
`command < filename`

## Pipes
Pipe is used to pass output of one command to another
`ls . | grep file`

### Difference between a Pipe and Redirection Operations 
|                  | Pipe                                                                                                                                       | Redirection                                                                           |
| ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------- |
| **Description**  | Connects the output stream of one command directly to the input stream of another command, allowing commands to work together in sequence. | Redirects the output of a command to a file instead of displaying it in the terminal. |
| **Example**      | `ls . \| grep file`                                                                                                                        | `ls -l > output.txt`                                                                  |
| **What it does** | Lists files and filters results containing "file"                                                                                          | Saves directory listing to a file                                                     |


[[250515 File Streams]]