import json
from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/IA", methods=["POST"])
def read():
    try:
        data = json.loads(request.get_data())
        print(data)
        return "Hello, World!"
    except:
        print("An exception occurred")
        return "Error 404"