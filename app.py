from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key' #can ignore for now, should be setup in the future though
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

# WebSocket event handlers
@socketio.on('send_json')
def handle_json(data):
    print(f'Received JSON: {data}')
    # Modify the received data and send a response backy
    response = {
        "status": "success",
        "received_data": data,
        "message": "JSON received and processed successfully"
    }
    emit('receive_json', response)

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)
