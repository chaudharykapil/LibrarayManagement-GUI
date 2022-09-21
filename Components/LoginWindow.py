from PySide2.QtWidgets import QDialog,QTextEdit,QLineEdit,QVBoxLayout,QLabel,QStyle,QPushButton
from PySide2.QtCore import Qt
from Style import LoginWindow as loginstyle
class LoginWindow(QDialog):
    def __init__(self) -> None:
        super().__init__()
        self.mainlayout = QVBoxLayout()
        self.setLayout(self.mainlayout)
        self.setProp()
        self.createUI()
        self.setcss()

    def setProp(self):
        self.setWindowTitle("Login")
        self.setGeometry(200,200,500,400)

    def createUI(self):
        self.formtitle = QLabel("Admin Login")
        self.formtitle.setBaseSize(500,100)
        self.formtitle.setAlignment(Qt.AlignCenter)
        self.usernamefield = QLineEdit()
        self.passwordfield = QLineEdit()
        self.submitbtn = QPushButton("Login")
        self.mainlayout.addWidget(self.formtitle)
        self.mainlayout.addWidget(self.usernamefield)
        self.mainlayout.addWidget(self.passwordfield)
        self.mainlayout.addWidget(self.submitbtn)

    def setcss(self):
        self.setStyleSheet(loginstyle.mainlayoutstyle)
        self.formtitle.setStyleSheet(loginstyle.formtitle)
        self.usernamefield.setStyleSheet(loginstyle.forminput)
        self.passwordfield.setStyleSheet(loginstyle.forminput)
        self.passwordfield.setEchoMode(QLineEdit.Password)
        self.submitbtn.setStyleSheet(loginstyle.submitbutn)