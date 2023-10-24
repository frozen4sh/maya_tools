import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from_class=uic.loadUiType(r'D:\Justin\Python\VIVE_Python\QT_Test\test01.ui')[0]

class WindowClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

app=QApplication(sys.argv)
Ui_MainWindow=WindowClass()
Ui_MainWindow.show()
app.exec()