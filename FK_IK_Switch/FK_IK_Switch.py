"""
Justin's FK <-> IK Switch Tool
Created by Justin Yehun Hwang 25/03/2024
This tool helps to switch between FK and IK controller's key animaiton.

# future update list

FK-> IK 전환 시나리오 (수정안 2024.04.22)
로케이터를 2개 생성한다. ik_foot_loc, ik_pv_loc
cmds.spaceLocator(n='ik_foot_loc')
cmds.spaceLocator(n='ik_pv_loc')

FKIKLeg_R 의 FKIKBlend 수치를 10으로 맞춰서 IK모드로 변경 시킨다.
cmds.setAttr('FKIKLeg_R.FKIKBlend', 10)



ik_foot_loc를 IKLeg_R에 패런트 시킨다.
cmds.parent('ik_foot_loc','IKLeg_R')
위치값 및 로테이션 값을 000으로 한다.
cmds.setAttr('ik_foot_loc.translate', 0, 0, 0, type="double3")
cmds.setAttr('ik_foot_loc.rotate', 0, 0, 0, type="double3")
ik_foot_loc를 Ankle_R에 패런트 시킨다.
cmds.parent('ik_foot_loc','Ankle_R')

ik_pv_loc를 PoleLeg_R에 패런트 시킨다.
cmds.parent('ik_pv_loc','PoleLeg_R')
위치값 000 으로 맞춘다
cmds.setAttr('ik_pv_loc.translate', 0, 0, 0, type="double3")
ik_foot_loc를 Knee_R에 패런트 시킨다.
cmds.parent('ik_pv_loc','Knee_R')
위치값 000 으로 맞춘다
cmds.setAttr('ik_pv_loc.translate', 0, 0, 0, type="double3")


FKIKLeg_R 의 FKIKBlend 수치를 0으로 맞춰서 FK모드로 변경 시킨다.
cmds.setAttr('FKIKLeg_R.FKIKBlend', 0)

a=pm.parentConstraint('ik_foot_loc','IKLeg_R',mo=0)
b=pm.pointConstraint('ik_pv_loc','PoleLeg_R',mo=0)
pm.delete(a)
pm.delete(b)

해준다.

해당 작업을 키가 있는곳만 위의 내용을 반복 시키고 키를 찍는다.
전부 키를 찍으면 로케이터 2개를 삭제한다.





FK -> IK 전환 시나리오 (초안)
1. FK -> IK의 경우 임시 로케이터 두개를 생성한다. 
2. 생성한 임시 로케이터를 각각 발목과 무릎에 배치하고 컨트롤러의 TR 값과 동일하게 맞춘다. 
3. 발목 컨트롤러 키를 발목 임시 로케이터에 복사한다.
4. 무릎 컨트롤러의 키를 무릎 임시 로케이터에 복사한다.
5. Attribute 를 이용하여 FK -> IK 로 전환 시킨다.
6. 발목 임시 로케이터와 발IK컨트롤러를 Parent 컨스트레인 시킨다.
7. 무릎 임시 로케이터와 다리 폴벡터를 Point 컨스트레인 시킨다.
8. 베이크 시킨다.
9. 임시 로케이터들을 삭제한다.


FK -> IK 전환 시나리오 (수정안)
1. Frame Range 제일 처음으로 간다.
2. FK컨트롤러에 키가 있는 프레임으로 간다.
3. FK컨트롤러에 키가 없다면 다음프레임으로 간다.
4. FK발목 조인트 위치를 저장한다.
5. FK무릎 조인트 위치를 저장한다.
6. Attribute 를 이용하여 FK -> IK 로 전환 시킨다.
7. 저장된 FK발목 조인트 위치를 발IK컨트롤러에 붙여넣고 키를 준다.
8. 저장된 FK무릎 조인트 위치를 다리 폴벡터에 붙여넣고 키를 준다.
9. Frame Range 제일 끝까지 2~8 반복


프레임마다 fK컨트롤러 위치를 프린트 한다 ok





Maya/QT UI template
Maya 2023
"""

