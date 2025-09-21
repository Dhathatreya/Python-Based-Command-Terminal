# MyTerminal 🐍

A powerful, modular, and extensible command-line terminal built in Python.

This project is a fully functional command terminal created for the CodeMate Hackathon. It mimics the behavior of a real system terminal, providing support for file system operations, system monitoring, and more. The project features a highly modular, plugin-based architecture where each command is its own self-contained file, making it incredibly easy to extend.

---

## ✨ Features

### File System Operations
* **`pwd`**: Print the name of the current working directory.
* **`ls`**: List the contents of the current directory.
* **`cd <path>`**: Change the current directory.
* **`mkdir <name>`**: Create a new directory.
* **`rm <name>`**: Remove a file or an empty directory.

### System Monitoring
* **`cpu`**: Display real-time CPU utilization, updating on a single line.
* **`mem`**: Display real-time memory usage (percentage, total, and available), updating on a single line.
* **`ps`**: List the top 15 currently running processes.

### Terminal Features
* **`history`**: View a numbered list of all commands used in the current session.
* **`exit`**: Gracefully exit the terminal.

### Core Architecture
* **Dynamic Command Loading**: The terminal automatically discovers and loads all commands from the `commands/` directory at startup.
* **Extensible Plugin System**: Adding new commands is as simple as adding a new file.

---

## 🚀 Getting Started

Follow these steps to get a local copy up and running.

### Prerequisites
* Python 3.8 or higher
* pip (Python package installer)

### Installation Steps

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/Dhathatreya/Python-Based-Command-Terminal.git](https://github.com/Dhathatreya/Python-Based-Command-Terminal.git)
    ```

2.  **Navigate to the project directory:**
    ```sh
    cd Python-Based-Command-Terminal
    ```

3.  **Create a `requirements.txt` file:**
    The project depends on the `psutil` library. Create a file to manage this dependency.
    ```sh
    echo psutil > requirements.txt
    ```

4.  **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

---

## 💻 Usage

To start the terminal, run the `main.py` script from the root of the project directory:

```sh
python main.py
