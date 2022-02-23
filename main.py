from PySide2 import QtWidgets
from PySide2.QtWidgets import QApplication, QWidget, QLineEdit, QPushButton, QListWidget,QHBoxLayout
import sys
import time


style = """

QPushButton {
    background: green;
}

"""

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pyside2 Simple Appplication")
        self.setGeometry(400, 400, 600, 500)
        self.setMinimumHeight(200)
        self.setMinimumWidth(350)
        self.setMaximumHeight(300)
        self.setMaximumWidth(1200)
        self.Button = QPushButton('Press Me')

        self.setLayout(QHBoxLayout())
        self.layout().addWidget(self.Button)

        self.List = QListWidget("Do not Press ME")
        # self.setQListWidget(QListWidget)
        self.layout().addItem(self.List)

        self.setStyleSheet(style)

myApp = QApplication(sys.argv)
window = Window()
window.show()

time.sleep(3)
window.resize(700, 900)
# window.repaint()

myApp.exec_()
sys.exit("Session is over")