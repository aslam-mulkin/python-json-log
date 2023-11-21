from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

@app.route('/')
def generate_log():
    timestamp = time.strftime('%d/%b/%Y:%H:%M:%S %z')
    ip_address = f'{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}.{random.randint(1, 255)}'
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'

    log_entry = f'{ip_address} - - [{timestamp}] "GET /" 200 - "{user_agent}"'
    print(log_entry)

    return jsonify({'log_entry': log_entry})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
