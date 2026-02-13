from flask import Flask, jsonify

app = Flask(__name__)

DATA = [
    {"id": 1, "campus": "MMC", "lat": 25.76, "lng": -80.36},
    {"id": 2, "campus": "BBC", "lat": 25.90, "lng": -80.13},
    {"id": 3, "campus": "DC", "lat": 38.89, "lng": -77.01}
]

next_id = 4

@app.route("/")
def index():
    return """
    <h1>FIU Campus API</h1>
    <p>Try these endpoints:</p>
    <ul>
        <li><a href="/api/health">/api/health</a></li>
        <li><a href="/api/data">/api/data</a></li>
        <li><a href="/api/data/1">/api/data/1</a></li>
    </ul>
    """

@app.route("/api/hello")
def health():
    return jsonify({"Welcome": "My name is Brandon Delgado and welcome to my first ever Flask app!"}), 200

@app.route("/api/data")
def items():
    return jsonify(DATA), 200

@app.route("/api/data/<int:id>")
def item(id):
    for i in DATA:
        if i["id"] == id:
            return jsonify(i), 200
    return jsonify({"Error": "Data not found"}), 404

if __name__ == "__main__":
    app.run(debug=True, port=6767)