from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import json

app = Flask(__name__)
cors = CORS(app)
app.config["CORS_HEADERS"] = "Content-Type"


# Load configuration from the config file
with open("config.json", "r") as config_file:
    config = json.load(config_file)

@app.route('/service', methods=['POST'])
def proxy():
    payload = request.json
    action = payload.get('action')

    if action in config:
        microservice_url = config[action]['url']
        query = payload.get('data', {})  # Assuming custom query parameters are in the payload
        url = microservice_url + config[action]['policy'].format(**query)
        response = requests.get(url)
        return (response.text)
    else:
        return jsonify({"error": "Action not configured"}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

