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
        self.btn_addBone = self.widget.findChild(QtWidgets.QPushButton, 'btn_addBone')        
        self.btn_addCtrl = self.widget.findChild(QtWidgets.QPushButton, 'btn_addCtrl')        
        self.btn_close = self.widget.findChild(QtWidgets.QPushButton, 'btn_close')        
        self.scroll_list_bone = self.widget.findChild(QtWidgets.QListWidget,'scroll_list_L')
        self.scroll_list_ctrl = self.widget.findChild(QtWidgets.QListWidget,'scroll_list_R')
        # assign functionality to buttons
        self.btn_addBone.clicked.connect(self.addBone)
        self.btn_addCtrl.clicked.connect(self.addCtrl)
        self.btn_close.clicked.connect(self.closeWindow)
        self.bone_list = []  # Replace with your bone names
        
        
        # Add items to the list
        self.items = ['Item 1', 'Item 2', 'Item 3']
        


    
    """
    Your code goes here
    """
    def addBone(self):
        # cmds.polySphere()
        # print ('Add Bone Button is pressed')
        
        # Get the selected bone
        selected_bone = cmds.ls(selection=True, type="joint")
        if not selected_bone:
            cmds.warning("Please select a bone.")
            return
        
        print("a")
        self.scroll_list_bone.addItem(selected_bone[0])

        # Add the selected bone to the bone_list
        # self.scroll_list_bone.addItems(selected_bone[0])
        

        

        # Update the bone text scroll list with the new data
        # self.update_text_scroll_list(self.scroll_list_bone, self.bone_list)

        print(f"Bone '{selected_bone[0]}' added to the list.")
    
    def addCtrl(self):
        # cmds.polySphere()
        # print ('Add Bone Button is pressed')
        
        # Get the selected bone
        selected_ctrl = cmds.ls(selection=True, type="transform")
        if not selected_ctrl:
            cmds.warning("Please select a controller.")
            return
        
        print("a")
        self.scroll_list_ctrl.addItem(selected_ctrl[0])

        # Add the selected bone to the bone_list
        # self.scroll_list_bone.addItems(selected_bone[0])
        

        

        # Update the bone text scroll list with the new data
        # self.update_text_scroll_list(self.scroll_list_bone, self.bone_list)

        print(f"Bone '{selected_ctrl[0]}' added to the list.")
       

    def update_text_scroll_list(self, text_scroll_list, data_list):
        # Update the text scroll list with the given data list
        # cmds.textScrollList(text_scroll_list, edit=True, removeAll=True)
        # cmds.textScrollList(text_scroll_list, edit=True, append=data_list)
        pass

  

        
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