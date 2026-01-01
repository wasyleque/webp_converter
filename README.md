# webp_converter
Mass convert Your jpg, png graphics files to recover free space on Your hard drive, as an extra function the script modyfying the Fooocus log.html if found any and update with .webp instead of jpeg and png.

# Installation and Usage Guide

This guide will walk you through setting up and running the conversion script on both Linux and Windows using a Python virtual environment.

## 1. Prerequisites

- Python 3.6+ installed on your system.
- The script file (`converter.py`) and `requirements.txt` in the same directory.

## 2. Setup and Installation

Follow the steps for your operating system.

### On Linux / macOS

1.  **Open a terminal** and navigate to the directory containing the script.

2.  **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    ```

3.  **Activate the virtual environment:**
    ```bash
    source venv/bin/activate
    ```
    Your terminal prompt should now be prefixed with `(venv)`.

4.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

### On Windows

1.  **Open Command Prompt (cmd) or PowerShell** and navigate to the directory containing the script.

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    ```powershell
    # For PowerShell
    .\venv\Scripts\Activate.ps1
    
    # For Command Prompt (cmd.exe)
    .\venv\Scripts\activate.bat
    ```
    Your terminal prompt should now be prefixed with `(venv)`.

4.  **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

## 3. Running the Script

Make sure your virtual environment is activated before running the script.

### Standard Conversion

This will convert all `.png` and `.jpeg` images to `.webp` in all subdirectories. The original files will be kept.

```bash
python converter.py
```

### Conversion with Auto-Remove

This will convert the images and **delete the original `.png` and `.jpeg` files** after a successful conversion.

```bash
python converter.py --autoremove
```

A summary of the reclaimed disk space will be displayed at the end.

## 4. Deactivating the Virtual Environment

When you are finished, you can deactivate the virtual environment by simply running:

```bash
deactivate
```
