---
title: Flashcards on Linux Tools - Practical
draft: true
tags: 
date: 2025-07-10
---
### **Text Manipulation (Deletion)**
**How do you manipulate a text file to delete the third line?**

Use the sed stream editor with the d command for deletion. This command will display the file's contents without the 3rd line.
**Example:**
`sed '3d' employee_database.txt` 

---
### **Text Formatting (Creating a Table)**
**How do you format a space-separated data file into a clean, aligned table?**

Use the column command with the -t option. This determines the number of columns from the input and creates a well-formatted table.

**Example**
`column -t data_file.txt` 

---
### **Character/Word Substitutions**
**How do you substitute every instance of the word "Engineering" with "Eng" in a file?**

Use `sed`'s substitute command, `s`, with the `g` (global) flag to replace all occurrences on a line. 

**Example**
`sed 's/Engineering/Eng/g' employee_database.txt` 

---
### **Line/Word Extraction**
**How do you extract and display only the lines from a file that contain the word "apple"?**

Use `grep` command, which is designed to find and print lines that match a pattern. 

**Example**
`grep 'apple' fruitlist.txt` 

---
### **Column Extraction**
**How do you extract and print only the first and third columns from a comma-separated file?**

Use the `awk` command. It is designed to process text based on fields (columns). Use the `-F` flag to set the field separator to a comma and print to specify which columns to display.

**Example**
`awk -F"," '{print $1, $3}' employee-database.csv` 

---
### **File Searching**
**How do you search the current directory and all its sub-directories for files ending with the `.cpp` extension?**

`find` command, which searches a directory hierarchy based on criteria like a file's name. 

**Example**
find . -name "*.cpp" 10

---
### **Text Searching (Multiple Files)**
**How do you search for the word "dummy" inside all files ending with `.txt` in the current directory?**

Use the grep command with a shell wildcard (*).
`grep` will search the content of every file matching the pattern and display the filename along with the matching lines. 

**Example**
`grep 'dummy' *.txt` 

---
### **Comparing Folders & Files**
**How do you compare the contents of two folders, `folder1` and `folder2`?**

Use the diff command. When used on directories, it reports files that are unique to each folder and shows the differences between files that share the same name. 

**Example**
`diff folder1 folder2` 