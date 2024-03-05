from flask import Flask, request, render_template, jsonify
from flask_socketio import SocketIO,emit
from flask_cors import CORS
from findWord import findWord

app = Flask(__name__)
app.run(debug=True)

@app.route("/")
def home():
    return render_template('home.html')


@app.route('/find', methods=['POST'])
def find_words():
    # Get the data from the request
    data = request.json
    
    findWord.findWord(data)
    
    # Return a response (for demonstration purposes)
    return jsonify({"message": "Arrays received successfully"})