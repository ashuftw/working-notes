---
title: Flashcards on Linux Tools
draft: false
tags: 
date: 2025-07-10
---
### **Flashcard 1: `find`**

**What is the `find` command used for and what is its basic syntax?**
- **Purpose:** The `find` command is a command-line utility used to search for files within a directory hierarchy.
- **Syntax:** `find PATH [FLAG] [EXPRESSION]`.
- **Functionality:** It searches for files based on expressions, which can include tests like name (`-name`), type (`-type`), or regular expressions. It can then perform various actions (`-exec`, `-delete`, etc.) on the search results. If no action is specified, it defaults to printing the file path.
---
### **Flashcard 2: `grep`**
**What does `grep` stand for, what is its primary function, and what are some key options?**
- **Stands for:** **G**lobal **R**egular **E**xpression **P**rint.
- **Primary Function:** `grep` is a text-search utility that scans files or input streams for lines containing a match to a given pattern.
- **Key Options:**
    - `-i`: Ignores case during the search.
    - `-v`: Inverts the match, selecting non-matching lines.
    - `-r`: Searches recursively through directories.
    - `-c`: Counts the number of matching lines instead of showing them.
    - `-E`: Enables extended regular expressions, allowing for operators like `|` for "OR" conditions.
---
### **Flashcard 3: `awk`**
**What is `awk`, and what key features distinguish it from grep?**
- **Definition:** `awk` is a powerful **pattern-scanning** and **processing language** designed for advanced text manipulation.
- **Key Distinguishing Features:**
    - **Field-Based Processing:** `awk` excels at handling text in columns (fields). It can easily split lines based on a delimiter (like a comma or space) and process individual fields.
    - **Scripting Language:** It is a full programming language with variables, arithmetic operations, and conditional logic (`if-else`), making it suitable for generating reports and complex data transformations.
    - **BEGIN/END Blocks:** `awk` scripts can include a `BEGIN` block to execute code before processing any lines and an `END` block to execute code after all lines have been processed.
---
### **Flashcard 4: `sed`**
**What does `sed` stand for, and what are its primary use cases?**
- **Stands for:** **S**tream **Ed**itor.
- **Primary Use Cases:** `sed` is used to perform basic text transformations on an input stream or file, line by line. It is ideal for:
    - **Substitution:** The `s` command is used to find and replace text (e.g., `s/old/new/g` to replace all occurrences).
    - **Deletion:** The `d` command deletes entire lines that match a pattern or line number.
    - **Insertion/Appending:** The `i` and `a` commands insert text before or append text after a specified line, respectively.
---
### **Flashcard 5: `diff`**
**What is the `diff` command used for? What types of content can it compare?**
- **Purpose:** `diff` is a utility that compares two sources of text and shows the differences between them.
- **Content It Can Compare:**
    - **Files:** It compares two files line-by-line to identify which lines need to be added, removed, or changed to make the files identical.
    - **Directories/Folders:** It can recursively compare the contents of two directories. It will report which files are unique to each directory and run a file comparison on any files that share the same name.
---
### **Flashcard 6: `column`**
**What is the function of the `column` command? Provide a common use case.**
**Back:**
- **Function:** The `column` command formats input text from a file or stream into well-aligned, multi-column layouts.
- **Common Use Case:** It is frequently used to create "pretty-printed" tables from data that uses delimiters (like commas in a CSV or colons in `/etc/passwd`).
- Example: To format the colon-delimited /etc/passwd file into a clean table, you would use:
    `column -t -s ":" /etc/passwd`. The
    `-t` flag creates a table, and `-s` specifies the delimiter.
---
### **Flashcard 7: Efficient Tool Selection**
**For the following tasks, which tool (`find`, `grep`, `awk`, `sed`) is most efficient?**
1. Searching a file hierarchy for files modified in the last 24 hours.
 **`find`:** Best for searching for _files_ based on metadata like modification time, name, or type.
2. Extracting just the lines containing the word "`Error`" from a log file.
	 **`grep`:** Perfect for simple line extraction based on a pattern.
3. Changing every instance of "`cat`" to "`dog`" in a text file.
	 **`sed`:** Its primary strength is stream editing, making it ideal for find-and-replace operations.
4. Calculating the average value of the 3rd column in a data file and printing only the result.
	 **`awk`:** The only one of the four with built-in arithmetic and columnar processing capabilities, making it the right choice for calculations on structured text data.


---
### **Flashcard 8: Practical Skills Overview**
**Match the task to the primary tool (`find, grep, awk, sed, diff, column`).**
- Text manipulation & substitution
- Text formatting into tables
- Character/word extraction from a line
- File searching in a hierarchy
- Comparing folder contents
- Column extraction from a file

**Back:**
- **Text manipulation & substitution:** `sed` 
- **Text formatting into tables:** `column`
- **Character/word extraction from a line:** `grep` or `awk`
- **File searching in a hierarchy:** `find`
- **Comparing folder contents:** `diff` 
- **Column extraction from a file:** `awk` 