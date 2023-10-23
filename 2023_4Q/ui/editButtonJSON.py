#-*- coding:utf-8 -*-

import pymel.core as pm
import maya.cmds as cmds
import maya.cmds as mc
import math
import os,sys
import json

import importlib
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QDialog, QVBoxLayout, QLineEdit,QListWidget,QListWidgetItem
from PySide2 import QtCore,QtGui,QtWidgets,__version__
from maya.app.general import mayaMixin
from collections import OrderedDict

class IconDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("select icon")  
        self.setGeometry(200, 200, 300, 100)
        layout = QVBoxLayout( self )
        self.text_input = QLineEdit(self)
        self.icon_list_widget = QListWidget( self )
        self.icon_list_widget.itemClicked.connect( self.accept )
        self.loadIcons()
        layout.addWidget(self.icon_list_widget)  
        layout.addWidget(self.text_input)  
    def loadIcons(self):
        folder_path = "Z:/Private_Folder/kyuseokKim/test_Git/ui/icon/"
        # 지정한 폴더 내의 모든 파일 및 폴더 목록을 가져옵니다.
        folder_contents = os.listdir(folder_path)
        
        png_files = [file for file in folder_contents if file.lower().endswith(".png")]

        for icon_path in png_files:
            icon_item = QListWidgetItem(QtGui.QIcon(folder_path+icon_path), icon_path)
            self.icon_list_widget.addItem(icon_item)
    def get_text(self):
        #selected_icon_name = item.text()
        selected_icon_name = self.icon_list_widget.currentItem() 
        if selected_icon_name is not None:  # 아이템이 선택되었는지 확인
            #print("선택한 아이콘 이름:", selected_icon_name.text())  
            #self.text_input.text( selected_icon_name)
            return 'ui/icon/'+selected_icon_name.text() 
"""                                 
class TextDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()
    def initUI(self):
        self.setWindowTitle("Text Input")
        self.setGeometry(200, 200, 300, 100)
        layout = QVBoxLayout(self)
        self.text_input = QLineEdit(self)
        layout.addWidget(self.text_input)
        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

    def get_text(self):
        return self.text_input.text()
"""   
class TextDialog(QDialog):
    def __init__(self, parent=None, title="Text Input Dialog", default_text=""):
        super().__init__(parent)
        self.initUI(title, default_text)

    def initUI(self, title, default_text):
        self.setWindowTitle(title)
        self.setGeometry(200, 200, 300, 100)
        layout = QVBoxLayout(self)
        
        self.text_input = QLineEdit(self)
        self.text_input.setText(default_text)  # 라인 에디터에 기본 텍스트 설정
        layout.addWidget(self.text_input)
        
        ok_button = QPushButton("OK", self)
        ok_button.clicked.connect(self.accept)
        layout.addWidget(ok_button)

    def get_text(self):
        return self.text_input.text()   