import maya.cmds as cmds

def createLocators():
    print('createLocators')
    cmds.spaceLocator(n='ik_foot_loc')
    cmds.spaceLocator(n='ik_pv_loc')

def parentLocators():
    print('parentLocators')
    cmds.setAttr('FKIKLeg_R.FKIKBlend', 10)

    cmds.parent('ik_foot_loc','IKLeg_R')
    cmds.setAttr('ik_foot_loc.translate', 0, 0, 0, type="double3")
    cmds.setAttr('ik_foot_loc.rotate', 0, 0, 0, type="double3")
    cmds.parent('ik_foot_loc','Ankle_R')
      
    cmds.parent('ik_pv_loc','PoleLeg_R')
    cmds.setAttr('ik_pv_loc.translate', 0, 0, 0, type="double3")
    cmds.parent('ik_pv_loc','Knee_R')
    cmds.setAttr('ik_pv_loc.translate', 0, 0, 0, type="double3")

    cmds.setAttr('FKIKLeg_R.FKIKBlend', 0)

def repeateAndKey():
    # # Constraint locator and IK controller
    a=cmds.parentConstraint('ik_foot_loc','IKLeg_R',mo=0)
    b=cmds.pointConstraint('ik_pv_loc','PoleLeg_R',mo=0)

    # Key 2 controllers
    cmds.setKeyframe('IKLeg_R')
    cmds.setKeyframe('PoleLeg_R')

    # Delete constraints
    cmds.delete(a)
    cmds.delete(b)   

def deleteConstraintLocators():
    
    # Delete locators
    cmds.delete('ik_foot_loc')
    cmds.delete('ik_pv_loc')



# Get the start and end frames of the timeline
start_frame = cmds.playbackOptions(query=True, minTime=True)
print('start_frame=',start_frame)
end_frame = cmds.playbackOptions(query=True, maxTime=True)
print('end_frame=',end_frame)

# Iterate over each frame in the timeline

createLocators()
parentLocators()

for frame in range(int(start_frame), int(end_frame) + 1):
    cmds.currentTime(frame)

    print('frame=',frame)
    repeateAndKey()

deleteConstraintLocators()



# import maya.cmds as cmds
# import maya.mel as mel
# import maya.api.OpenMaya as om
# import csv
# import os
# import pymel as pm

# from maya import OpenMayaUI as omui
# from shiboken2 import wrapInstance
# from PySide2 import QtUiTools, QtCore, QtGui, QtWidgets
# from functools import partial # optional, for passing args during signal function calls
# import sys

# class FK_IK_Switch(QtWidgets.QWidget):
#     """
#     Create a default tool window.
#     """
#     window = None
    
#     def __init__(self, parent = None):
#         """
#         Initialize class.
#         """
#         super(FK_IK_Switch, self).__init__(parent = parent)
#         self.setWindowFlags(QtCore.Qt.Window)
#         self.widgetPath = ('FK_IK_Switch_renew.ui')
#         self.widget = QtUiTools.QUiLoader().load(self.widgetPath)
#         self.widget.setParent(self)
        
#         # set initial window size
#         self.resize(1000, 800)      
        
#         # locate UI widgets
#         self.btn_addUFK = self.widget.findChild(QtWidgets.QPushButton, 'btn_addUFK')
#         self.btn_addLFK = self.widget.findChild(QtWidgets.QPushButton, 'btn_addLFK')

#         self.btn_addUIK = self.widget.findChild(QtWidgets.QPushButton, 'btn_addUIK')
#         self.btn_addLIK = self.widget.findChild(QtWidgets.QPushButton, 'btn_addLIK')

