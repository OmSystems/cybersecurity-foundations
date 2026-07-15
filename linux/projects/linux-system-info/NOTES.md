# Linux Bash & Shell Basics

A quick reference guide covering the foundational concepts of the Linux command line, permissions, and scripting syntax.

---

### 1. What is a Shell?
A **Shell** is a command-line interpreter that acts as an interface between the user and the operating system kernel. It takes the commands you type, interprets them, and passes them to the OS to be processed. 
> *Examples of shells include sh, Bash, Zsh, and Fish.*

### 2. What is Bash?
**Bash** (Bourne Again SHell) is a specific, widely used implementation of a shell. It is the default command-line interface on many Linux distributions and macOS (historically). It provides the environment where you run standard commands like `cd`, `ls`, and `chmod`.

### 3. What is a Shebang (`#!`)?
The **Shebang** (also called a hashbang) is a special character sequence (`#!`) placed at the absolute beginning of a script file. It tells the operating system's program loader which interpreter should be used to execute the rest of the script.
* *Example:* `#!/bin/bash` tells the system to run the script using Bash.
* *Example:* `#!/usr/bin/env python3` tells the system to run the script using Python.

### 4. What does `chmod +x` do?
The `chmod +x` command changes a file's permissions to make it **executable**. By default, new text files or scripts only have read/write permissions. Running `chmod +x filename.sh` allows you to run the script directly from the terminal using `./filename.sh`.

### 5. What does the `$(...)` syntax mean?
The `$(...)` syntax is used for **Command Substitution**. It executes the command enclosed within the parentheses, captures its standard output, and substitutes it back into the line. This allows you to store the output of a command into a variable or pass it as an argument to another command.

* *Example:*
    ```bash
    CURRENT_DIR=$(pwd)
    echo "You are currently in: $CURRENT_DIR"
    ```