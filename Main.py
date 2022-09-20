import sys
from Components.MainWindow import MainWindow
from Components.LoginWindow import LoginWindow
from PySide2.QtWidgets import QApplication
login = False
if __name__ == "__main__":
    app = QApplication(sys.argv)
    wind = MainWindow()
    loginwind = LoginWindow()
    if not login:
        loginwind.show()
    else:
        wind.show()
    sys.exit(app.exec_())