#         self.btn_switch = self.widget.findChild(QtWidgets.QPushButton, 'btn_switch')
#         self.btn_saveCSV = self.widget.findChild(QtWidgets.QPushButton, 'btn_saveCSV')
#         self.btn_loadCSV = self.widget.findChild(QtWidgets.QPushButton, 'btn_loadCSV')
#         self.btn_clearList = self.widget.findChild(QtWidgets.QPushButton, 'btn_clearList')
#         self.btn_close = self.widget.findChild(QtWidgets.QPushButton, 'btn_close')


#         self.scroll_list_UFK = self.widget.findChild(QtWidgets.QListWidget,'scroll_list_UFK')
#         self.scroll_list_LFK = self.widget.findChild(QtWidgets.QListWidget,'scroll_list_LFK')
#         self.scroll_list_UIK = self.widget.findChild(QtWidgets.QListWidget,'scroll_list_UIK')
#         self.scroll_list_LIK = self.widget.findChild(QtWidgets.QListWidget,'scroll_list_LIK')
#         self.UFK_locator_list =[]
#         self.LFK_locator_list =[]
#         self.UIK_locator_list =[]
#         self.LIK_locator_list =[]
#         self.selected_UIK = []
#         self.selected_LIK = []


        
#         # assign functionality to buttons
#         self.btn_addUFK.clicked.connect(self.addUFK)
#         self.btn_addLFK.clicked.connect(self.addLFK)
#         self.btn_addUIK.clicked.connect(self.addUIK)
#         self.btn_addLIK.clicked.connect(self.addLIK)

#         self.btn_switch.clicked.connect(self.switch)
#         self.btn_saveCSV.clicked.connect(self.saveCSV)
#         self.btn_loadCSV.clicked.connect(self.loadCSV)
#         self.btn_clearList.clicked.connect(self.clearList)
#         self.btn_close.clicked.connect(self.closeWindow)
#         # self.FK_list = []  # Replace with your bone names         
#         self.FK_items =[]
#         self.IK_items =[]

             
#         # Add items to the list
#         self.items = ['Item 1', 'Item 2', 'Item 3']

#         # Set the time range to bake
#         self.start_frame = cmds.playbackOptions(q=True, min=True)
#         self.end_frame = cmds.playbackOptions(q=True, max=True)
        


    
#     """
#     Your code goes here
#     """
#     def addUFK(self):
#         print("addUFK Button Clicked")
        
#         # nurbsCurve Finder
#         somethingSelected = om.MGlobal.getActiveSelectionList()
#         obj = somethingSelected.getDependNode(0)
#         shape = om.MFnDagNode(obj).child(0)
#         mfnDepNode = om.MFnDependencyNode(shape)
#         typeName = mfnDepNode.typeName

#         selected_UFK = cmds.ls(selection=True)

#         # Get the selected ctrl
#         if typeName == "nurbsCurve":
#             self.scroll_list_UFK.addItem(selected_UFK[0])
#             # Create locator and Constraint
#             cmds.spaceLocator(n=selected_UFK[0]+'_lo')
#             cmds.parentConstraint(selected_UFK[0], selected_UFK[0]+'_lo', maintainOffset=False)
#             self.UFK_locator_list.append(selected_UFK[0]+'_lo')
#             print(self.UFK_locator_list)    

#         # warn for none nurbsCurve 
#         if not typeName == "nurbsCurve":
#             cmds.warning("Please select a controller.")
#             return                    

#         print(f"'{selected_UFK[0]}' added to the list.")

#     def addLFK(self):
#         print("addLFK Button Clicked")

#         # nurbsCurve Finder
#         somethingSelected = om.MGlobal.getActiveSelectionList()
#         obj = somethingSelected.getDependNode(0)
#         shape = om.MFnDagNode(obj).child(0)
#         mfnDepNode = om.MFnDependencyNode(shape)
#         typeName = mfnDepNode.typeName

#         selected_LFK = cmds.ls(selection=True)

