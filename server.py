import time
import threading
import random
from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app, cors_allowed_origins='https://imaginative-cat-228fb6.netlify.app')

emitting = False
frequency = 10000
thread = None

def emit_message():
    global emitting
    global frequency
    while emitting:
        socketio.emit('message', random.uniform(0.1, 2))
        time.sleep(frequency / 1000)

@socketio.on('connect')
def handle_connect():
    global emitting
    print('Client connected')
    if not emitting:
        emitting = True
        thread = threading.Thread(target=emit_message)
        thread.start()

@socketio.on('disconnect')
def handle_disconnect():
    global emitting
    emitting = False
    print('Client disconnected')


@socketio.on('frequency')
def handle_message(data):
    global frequency
    frequency = data
    print(f'Received message: {data}')

@socketio.on('stop')
def handle_stop():
    global emitting
    emitting = False
    print(f'Stopped emitting')

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=8080)

