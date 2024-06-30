from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

latest_coordinates = {"latitude": 26.769464, "longitude": 81.095838}

@app.route('/gps', methods=['POST'])
def receive_gps():
    global latest_coordinates
    data = request.get_json()
    latest_coordinates = {"latitude": data['longitude'], "longitude": data['latitude']}
    return jsonify({"status": "success"}), 200

@app.route('/coordinates', methods=['GET'])
def get_coordinates():
    return latest_coordinates

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=4000)