#         # Get the selected ctrl
#         if typeName == "nurbsCurve":
#             self.scroll_list_LFK.addItem(selected_LFK[0])
#             # Create locator and Constraint
#             cmds.spaceLocator(n=selected_LFK[0]+'_lo')
#             cmds.parentConstraint(selected_LFK[0], selected_LFK[0]+'_lo', maintainOffset=False)
#             self.LFK_locator_list.append(selected_LFK[0]+'_lo')
#             print(self.LFK_locator_list)    

#         # warn for none nurbsCurve 
#         if not typeName == "nurbsCurve":
#             cmds.warning("Please select a controller.")
#             return                             

#         print(f"'{selected_LFK[0]}' added to the list.")
        
#     def addUIK(self):
#         print("addUIK Button Clicked")
               
                
#         self.selected_UIK = cmds.ls(selection=True)
#         self.scroll_list_UIK.addItem(self.selected_UIK[0])            

#         print(f"'{self.selected_UIK[0]}' added to the list.")

#     def addLIK(self):
#         print("addLIK Button Clicked")
         
        
#         self.selected_LIK = cmds.ls(selection=True)
#         self.scroll_list_LIK.addItem(self.selected_LIK[0])            

#         print(f"'{self.selected_LIK[0]}' added to the list.")
    
#     def switch(self):
#         print("Switch Button Clicked")


#         cmds.spaceLocator(n='ik_foot_loc')
#         cmds.spaceLocator(n='ik_pv_loc')


#         cmds.parent('ik_foot_loc','IKLeg_R')
#         cmds.setAttr('ik_foot_loc.translate', 0, 0, 0, type="double3")
#         cmds.setAttr('ik_foot_loc.rotate', 0, 0, 0, type="double3")
#         cmds.parent('ik_foot_loc','Ankle_R')
#         cmds.setAttr('ik_foot_loc.translate', 0, 0, 0, type="double3")


#         cmds.parent('ik_pv_loc','PoleLeg_R')
#         cmds.setAttr('ik_pv_loc.translate', 0, 0, 0, type="double3")
#         cmds.parent('ik_pv_loc','Knee_R')
#         cmds.setAttr('ik_pv_loc.translate', 0, 0, 0, type="double3")


#         a=pm.parentConstraint('ik_foot_loc','IKLeg_R',mo=0)
#         b=pm.pointConstraint('ik_pv_loc','PoleLeg_R',mo=0)
#         pm.delete(a)
#         pm.delete(b)

                   
#         self.collect()

#         print(self.FK_items, self.IK_items)
       
#         # Connect each pair of FK and IK using parent constraint
#         for FK, IK in zip(self.FK_items, self.IK_items):
#             if cmds.objExists(FK) and cmds.objExists(IK):
                
#                 # Check if the pair exists and apply parent constraint
#                 constraint = cmds.parentConstraint(self.LFK_locator_list, self.selected_LIK, maintainOffset=False)
#                 constraint = cmds.pointConstraint(self.UFK_locator_list, self.selected_UIK, maintainOffset=False)
                
#                 print(f"Connected: {self.UFK_locator_list} -> {self.selected_UIK}")
#                 print(f"Connected: {self.LFK_locator_list} -> {self.selected_LIK}")


#                 # Bake the controllers
#                 # cmds.bakeResults(self.selected_UIK, sm=True, t=(self.start_frame, self.end_frame), at=["tx", "ty", "tz"], sb=1 )
#                 # cmds.bakeResults(self.selected_LIK, sm=True, t=(self.start_frame, self.end_frame), at=["tx", "ty", "tz", "rx","ry","rz"], sb=1 )
                

#                 # Delete locators
#                 # cmds.delete(self.UFK_locator_list)
#                 # cmds.delete(self.LFK_locator_list)

#                 # Clear list
#                 self.clearList()
                


                
#             else:
#                 cmds.warning(f"Skipping connection for pair: {FK} -> {IK}. One or both objects do not exist.")
        
#     def collect(self):
        
