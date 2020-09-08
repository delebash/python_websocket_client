import sys

# python -m pip install PySide2  #

from PySide2.QtWidgets import (QLineEdit, QPushButton, QApplication,
                               QVBoxLayout, QDialog)

# python -m pip install "python-socketio[client]"  #
from python_websocket_client import *

url = 'ws://localhost:5000'
transport = 'websocket'
myroom = "pythonclient"


class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.startbutton = QPushButton("start")
        self.stopbutton = QPushButton("stop")
        self.setFixedSize(300, 300)
        # Create layout and add widgets
        layout = QVBoxLayout()
        layout.addWidget(self.startbutton)
        layout.addWidget(self.stopbutton)
        # Set dialog layout
        self.setLayout(layout)
        # Add button signal to greetings slot
        self.startbutton.clicked.connect(self.start)
        self.stopbutton.clicked.connect(self.stop)

    def start(self):
        startclient(url, myroom, transport)

    def stop(self):
        stopclient()


app = QApplication(sys.argv)

window = Form()
window.show()

app.exec_()
