
import sys
from PySide2.QtWidgets import QApplication,QDialog, QLabel,QMainWindow,QVBoxLayout,QWidget,QPushButton,QHBoxLayout
from PySide2.QtCore import Slot
from Style import mainWindow as style

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        widget = QWidget()
        self.mainlayout = QHBoxLayout()
        widget.setLayout(self.mainlayout)
        self.setCentralWidget(widget)
        self.setMainWindowProperty()
        self.makeLeftSection()
        self.makeRightSection()
        self.AddCss()

    def makeLeftSection(self):
        self.leftwidget = QWidget()
        self.leftLayout = QVBoxLayout()
        self.leftwidget.setLayout(self.leftLayout)
        self.mainlayout.addWidget(self.leftwidget)
    
    def makeRightSection(self):
        self.rightwidget = QWidget()
        self.rightwidget.setFixedSize(100,100)
        self.rightLayout = QVBoxLayout()
        self.rightwidget.setLayout(self.rightLayout)
        self.mainlayout.addWidget(self.rightwidget)

    def MakeHeader():
        pass


    def setMainWindowProperty(self):
        self.setGeometry(200,200,1000,600)
        self.setWindowTitle("Library Management")

    def AddCss(self):
        self.leftwidget.setStyleSheet(style.leftsection)
        self.rightwidget.setStyleSheet(style.rightsection)