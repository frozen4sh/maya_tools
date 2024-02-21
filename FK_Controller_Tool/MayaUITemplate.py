"""
Justin's FK -> Controller Tool
Created by Justin Yehun Hwang 20/02/2024
This tool helps to connect between controller and exist bone animaiton.

# future update list
1. Save and load list to/from CSV 
2. Window size change

Maya/QT UI template
Maya 2023
"""

import maya.cmds as cmds
import maya.mel as mel
import maya.api.OpenMaya as om

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
        self.widgetPath = ('FK_Controller_Tool.ui')
        self.widget = QtUiTools.QUiLoader().load(self.widgetPath)
        self.widget.setParent(self)
        
        # set initial window size
        self.resize(1000, 800)      
        
        # locate UI widgets
        self.btn_addBone = self.widget.findChild(QtWidgets.QPushButton, 'btn_addBone')        
        self.btn_addCtrl = self.widget.findChild(QtWidgets.QPushButton, 'btn_addCtrl')        
        self.btn_connect = self.widget.findChild(QtWidgets.QPushButton, 'btn_connect')        
        self.btn_clearList = self.widget.findChild(QtWidgets.QPushButton, 'btn_clearList')        
        self.btn_close = self.widget.findChild(QtWidgets.QPushButton, 'btn_close')        
        self.scroll_list_bone = self.widget.findChild(QtWidgets.QListWidget,'scroll_list_L')
        self.scroll_list_ctrl = self.widget.findChild(QtWidgets.QListWidget,'scroll_list_R')
        
        # assign functionality to buttons
        self.btn_addBone.clicked.connect(self.addBone)
        self.btn_addCtrl.clicked.connect(self.addCtrl)
        self.btn_connect.clicked.connect(self.connect)
        self.btn_clearList.clicked.connect(self.clearList)
        self.btn_close.clicked.connect(self.closeWindow)
        self.bone_list = []  # Replace with your bone names         
      
        
        # Add items to the list
        self.items = ['Item 1', 'Item 2', 'Item 3']
        


    
    """
    Your code goes here
    """
    def addBone(self):
        
        # Get the selected bone
        selected_bone = cmds.ls(selection=True, type="joint")
        if not selected_bone:
            cmds.warning("Please select a bone.")
            return
                
        self.scroll_list_bone.addItem(selected_bone[0])


        print(f"Bone '{selected_bone[0]}' added to the list.")
    
    def addCtrl(self):
                
        # nurbsCurve Finder
        somethingSelected = om.MGlobal.getActiveSelectionList()
        obj = somethingSelected.getDependNode(0)
        shape = om.MFnDagNode(obj).child(0)
        mfnDepNode = om.MFnDependencyNode(shape)
        typeName = mfnDepNode.typeName

        selected_ctrl = cmds.ls(selection=True)

        # Get the selected ctrl
        if typeName == "nurbsCurve":
            self.scroll_list_ctrl.addItem(selected_ctrl[0])            


        if not typeName == "nurbsCurve":
            cmds.warning("Please select a controller.")
            return          
       

        print(f"Bone '{selected_ctrl[0]}' added to the list.")
    
    def connect(self):
        # Connect each pair of bone and controller using parent constraint
        
        
        item_count = self.scroll_list_ctrl.count()
        ctrl_items = [self.scroll_list_ctrl.item(i).text() for i in range(item_count)]
        print("Items in QListWidget:", ctrl_items) 
        
        bone_items = [self.scroll_list_bone.item(i).text() for i in range(item_count)]
        print("Items in QListWidget:", bone_items) 


        for bone, controller in zip(bone_items, ctrl_items):
            if cmds.objExists(bone) and cmds.objExists(controller):
                # Check if the pair exists and apply parent constraint
                constraint = cmds.parentConstraint(bone, controller, maintainOffset=True)
                print(f"Connected: {bone} -> {controller}")
            else:
                cmds.warning(f"Skipping connection for pair: {bone} -> {controller}. One or both objects do not exist.")

        print("Connection completed.")
        self.clearList()        



    def clearList(self):
        # clear both lists
        self.scroll_list_bone.clear()
        self.scroll_list_ctrl.clear()
        print("List Cleared")    
    

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
    MayaUITemplate.window.setWindowTitle('Justin\'s FK -> Controller Tool')
    MayaUITemplate.window.show()
    
openWindow()