titleA='ui_BUTTON_JSON_00'
class sequence_run_script_UI(mayaMixin.MayaQWidgetBaseMixin,QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(sequence_run_script_UI, self).__init__(parent)
        if pm.window(u'ui_BUTTON_JSON_00', q=True, ex=True):
            pm.deleteUI(u'ui_BUTTON_JSON_00', window=True)
        self.setObjectName('ui_BUTTON_JSON_00')
        self.setWindowTitle(titleA)
        self.setGeometry(500, 200, 750, 350)
        #self.Log()
        self.UI()
    def UI(self):
        layoutA = QtWidgets.QVBoxLayout()
        layoutAH = QtWidgets.QHBoxLayout()        
        #self.textEdit = QtWidgets.QTextEdit()
        self.lEbasePath = QtWidgets.QLineEdit('Z:/Private_Folder/kyuseokKim/test_Git/')
        self.lineEdit = QtWidgets.QLineEdit('Z:/Private_Folder/kyuseokKim/test_Git/ui/button.json')
        self.pBloadJson = QtWidgets.QPushButton('load JSON File')
        self.pBloadJson.clicked.connect(self.loadJsonFile)
        self.pushButton = QtWidgets.QPushButton('저장')
        self.pushButton.clicked.connect(self.saveJsonFile) 
        self.TreeWidget = QtWidgets.QTreeWidget()
        self.TreeWidget.setSelectionMode( QtWidgets.QAbstractItemView.ExtendedSelection )
        #self.addItemTreeWidget(self.TreeWidget)

                           
        #layout = QtWidgets.QVBoxLayout()
        #layoutA.addWidget(self.lineEdit)
        layoutA.addLayout(layoutAH)
        #
        layoutAH.addWidget(self.lEbasePath)        
        layoutAH.addWidget(self.lineEdit)
        layoutAH.addWidget(self.pBloadJson)
        #
        layoutA.addWidget(self.TreeWidget)        
        layoutA.addWidget(self.pushButton)

        self.setLayout(layoutA)
        

    def expandAllItems(self, treeWidget):
        for i in range(treeWidget.topLevelItemCount()):
            item = treeWidget.topLevelItem(i)
            self.expandItemAndChildren(item)

    def expandItemAndChildren(self, item):
        item.setExpanded(True)
        for i in range(item.childCount()):
            child = item.child(i)
            self.expandItemAndChildren(child)
    def addItemTreeWidget(self, TreeWidget):  
        
        header = TreeWidget.header() 
        #header.setSectionResizeMode(0, QtWidgets.QHeaderView.Fixed)  # 첫 번째 열 간격 고정
        #header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)  # 두 번째 열 간격 자동 조정
        #header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)  # 세 번째 열 간격 고정
        #header.setSectionResizeMode(3, QtWidgets.QHeaderView.Fixed)  # 세 번째 열 간격 고정
        header.resizeSection(0, 250) 
        header.resizeSection(1, 30) 
        header.resizeSection(2, 260) 
        TreeWidget.setColumnCount(4)  
        TreeWidget.setHeaderLabels(['이름', '아이콘','아이콘경로','명령어'])
        jsonfilepath=self.lineEdit.text()
        basefilepath=self.lEbasePath.text()
        jsonopenPath=  os.path.normpath( jsonfilepath )
        with open(jsonopenPath, "r") as json_file:
            loaded_data = json.load(json_file)
        buttonDic=loaded_data["buttonDic"]
        buttonImageDic=loaded_data["buttonImageDic"]
        buttonCommandDic=loaded_data["buttonCommandDic"]             
        
        for i in buttonDic:
            rootItemA = QtWidgets.QTreeWidgetItem(self.TreeWidget)
            rootItemA.setText(0, i)
            if i in buttonImageDic:
                icon = QtGui.QIcon(basefilepath+buttonImageDic[i][0])  # 아이콘 이미지 파일 경로 설정
                rootItemA.setIcon(1, icon)
                rootItemA.setText(2, buttonImageDic[i][0])
            if i in buttonDic :
                for j in buttonDic[i]:
                    if j !='':
                        childItem1A = QtWidgets.QTreeWidgetItem(rootItemA)
                        childItem1A.setText(0, j) 
                        if j in buttonImageDic: 
                            icon = QtGui.QIcon(basefilepath+buttonImageDic[j][0])  # 아이콘 이미지 파일 경로 설정
                            childItem1A.setIcon(1, icon) 
                            childItem1A.setText(2, buttonImageDic[j][0]) 
                        if j in buttonCommandDic: 
                            childItem1A.setText(3, buttonCommandDic[j][0])                                                         
        # 컨텍스트 메뉴 생성
        self.contextMenu = QtWidgets.QMenu(self)
        addRootItem = self.contextMenu.addAction("add Root Item")
        addChildItem = self.contextMenu.addAction("add Child Item")
        changeCommand = self.contextMenu.addAction("change Command")
        changeIcon = self.contextMenu.addAction("change Icon")
        selectItemDown = self.contextMenu.addAction("select Item Down")
        testETC = self.contextMenu.addAction("testETC")
        # 컨텍스트 메뉴 연결
        addRootItem.triggered.connect(self.addRootItem)
        addChildItem.triggered.connect(self.addChildItem)
        changeCommand.triggered.connect(self.changeCommand)
        changeIcon.triggered.connect(self.changeIcon)    
        testETC.triggered.connect(self.testETC)     
        selectItemDown.triggered.connect(self.selectItemDown)     
        # 컨텍스트 메뉴 요청 시그널 연결
        self.TreeWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.TreeWidget.customContextMenuRequested.connect(self.showContextMenu)
        
    def showContextMenu(self, position):
        globalPos = self.TreeWidget.viewport().mapToGlobal(position)
        self.contextMenu.exec_(globalPos)

    def addRootItem(self):
        dialog = TextDialog(self)
        if dialog.exec_():
            textA = dialog.get_text()
            print("Entered text:", textA)
        # 추가 작업을 수행하는 코드 작성
        rootItemA = QtWidgets.QTreeWidgetItem(self.TreeWidget)
        rootItemA.setText(0, textA)        
        #print("Add Item")
    def addChildItem(self):
        selected_item = self.TreeWidget.currentItem() 
        if selected_item is not None:  # 아이템이 선택되었는지 확인
            dialog = TextDialog(self)
            if dialog.exec_():
                textA = dialog.get_text()
                print("Entered text:", textA)        
                child_item = QtWidgets.QTreeWidgetItem(selected_item)  # 선택된 아이템의 자식 아이템 생성
                child_item.setText(0, textA)  # 자식 아이템의 텍스트 설정
    def changeCommand(self):
        selected_item = self.TreeWidget.currentItem() 
        parent_item =selected_item.parent()
        default_textA= parent_item.text(0)+'/'+selected_item.text(0)
        if selected_item is not None:  # 아이템이 선택되었는지 확인
            #dialog = TextDialog(self)
            dialog = TextDialog(title="change Command", default_text=default_textA)
            if dialog.exec_():
                textA = dialog.get_text()
                print("Entered text:", textA)    
                selected_item.setText(3, textA)
    def changeIcon(self):
        basefilepath=self.lEbasePath.text()
        selected_item = self.TreeWidget.currentItem()        
        if selected_item is not None:  # 아이템이 선택되었는지 확인
            dialog = IconDialog(self) 
            if dialog.exec_():
                textA = dialog.get_text()              
                print("Entered text aa:", textA)                
                icon = QtGui.QIcon(basefilepath+textA)  # 아이콘 이미지 파일 경로 설정
                selected_item.setIcon(1, icon)     
                selected_item.setText(2, textA)
    def selectItemDown(self):
        selected_item = self.TreeWidget.currentItem()   
        index1 = self.TreeWidget.indexOfTopLevelItem(selected_item) 
        countNum=self.TreeWidget.topLevelItemCount()
        if  index1 < countNum :
            root_item1 = self.TreeWidget.topLevelItem(index1)
            root_item2 = self.TreeWidget.topLevelItem(index1+1)
            if root_item1 and root_item2:
                self.TreeWidget.takeTopLevelItem(index1+1)
                self.TreeWidget.takeTopLevelItem(index1)
                self.TreeWidget.insertTopLevelItem(index1, root_item2)
                self.TreeWidget.insertTopLevelItem(index1+1, root_item1)
        print(index1)
        # 모든 아이템 확장
        self.expandAllItems(self.TreeWidget)          
    def testETC(self):
        self.TreeWidget.setSelectionMode( QtWidgets.QAbstractItemView.SingleSelection )  
        #self.TreeWidget.clear()           
    def loadJsonFile(self):
        self.TreeWidget.clear()
        self.addItemTreeWidget(self.TreeWidget)   
        # 모든 아이템 확장
        self.expandAllItems(self.TreeWidget)  
    def saveJsonFile(self):
        countNum=self.TreeWidget.topLevelItemCount()
        buttonDic={}
        buttonImageDic={}
        buttonCommandDic={}
        #-------------------------------buttonDic-------------------
        for i in range(0,countNum):
            root_item = self.TreeWidget.topLevelItem(i)
            #print ( root_item.text(0) )
            stringA=()
            for j in range(0,root_item.childCount()):
                child_item=root_item.child(j)
                #print ( child_item.text(0) )
                stringA = stringA + ( child_item.text(0), )
                #stringA.append( child_item.text(0) )
            stringA = stringA + ( '', )    
            buttonDic[ root_item.text(0) ] =  stringA     
        #-------------------------------buttonDic-------------------
        #-------------------------------buttonImageDic-------------------  
        for i in range(0,countNum):
            root_item = self.TreeWidget.topLevelItem(i)
            #print ( root_item.text(0) )
            buttonImageDic[root_item.text(0)]=(root_item.text(2),'')

            for j in range(0,root_item.childCount()):
                child_item=root_item.child(j)
                #print ( child_item.text(0) )
                buttonImageDic[child_item.text(0)]=(child_item.text(2),'')
                #stringA.append( child_item.text(0) )

        #-------------------------------buttonImageDic-------------------  
        #-------------------------------buttonCommandDic------------------- 
        for i in range(0,countNum):
            root_item = self.TreeWidget.topLevelItem(i)
            for j in range(0,root_item.childCount()):
                child_item=root_item.child(j)
                buttonCommandDic[child_item.text(0)]=(child_item.text(3),'')
        #-------------------------------buttonCommandDic------------------- 
        combined_data = {
            "buttonDic": buttonDic,
            "buttonImageDic": buttonImageDic,
            "buttonCommandDic": buttonCommandDic
        }                
        print (buttonDic,buttonImageDic,buttonCommandDic) 
        file_path = pm.fileDialog2(fileFilter="JSON (*.json);;All Files (*.*)", dialogStyle=2, fileMode=0)
        if file_path:
            json_data = json.dumps(combined_data, indent=4)
            #with open("d:/data.json", "w") as json_file:
            with open(file_path[0], "w") as json_file:    
                #json.dump(json_data, json_file)
                json_file.write(json_data)       
            print (file_path[0])                   
sequence_run_script_UI().show()
