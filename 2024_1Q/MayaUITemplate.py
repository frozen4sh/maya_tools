"""
Maya/QT UI template
Maya 2023
"""

import maya.cmds as cmds
import maya.mel as mel
from maya import OpenMayaUI as omui
from shiboken2 import wrapInstance
from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
from functools import partial # optional, for passing args during signal function calls
import sys

class MayaUITemplate(QtWidgets.QWidget):
    """
    Create a default tool window.
    """
    window = None
    
    def __init__(self, parent = None):
        """
        Initialize class.
        """
        super(MayaUITemplate, self).__init__(parent = parent)
        self.setWindowFlags(QtCore.Qt.Window)
        self.widgetPath = ('D:\\Justin\\Python\\VIVE_Python\\QT_Test\\demo.ui')
        self.widget = QtUiTools.QUiLoader().load(self.widgetPath)
        self.widget.setParent(self)
        # set initial window size
        self.resize(1000, 800)      
        # locate UI widgets
        self.btn_add = self.widget.findChild(QtWidgets.QPushButton, 'btn_add')        
        self.btn_close = self.widget.findChild(QtWidgets.QPushButton, 'btn_close')        
        # assign functionality to buttons
        self.btn_add.clicked.connect(self.add)
        self.btn_close.clicked.connect(self.closeWindow)
    
    """
    Your code goes here
    """
    def add(self):
        cmds.polySphere()
        print ('add pressed')

        
    def resizeEvent(self, event):
        """
        Called on automatically generated resize event
        """
        self.widget.resize(self.width(), self.height())
        
    def closeWindow(self):
        """
        Close window.
        """
        print ('closing window')
        self.destroy()
    
def openWindow():
    """
    ID Maya and attach tool window.
    """
    # Maya uses this so it should always return True
    if QtWidgets.QApplication.instance():
        # Id any current instances of tool and destroy
        for win in (QtWidgets.QApplication.allWindows()):
            if 'myToolWindowName' in win.objectName(): # update this name to match name below
                win.destroy()

    #QtWidgets.QApplication(sys.argv)
    mayaMainWindowPtr = omui.MQtUtil.mainWindow()
    mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
    MayaUITemplate.window = MayaUITemplate(parent = mayaMainWindow)
    MayaUITemplate.window.setObjectName('myToolWindowName') # code above uses this to ID any existing windows
    MayaUITemplate.window.setWindowTitle('Maya UI Template')
    MayaUITemplate.window.show()
    
openWindow()