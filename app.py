from flask import Flask, jsonify
import random

app = Flask(__name__)

@app.route('/status')
def get_status():
    return jsonify({
        'CPU_Usage': f"{random.randint(10, 90)}%",
        'RAM_Usage': f"{random.randint(20, 95)}%",
        'Disk_Usage': f"{random.randint(30, 99)}%"
    })

@app.route('/run-diagnostics')
def run_diagnostics():
    return jsonify({
        'status': 'Healthy',
        'checks': {
            'CPU': 'OK',
            'RAM': 'OK',
            'Disk': 'OK',
            'Network': 'OK'
        }
    })

if __name__ == '__main__':
    app.run(debug=True)