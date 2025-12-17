from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route("/")
def home():
    return "2-Tier Application Running Successfully"

app.run(host="0.0.0.0", port=5000)

