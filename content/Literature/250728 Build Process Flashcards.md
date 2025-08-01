---
title: Build Process Flashcards
draft: false
tags: 
date: 2025-07-28
---
### Question
Name the steps of the build process and the input and output of each step.

### Answer
The build process has four main steps:
1.  **Preprocessing**: Input is a source code file (e.g., `.cpp`/`.c`), and the output is a preprocessed file (e.g., `.i`).
2.  **Compilation**: Input is the preprocessed file (`.i`), and the output is an assembly code file (e.g., `.s`).
3.  **Assembling**: Input is the assembly file (`.s`), and the output is an object file (e.g., `.o`).
4.  **Linking**: Input is one or more object files (`.o`) and libraries, and the output is an executable file (e.g., `.exe`).

---

### Question
Describe and explain the individual processes of the build pipeline.

### Answer
* **Preprocessing**: This step handles directives that start with a `#`. It includes header files, expands macros, removes comments, and handles conditional compilation.
* **Compilation**: This step takes the preprocessed code and converts it into assembly language. It involves checking for syntax and semantic errors. This phase has a front end (lexical, syntactic, semantic analysis) and a back end (code optimization and generation).
* **Assembling**: The assembler takes the assembly code and translates it into machine-readable binary code, creating an object file.
* **Linking**: The linker takes one or more object files and combines them with necessary libraries to create a single executable program. It resolves references between different files.

---

### Question
Describe the steps to build a program and the required tools.

### Answer
To build a program, you follow the build pipeline:
1.  Write the source code in files (e.g., `main.cpp`).
2.  Use a **compiler** (like GCC's `g++`) to preprocess, compile, and assemble the source code into object files.
3.  The **linker** (often part of the compiler suite) then combines these object files and any necessary libraries into a final executable.
For larger projects, you use tools like **Make** or **CMake** to automate these steps.

---

### Question
If you have an error in the code, at which step will the build process fail?
- Semantic error
- Missing library
- Missing header

### Answer
* A **semantic error**, like using an undeclared variable or a type mismatch, would cause the build to fail during the **Compilation** step (specifically, during semantic analysis).
* A **missing library** would cause a failure at the **Linking** step, as the linker wouldn't be able to find the necessary function definitions.
* A **missing header** file would cause the build to fail during the **Preprocessing** step, because the `#include` directive cannot be resolved.

---

### Question
What is the difference between a shared and a static object, and how do you create them?

### Answer
* **Static objects/libraries** are copied directly into the final executable file during linking. This makes the executable larger but self-contained.
* **Shared objects/libraries** (`.so` files) are not copied into the executable. Instead, the executable loads them into memory at runtime when it's launched. This results in smaller executables and allows multiple programs to use the same library in memory.

To create a **shared object** with `g++`, you use the `-shared` and `-fPIC` flags:
`g++ -shared -fPIC -o libexample.so example.cpp`

---

## Make

### Question
What is the general idea of a Makefile?

### Answer
A Makefile is a script that automates the build process. It contains a set of rules. Each rule specifies a **target** (a file to be created, like an executable), its **dependencies** (files it depends on), and the **command** to execute to create the target from the dependencies. `make` only rebuilds what's necessary based on what files have changed, which makes it very efficient.

---

### Question
Describe and explain the advantages of using Make.

### Answer
The main advantages of using `make` are:
* **Automation**: It simplifies complex build processes into a single command (`make`).
* **Efficiency**: It saves time by only recompiling files that have been changed since the last build.
* **Consistency**: It ensures that the project is built the same way every time, regardless of the user or environment.
* **Maintainability**: It organizes the build process, making it easier to manage large projects with many files.

---

## CMake

### Question
Describe the advantages of the CMake program compared to Make.

### Answer
CMake has several advantages over writing Makefiles by hand:
* **Cross-Platform Support**: CMake can generate native build files for different environments (like Makefiles for Linux/macOS or Visual Studio projects for Windows) from a single configuration file (`CMakeLists.txt`).
* **Easier Configuration**: The `CMakeLists.txt` file is generally simpler and more high-level than a Makefile, making it easier to manage complex projects.
* **Dependency Management**: CMake can automatically find libraries and dependencies on a system.
* **Out-of-Source Builds**: CMake makes it easy to keep the build files separate from the source files, which keeps the project directory clean.
* **IDE Integration**: It can generate project files for popular IDEs like Visual Studio, Xcode, and others.

---

## Additional Relevant Questions

---

### Question
What are the different types of tokens identified during lexical analysis?

### Answer
During lexical analysis, the code is broken down into tokens, which are classified as:
* **Keywords**: Reserved words like `int`, `for`, `if`.
* **Identifiers**: Names for variables, functions, or classes (e.g., `main`, `myVariable`).
* **Literals**: Constant values like numbers (`23`) or strings (`"hello"`).
* **Operators**: Symbols for operations like `+`, `=`, `*`.
* **Punctuators**: Punctuation characters like `{`, `}`, `(`, `)`, `;`.

---

### Question
What is an Abstract Syntax Tree (AST)?

### Answer
An Abstract Syntax Tree (AST) is a tree representation of the logical structure of the source code. It's created during the **syntactic analysis** phase of compilation. Each node in the tree represents a construct in the code, like a variable declaration, an expression, or a statement. The compiler uses the AST to check for syntactical correctness and for later stages like semantic analysis and code optimization.

---

### Question
What is the purpose of code optimization in the compilation process?

### Answer
The purpose of code optimization is to improve the intermediate code to produce a program that runs faster and/or uses less memory. The key rules for optimization are that it must not change the program's original meaning, it should improve performance, and it shouldn't take too long to perform. An example is reducing complex calculations into simpler ones.