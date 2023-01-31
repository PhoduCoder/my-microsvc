import os
from app import app
from flask import Flask, jsonify
from flask_cors import CORS

#app = Flask(__name__)

#CORS(app)

CORS(app, origins=["http://54.198.65.206:8080"], methods=["GET"])

@app.route("/data")
def data():
    data = [{"id": 1, "name": "Item 1"}, {"id": 2, "name": "Item 2"}]
    print ("Checking execution entry")
    return jsonify(data)


#commented by gaurav
# if __name__ == "__main__":
#     port = int(os.environ.get("PORT", 5000))
#     app.run(host='0.0.0.0', port=port)