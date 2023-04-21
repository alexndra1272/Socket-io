from flask import Flask, render_template
from flask_socketio import emit, join_room, SocketIO

app = Flask(__name__)

socket = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return render_template("index.html")