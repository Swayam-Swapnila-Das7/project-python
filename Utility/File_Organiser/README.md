
```markdown
# 📂 Automated File Organizer

A lightweight, robust, and zero-dependency Python utility designed to automatically declutter and organize files in a directory based on their extensions. 

Built using pure standard library modules (`os`, `shutil`, `pathlib`), this script runs dynamically, ignores system directories, and natively handles case-sensitivity edge cases.

---

## ✨ Features

* **Dynamic Directory Creation:** Automatically scans your extension mapping and builds *only* the folders required, avoiding bloated boilerplate code.
* **Case-Insensitive Normalization:** Seamlessly catches and moves uppercase extensions (e.g., `.PNG`, `.PDF`, `.ZIP`) instead of dumping them into Miscellaneous.
* **Self-Preservation Safeguard:** Programmatically detects its own file name (`Path(__file__).name`) to ensure it never accidentally moves itself mid-execution.
* **Directory Isolation:** Exclusively operates on flat files. Sub-folders and directories remain completely untouched.
* **Fail-Safe Architecture:** Wrapped in standard Python entry point conventions (`if __name__ == '__main__':`) for modularity and safety.

---

## 📁 Organized Folder Structure

When executed, the script categorizes your files into the following clean layout:

```text
📁 Current Directory/
│
├── 📁 Documents/      # .pdf, .txt, .xlsx, .pptx, .doc, .docx, .csv
├── 📁 Images/         # .jpeg, .png, .jpg, .gif, .svg, .webp
├── 📁 Audio/          # .mp3, .opus, .m4a
├── 📁 Video/          # .mp4, .mkv
├── 📁 Archive/        # .zip
├── 📁 Code/           # .py, .c, .html, .css, .js, .rs
└── 📁 Miscellaneous/  # Any file types not listed above

```
## 🚀 How To Use
### Prerequisites
 * Python 3.6 or higher installed on your system.
 * No external libraries are required (uses built-in modules).
### Setup & Execution
 1. Download or copy the file_organizer.py script.
 2. Drop the script directly into the messy folder you want to organize (e.g., your *Downloads* or *Desktop* folder).
 3. Open your terminal/command prompt, navigate to that directory, and run:
```bash
python file_organizer.py

```
## 🛠️ Implementation Details
 * **Fast Directory Scanning:** Utilizes os.scandir() instead of os.listdir() to efficiently fetch file system data, providing optimal performance even in folders with thousands of items.
 * **Path Safety:** Employs explicit string parsing adjustments alongside pathlib.Path objects to ensure cross-platform path resolution compatibility between Windows, macOS, and Linux.
## 📝 Important Notes
> ⚠️ **Scope of Operation:** This script operates strictly on a **single-level directory** (the folder it is currently running in). It will **not** recursively enter existing sub-folders, ensuring your nested project structures remain undisturbed.
> 
```

```
