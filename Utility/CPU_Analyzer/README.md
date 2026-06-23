```markdown
# Linux & Android CPU Information Utility

A lightweight, interactive Command Line Interface (CLI) tool designed to retrieve, format, and export detailed system hardware and CPU specifications. Built natively using Python's standard libraries, this script provides a robust alternative to manually running system diagnostic commands, featuring custom terminal styling and defensive error handling.

## 🚀 Features

- **Interactive CLI Menu:** Smooth navigation utilizing Python's modern `match-case` structural pattern matching.
- **Cross-Platform Safety Wrapper:** Active hardware detection targeting Linux and Android environments while preventing execution failures on unsupported hosts.
- **Dynamic Terminal Reporting:** Color-coded, organized terminal rendering of system specifications derived from native `lscpu` execution.
- **Diagnostic Logging:** Generates standalone, structured text reports (`cpu_details.txt`) stamped with localized dynamic generation timestamps.
- **Robust Error Handling:** Completely sandboxed initialization blocks to safeguard execution loops against missing dependencies or OS restrictions.

## 📁 Repository Structure

```text
project-python/
└── Utility/
    └── CPU_Analyzer 
          └── cpu_analyzer.py   # Main executable utility script

```
## 🛠️ Requirements & Dependencies
The script relies completely on built-in Python standard libraries. No external pip installations are required.
 * **Python Version:** Python 3.10 or higher (required for match-case syntax)
 * **Environment:** Linux-based operating systems or Android terminal emulators (e.g., Termux) with the lscpu package installed.
## 💻 Usage
 1. Clone the repository and navigate to the project directory:
   ```bash
   git clone [https://github.com/Swayam-Swapnila-Das7/project-python.git](https://github.com/Swayam-Swapnila-Das7/project-python.git)
   cd project-python/Utility/CPU_Analyzer
   
   ```
 2. Execute the script:
   ```bash
   python3 cpu_analyzer.py
   
   ```
 3. Select an operation from the interactive interface:
   * **1** : Fetch and print raw hardware specifications directly to the terminal shell.
   * **2** : Export an aligned hardware inventory report as a .txt log file.
   * **3** : Terminate the interactive loop and close the terminal session safely.
## 🛡️ Structural Guardrails
 * **Caching Mechanisms:** Fetches system subprocess trees precisely once per selection cycle to reduce execution bottlenecks and context overhead.
 * **Terminal Escape Protections:** Implements automated virtual terminal processing overrides to preserve color output rendering across restrictive terminal emulators.
```

```
