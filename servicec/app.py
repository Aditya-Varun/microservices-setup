from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"message": "Service C is running!"}), 200

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify({"service": "C", "data": "Hello from Service C"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8003)
