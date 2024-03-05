from flask import Flask, render_template
from flask_socketio import SocketIO,emit
from flask_cors import CORS

app = Flask(__name__)
app.run(debug=True)

@app.route("/")
def home():
    return render_template('home.html')