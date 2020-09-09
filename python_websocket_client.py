# python -m pip install "python-socketio[client]" #

import socketio

sio = socketio.Client()


def startclient(url, myroom, transport):
    sio.connect(url, transports=transport)

    @sio.on('connect')
    def connect():
        print('Connected id  ', sio.sid)
        sio.emit('room', myroom)
        print('Joined room  ', myroom)

    @sio.on('message')
    def message(data):
        print('Received message!', data)

    @sio.on('join')
    def join(room):
        print('Joined room  ', room)

    @sio.on('connect_error')
    def connect_error():
        print("Connection failed!")

    @sio.on('disconnect')
    def disconnect():
        print("Disconnected!")
        sio.disconnect()


def stopclient():
    print("Disconnected!")
    sio.disconnect()
