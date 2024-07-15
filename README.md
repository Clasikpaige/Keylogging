

---

# Keylogger PDF Embed Project

Welcome to the Keylogger PDF Embed Project! This guide will walk you through setting up a keylogger embedded within a PDF file. We'll cover everything from creating the keylogger script, generating a malicious PDF, and setting up a server to log keystrokes. Let’s get started!

## Table of Contents

- [Introduction](#introduction
- [Prerequisites](#prerequisites)
- [Platform Compatibility](#platform-compatibility)

## Introduction

This project allows you to create a PDF that when opened, runs a keylogger and sends the captured keystrokes to your server. 

## Prerequisites

Before you get started, ensure you have the following:

- Python 3.x
- `pyinstaller` for compiling the keylogger
- `PyPDF2` for manipulating PDFs
- `Flask` for running the server
- A PDF reader that supports JavaScript (like Adobe Acrobat)


2. **Compile the Keylogger Script**

Navigate to the `keylogger` directory and run:

```
pip install pyinstaller
pyinstaller --onefile keylogger.py
```

This will generate `keylogger/dist/keylogger.exe`.

## Platform Compatibility

This setup primarily works on Windows due to the use of ActiveXObject in the JavaScript code for PDF. However, the keylogger script itself can be adapted to work on Linux and macOS with some modifications, but the PDF execution part will need a different approach as ActiveX is not supported on these platforms. 

## Disclaimer

This project is intended for educational purposes only. 
