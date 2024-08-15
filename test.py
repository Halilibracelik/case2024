from flask import Flask, jsonify, request

app = Flask(__name__)

# GET / endpointi
@app.route('/', methods=['GET'])
def home():
    return jsonify({"msg": "BC4M"})

# GET /health endpointi
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"})

# POST endpointi
@app.route('/', methods=['POST'])
def echo():
    data = request.json  # JSON verisini al
    return jsonify(data)  # Gelen veriyi geri döndür
    

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