#         # Collect items from the UI QListWidget
#         item_count = self.scroll_list_UIK.count()
#         self.IK_items = [self.scroll_list_UIK.item(i).text() for i in range(item_count)]
#         print("IK Items in QListWidget:", self.IK_items)

#         self.FK_items = [self.scroll_list_UFK.item(i).text() for i in range(item_count)]
#         print("FK Items in QListWidget:", self.FK_items)

#     def saveCSV(self):

#         self.collect()


#         # Specify the file name
#         file_name = "D:/Justin/output.csv"

#         # Transpose the data (switch rows and columns)
#         combine_lists = [self.FK_items, self.IK_items]
#         transposed_data = list(map(list, zip(*combine_lists)))

#         print(combine_lists)
#         print(transposed_data)

#         # Open the file in write mode with newline='' to avoid extra newline characters
#         with open(file_name, mode='w', newline='') as file:
#             # Create a CSV writer object
#             csv_writer = csv.writer(file)

#             # Write each row in the transposed data to the CSV file
#             csv_writer.writerows(transposed_data)

#         print(f"The list has been successfully saved to {file_name}.")
        
#     def loadCSV(self):
#          # Specify the file name
#         file_name = "D:/Justin/output.csv"

#         # Check if the file exists
#         if not os.path.exists(file_name):
#             return

#         # Open the file in read mode
#         with open(file_name, mode='r') as file:
#             # Create a CSV reader object
#             csv_reader = csv.reader(file)

#             # Read the rows from the CSV file
#             rows = list(csv_reader)

#             # Ensure there is data in the file
#             if len(rows) > 0:
#                 # Separate the transposed data back into bone and ctrl items
#                 self.FK_items, self.IK_items = zip(*rows)

#                 # Populate the QListWidgets with the loaded data
#                 self.clearList()
#                 self.scroll_list_UFK.addItems(self.FK_items)
#                 self.scroll_list_UIK.addItems(self.IK_items)

#             print(f"The list has been successfully loaded from {file_name}.")
    
#     def clearList(self):
#         # clear both lists
#         self.scroll_list_UFK.clear()
#         self.scroll_list_LFK.clear()
#         self.scroll_list_UIK.clear()
#         self.scroll_list_LIK.clear()
#         self.UFK_locator_list =[]
#         self.LFK_locator_list =[]
#         self.UIK_locator_list =[]
#         self.LIK_locator_list =[]
#         self.selected_UIK = []
#         self.selected_LIK = []
#         print("List Cleared")    
    
#     def update_text_scroll_list(self, text_scroll_list, data_list):
#         # Update the text scroll list with the given data list
#         # cmds.textScrollList(text_scroll_list, edit=True, removeAll=True)
#         # cmds.textScrollList(text_scroll_list, edit=True, append=data_list)
#         pass

#     def resizeEvent(self, event):
#         """
#         Called on automatically generated resize event
#         """
#         self.widget.resize(self.width(), self.height())
        
#     def closeWindow(self):
#         """
#         Close window.
#         """
#         print ('closing window')
#         self.destroy()
    
# def openWindow():
#     """
#     ID Maya and attach tool window.
#     """
#     # Maya uses this so it should always return True
#     if QtWidgets.QApplication.instance():
#         # Id any current instances of tool and destroy
#         for win in (QtWidgets.QApplication.allWindows()):
#             if 'myToolWindowName' in win.objectName(): # update this name to match name below
#                 win.destroy()

#     #QtWidgets.QApplication(sys.argv)
#     mayaMainWindowPtr = omui.MQtUtil.mainWindow()
#     mayaMainWindow = wrapInstance(int(mayaMainWindowPtr), QtWidgets.QWidget)
#     FK_IK_Switch.window = FK_IK_Switch(parent = mayaMainWindow)
#     FK_IK_Switch.window.setObjectName('myToolWindowName') # code above uses this to ID any existing windows
#     FK_IK_Switch.window.setWindowTitle('Justin\'s FK <-> IK Switch Tool')
#     FK_IK_Switch.window.show()
    
# openWindow()