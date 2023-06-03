from flask import Flask , jsonify , request
from data import data

app = Flask(__name__)

@app.route("/")

def index():
    return jsonify({
        "data" : data,
        "message" : "Success",
    }),200

@app.route("/GetStar")

def GetStar():
    name = request.args.get("name")
    pl = next(item for item in data if item["name"] == name)
    return jsonify({
        "data" : star ,
        "message" : "Success",
    }),200

app.run(debug = True)