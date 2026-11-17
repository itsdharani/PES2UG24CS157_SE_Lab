# Lab 5: Static Code Analysis: Reflection

### 1. What is static code analysis, and why is it important?

Static code analysis examines source code without executing the program to identify potential bugs, security vulnerabilities, and coding-style violations. It helps developers detect problems early, improve maintainability, and make software more reliable and secure.

### 2. What is the difference between Pylint, Bandit, and Flake8?

Pylint checks code quality, naming conventions, documentation, and potential programming errors. Bandit identifies common security risks, such as unsafe shell execution and insecure temporary-file handling. Flake8 checks Python formatting and compliance with PEP 8 style guidelines. Using all three provides a broader assessment of code quality and security.

### 3. What issues did you identify, and how did you fix them?

The initial reports identified a mutable default argument, overly broad exception handling, a hardcoded password, the use of an assertion for input validation, insecure temporary-file creation, and unsafe shell command execution. Pylint also reported missing docstrings and naming issues, while Flake8 identified formatting violations. I addressed these issues by using `None` as the default argument and initializing lists inside the function, validating inputs explicitly, avoiding broad exception handling, using secure temporary-file creation, validating phone numbers, and replacing `os.system()` with `subprocess.run()` using `shell=False`. I also improved function naming, documentation, and formatting.

### 4. What did you learn from this lab, and what are the limitations of static analysis?

This lab demonstrated how static analysis tools can identify potential problems before a program is deployed. After the fixes, the Pylint score increased from 4.81/10 to 10.00/10, and Flake8 reported no remaining violations. Bandit reported no high- or medium-severity findings, although three low-severity warnings remained. Static analysis cannot guarantee that a program behaves correctly in every situation or identify every runtime problem. Therefore, it should be combined with testing and code review.
