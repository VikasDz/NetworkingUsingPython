from flask import Flask, render_template

from flask_socketio import SocketIO, send


app = Flask(__name__)
app.config['']