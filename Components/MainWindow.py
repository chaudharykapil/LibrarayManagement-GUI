
import sys
from PySide2.QtWidgets import QApplication,QDialog, QLabel,QMainWindow,QVBoxLayout,QWidget,QPushButton
from PySide2.QtCore import Slot
from style.style import buttonstyle

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        widget = QWidget()
        self.mainlayout = QVBoxLayout()
        widget.setLayout(self.mainlayout)
        self.setCentralWidget(widget)
        self.setMainWindowProperty()
        self.AddButton()



    def AddButton(self):
        button = QPushButton("Press me")
        button.setFixedSize(50,50)
        button.setStyleSheet(buttonstyle)
        self.mainlayout.addChildWidget(button)


    def setMainWindowProperty(self):
        self.setGeometry(200,200,1000,600)
        self.setWindowTitle("Library Management")