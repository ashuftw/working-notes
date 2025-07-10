---
title: Flashcards on Linux Shell Scripting - Theory
draft: false
tags: 
date: 2025-07-10
---
### **Script vs. Program**
**Explain the difference between a compiled program and a script.**
- **Script**: A set of instructions that is interpreted and executed line-by-line at runtime. This allows for quick implementation but is generally slower.
- **Program**: A set of instructions that is preprocessed by a compiler into a binary file before it is run. This process optimizes the code to run fast and efficiently, especially for large amounts of data.

---
### **Advantages & Disadvantages**
**Discuss the key advantages and drawbacks of scripts vs. programs.**
- **Scripts**:
    - **Advantages**: They are quick to write and test.
    - **Disadvantages**: They are interpreted at runtime, which makes them slower and less efficient for data-intensive tasks.
- **Programs**:
    - **Advantages**: They are highly optimized for speed and efficiency.
    - **Disadvantages**: The development process is slower due to the required compilation step, and the resulting binary file is not easily portable to other systems without recompiling.

---
### **Running a Bash Script**
**What are the two main ways to run or execute a Bash script?**
1. **Pass the script to the interpreter**: Directly call the interpreter and provide the script file as an argument.
    - **Example**: `bash ./my_script.sh` 
2. **Execute the script directly**: This requires two steps:
    - **Shebang**: The script's first line must be a shebang that specifies the interpreter (e.g., `#!/bin/bash`).
    - **Permissions**: The script file must have execute permissions, which can be set with `chmod`.
    - **Example**: `chmod +x ./my_script.sh`, followed by `./my_script.sh`.
---
### **Variables**
**How do you define and access a variable in a Bash script?**
- **Definition**: Assign a value using the `=` sign without any spaces around it. By convention, variable names are in uppercase.
    - **Example**: `BACKUP_DIR="/mnt/data"`
- **Accessing**: Use a dollar sign `$` before the variable name. It's best practice to enclose the name in curly braces
    `${}` to prevent errors.
    - **Example**: `echo "Backing up to ${BACKUP_DIR}"`

---

### **Positional Parameters (Arguments)**
**What are positional parameters and how are they accessed in a script?**
- **Definition**: Positional parameters are the arguments passed to a script when it is run from the command line.
- **Access**: They are accessed using a `$` followed by their position number.
    - `$1`: The first argument.
    - `$2`: The second argument.
- **Special Variables**:
    - `$#`: The total number of arguments.
    - `$0`: The name of the script itself.
    - `$@`: All arguments as a space-separated list.
---
### **Conditionals (if statement)**
**What is the basic syntax for an `if-elif-else` statement in Bash?**
Conditional statements control the script's flow based on a test's outcome.
**Syntax:**
```bash
if [ "$1" -gt 100 ];
then
    echo "Value is greater than 100."
elif [ "$1" -eq 100 ];
then
    echo "Value is exactly 100."
else
    echo "Value is less than 100."
fi
```

---
### **Loops (`for` and `while`)**

**Show a simple example of a for loop and a while loop.**
- **`for` loop**: Executes code for each item in a list or range.
    - **Example**:
        ```bash
        for i in {1..3};
        do
            echo "Loop iteration: ${i}"
        done
        ```
- **`while` loop**: Executes code as long as a condition remains true.
    - **Example**:
        ```bash
        COUNT=1
        while [ ${COUNT} -le 3 ];
        do
            echo "Count is ${COUNT}"
            ((COUNT++))
        done
        ```
---

### **Functions**
**How do you define a function and check its return value in Bash?**
Functions are used to organize code into reusable blocks.
- **Definition & Call**:
    ```bash
    function check_file() {
        if [ -f "$1" ]; then
            return 0  # Success
        else
            return 1  # Failure
        fi
    }
	
    check_file "/etc/hosts"
    ```
- **Check Return Value**: Immediately after calling the function, use the special variable `$?` to get the return value (0-255).
    ```bash
    if [ $? -eq 0 ]; then
        echo "File exists."
    fi
    ```
---
### **Command-Line Options (`getopts`)**
**What is getopts and what is its purpose?**
- **Purpose**: `getopts` is a built-in Bash command used to reliably parse command-line options (flags like `-v` or `-f`) and their arguments when a script is run.
- **How it works**: It's typically used inside a `while` loop to process the options provided by the user. It uses an `OPTSTRING` to define which options are valid and which require an argument (e.g., a colon after an option letter indicates an argument is needed).
**Example**
`simple_script.h`
```bash
#!/bin/bash

# This loop checks for command-line options.
# OPTSTRING=":a" tells it to only look for the '-a' flag.
while getopts ":a" opt; do
  case ${opt} in
    a)
      echo "Option -a was triggered."
      ;;
    ?)
      echo "Invalid option."
      ;;
  esac
done
```
**Command**
`$ ./simple_script.sh -a`
**Output**
`Option -a was triggered.`

---
### **Analyzing a Script**
Your learning goals require you to analyze a script. What are the key features to look for when explaining a script's functionality?
When analyzing a script, identify and explain these core components:
1. **Shebang**: What interpreter does it use (`#!/bin/bash`)? 
2. **Variables**: What values are being stored? Are there any hard-coded paths or settings? 
3. **Input**: How does it get input? (Positional parameters like `$1`, or options via `getopts`). 
4. **Core Logic**: What is the main purpose? Look at the `if` statements, `loops`, and `functions` to understand the flow and decisions it makes.
5. **Error Handling**: Does it check if commands were successful (`$?`)? Does it validate user input (e.g., checking if a file exists with `[ -f FILE ]`)? 
6. **Output**: What does it print to the screen (`echo`)? Does it create or modify files?