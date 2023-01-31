from app import app
from app import routes
from flask_cors import CORS

if __name__ == "__main__":
    print(app.url_map)
    CORS(app)
    app.run(host='0.0.0.0', port=5000, debug=True)