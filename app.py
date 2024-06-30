from flask import Flask, request, redirect
from datetime import datetime

app = Flask(__name__)

def print_log():
    try:
        with open('scan_log.txt', 'r') as log_file:
            logs = log_file.read()
            print(logs)
    except Exception as e:
        print(f"An error occurred while reading logs: {e}")

@app.route('/')
def track():
    # Get user information
    user_ip = request.remote_addr
    user_agent = request.headers.get('User-Agent')
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    try:
        with open('scan_log.txt', 'a') as log_file:
            log_file.write(f'{timestamp} - {user_ip} - {user_agent}\n')
            print_log()  # Print logs after each entry
    except Exception as e:
        return f"An error occurred while logging: {e}", 500

    return redirect('https://lucky0-6.github.io/photo/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
