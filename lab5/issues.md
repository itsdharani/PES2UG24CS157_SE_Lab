# Static Analysis Issues: Blood Donation Management System

The line numbers in the first eight rows refer to the original `blood_donation.py` before fixes. The final three rows describe the remaining Bandit findings in the corrected version.

| Issue | Type | Line(s) | Description | Fix Approach |
|---|---|---:|---|---|
| Shell command execution | Security: High | 65 (original) | `os.system()` constructs a shell command using `phoneList`, potentially allowing command injection if untrusted input is supplied. | Replaced shell execution with `subprocess.run()` using a list of arguments, `shell=False`, and input validation. |
| Insecure temporary filename | Security: Medium | 60 (original) | `tempfile.mktemp()` generates a filename without securely creating the file, leaving a race condition. | Replaced it with `tempfile.NamedTemporaryFile()` to securely create the temporary file. |
| Mutable default argument | Code quality / bug risk | 17 (original) | `notes=[]` is created once and reused across calls that omit the argument, potentially sharing notes between registrations. | Changed the default to `None` and initialize a fresh list inside the function. |
| Broad exception handling | Reliability / maintainability | 45 (original) | Catching `Exception` hides unexpected errors and makes invalid input indistinguishable from a legitimate zero-unit result. | Added an explicit check for unknown patient blood groups and return `0` without catching unrelated exceptions. |
| Hardcoded password | Security : Low | 5 (original) | A credential is stored directly in the source code and could be exposed when the repository is shared. | Replaced the hardcoded value with an environment variable. |
| `assert` used for validation | Reliability / security : Low | 18 (original) | Assertions can be disabled when Python runs with optimization and should not be used for essential input validation. | Replaced the assertion with an explicit condition that raises `ValueError` for an unknown blood group. |
| Missing docstrings and non-snake-case names | Code quality / style | Multiple (original) | Missing documentation and camelCase function and parameter names reduce readability and trigger Pylint warnings. | Added module and function docstrings and renamed functions and parameters to snake_case. |
| Flake8 formatting violations | Style | 7, 57–58, 80–81 (original) | The original file contains a long line, excess blank lines, insufficient spacing before an inline comment, and missing spaces around an assignment operator. | Wrapped long lines, removed unnecessary blank lines, and corrected spacing to follow PEP 8 conventions. |
| Subprocess module usage | Security : Low | 6 (final) | Bandit flags the `subprocess` import for review because launching external processes can introduce security risks. | Kept process execution limited to the intended SMS utility and avoided shell interpretation. |
| Partial executable path | Security : Low | 96 (final) | Bandit warns that `send-sms` is resolved through the system's executable search path. | Use a trusted, explicitly configured executable path where the SMS utility is deployed. |
| Subprocess argument review | Security : Low | 96 (final) | Bandit flags the subprocess call for review to ensure arguments cannot be used to execute unintended commands. | Retained `shell=False`, passed arguments as a list, and validated phone numbers before invocation. |

## Summary

The original analysis identified code-quality, reliability, style, and security issues. The code was updated to address the documented problems, and all three static analysis tools were rerun.

- **Pylint:** 10.00/10.
- **Flake8:** No findings.
- **Bandit:** Zero high-severity and zero medium-severity findings; three low-severity findings remain.

Static analysis improves code quality and helps identify potential vulnerabilities, but its findings must be reviewed in context. The remaining Bandit warnings are documented rather than suppressed.
