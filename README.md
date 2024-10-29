

## README

### Keylogger and Server

This project consists of a keylogger that captures keystrokes and sends them to a remote server, as well as a Flask-based server to receive and log the data. The keylogger operates in a stealthy manner, buffering keystrokes into words and capturing the active window context before sending the logs to the server. This README provides all necessary details for setting up and running the components of this system.

---

### Table of Contents
1. [Overview](#overview)
2. [Keylogger Features](#keylogger-features)
3. [Server Features](#server-features)
4. [Setup](#setup)
    - [1. Environment Setup](#1-environment-setup)
    - [2. Running the Flask Server](#2-running-the-flask-server)
    - [3. Running the Keylogger](#3-running-the-keylogger)
5. [Dependencies](#dependencies)


---

### Overview

This repository consists of two main components:

1. **Keylogger**: A Python-based keylogger that captures keystrokes, accumulates them into words, and sends them to a remote server at regular intervals.
2. **Flask Server**: A server-side component that receives the keystrokes and stores them in a log file. The server listens for POST requests from the keylogger and handles logging accordingly.


---

### Keylogger Features

1. **Word Buffering**: Instead of sending individual keystrokes, the keylogger buffers characters into words. A word is defined by a space, enter, or punctuation keypress, allowing for more meaningful data to be sent.
   
2. **Active Window Detection**: The keylogger captures the title of the active window to give context on where the keystrokes are coming from (e.g., browser, text editor, etc.).

3. **Stealth Execution**: The logger is designed to run in the background and send logs periodically or after the buffer reaches a certain size.

4. **Backspace Handling**: Properly handles the backspace key, removing characters from the word buffer before logging.

5. **Cross-Platform Compatibility**: The keylogger can be run on both Windows and Linux, although Windows-specific features (like active window detection) rely on the `pywin32` library.

---

### Server Features

1. **HTTP POST Logging**: The server listens for POST requests from the keylogger and logs the received keystrokes in a file. This allows for remote logging, meaning the keylogger does not store logs locally.

2. **Simple and Lightweight**: Built using Flask, the server can be easily deployed on any environment that supports Python. It is minimalistic yet efficient.

3. **Log Storage**: Logs are written to a `server_keylogs.txt` file in the same directory as the Flask server. Each log entry contains both the word and the context of the active window from which the keystrokes were captured.

---

### Setup

#### 1. Environment Setup

To run both the keylogger and server, you need to have Python 3 installed on your machine. Additionally, you will need to install the required dependencies, which can be done using the `requirements.txt` file.

1. Clone the repository:
   ```bash
   git clone <https://github.com/Clasikpaige/Keylogger->
   cd <cd Keylogger>
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

#### 2. Running the Flask Server

1. Navigate to the server directory:
   ```bash
   cd server
   ```

2. Run the Flask server:
   ```bash
   python server.py
   ```

   By default, the server will run on `http://0.0.0.0:8080/`, and it will listen for incoming POST requests at the `/log` endpoint. This server logs all incoming data to the `server_keylogs.txt` file.

---

#### 3. Running the Keylogger

1. Ensure that the server is up and running on the designated IP and port.
   
2. Modify the `server_url` variable in the keylogger script to point to your server's IP address:
   ```python
   server_url = 'http://<your_server_ip>:8080/log'
   ```

3. Execute the keylogger:
   ```bash
   python keylogger.py
   ```

   For Windows users, you can convert this script into an executable `.exe` using tools like `pyinstaller` for stealthier operation. The keylogger will run in the background, capturing and sending keystrokes along with context to the server.

---

### Dependencies

The required dependencies for both the keylogger and the server are provided in the `requirements.txt` file. The keylogger requires `pynput` for keyboard event monitoring and `requests` for sending HTTP requests. On Windows, `pywin32` is needed to capture the active window.

```txt
Flask==2.0.2
pynput==1.7.6
requests==2.26.0
pywin32==302
subprocess32==3.5.4  # Optional for older Python versions on Windows
```

Install all dependencies using the following command:
```bash
pip install -r requirements.txt
```

---

