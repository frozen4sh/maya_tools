#-*- coding:utf-8 -*-
from maya import cmds
import pymel.core as pm
import maya.api.OpenMaya as om
"""
This example demonstrates Maya UI Window for simple and non-programmatic creation the scene with the creating functional rig.
- usage in command line:
    - call without arguments:
        - will not start with error message: "DNAViewer needs to be run with Maya2022"
    NOTE: Script cannot be called with Python or mayapy, it' must be called in Maya Script Editor.
- usage in Maya:
    1. copy whole content of this file to Maya Script Editor
    2. change value of ROOT_DIR to absolute path of dna_calibration, e.g. `c:/dna_calibration` in Windows or `/home/user/dna_calibration`. Important:
    Use `/` (forward slash), because Maya uses forward slashes in path.

    Expected: Maya will show UI.

NOTE: If running on Linux, please make sure to append the LD_LIBRARY_PATH with absolute path to the lib/linux directory before running the example:
    export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:<path-to-lib-linux-dir>
"""
import json
from json import loads

from os import environ
from os import path as ospath
from sys import path as syspath
from sys import platform

# if you use Maya, use absolute path
#ROOT_DIR = f"{ospath.dirname(ospath.abspath(__file__))}".replace("\\", "/")
ROOT_DIR = f"C:/dna_calibration"
ROOT_LIB_DIR = f"{ROOT_DIR}/lib"

if platform == "win32":
    LIB_DIR = f"{ROOT_LIB_DIR}/windows"
elif platform == "linux":
    LIB_DIR = f"{ROOT_LIB_DIR}/linux"
else:
    raise OSError(
        "OS not supported, please compile dependencies and add value to LIB_DIR"
    )

# Add bin directory to maya plugin path
if "MAYA_PLUG_IN_PATH" in environ:
    separator = ":" if platform == "linux" else ";"
    environ["MAYA_PLUG_IN_PATH"] = separator.join([environ["MAYA_PLUG_IN_PATH"], LIB_DIR])
else:
    environ["MAYA_PLUG_IN_PATH"] = LIB_DIR

# Adds directories to path
syspath.insert(0, ROOT_DIR)
syspath.insert(0, LIB_DIR)

import dna
import sys
from maya import OpenMayaUI as omui 
from PySide2.QtCore import * 
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from PySide2 import __version__
from shiboken2 import wrapInstance 
from maya.app.general import mayaMixin
#mayaMainWindowPtr = omui.MQtUtil.mainWindow() 
#mayaMainWindow= wrapInstance( int(mayaMainWindowPtr), QWidget)

def blendshapeweight1(nodeA,listB):
    pm.select(nodeA,listB[0])
    BlendShapeA=pm.mel.eval('blendShape;')
    pm.PyNode(BlendShapeA[0]).weight[0].set(1)
def skincopyUV(nodeA,nodeB):
    nodeA.v.set(0)
    skinclusterList=nodeA.listHistory(type='skinCluster')
    skinjonitList=pm.skinCluster(skinclusterList[0], query=True, influence=True)
    pm.select(skinjonitList,nodeB)
    pm.mel.eval('SmoothBindSkin;')
    skinclusterListB=nodeB.listHistory(type='skinCluster')
    pm.select(nodeA,nodeB)
    pm.mel.eval('copySkinWeights  -noMirror -surfaceAssociation closestPoint -uvSpace map1 map1 -influenceAssociation oneToOne -influenceAssociation label -influenceAssociation oneToOne;')
def blendshapeweight1(nodeA,listB):
    pm.select(nodeA,listB[0])
    BlendShapeA=pm.mel.eval('blendShape;')
    pm.PyNode(BlendShapeA[0]).weight[0].set(1)
# 노드 2개를 주면  스킨 조인트를 찾아서  스킨을 걸어주고 uv 모드로 카피해준다. 
def skincopyUV(nodeA,nodeB):
    nodeA.v.set(0)
    skinclusterList=nodeA.listHistory(type='skinCluster')
    skinjonitList=pm.skinCluster(skinclusterList[0], query=True, influence=True)
    pm.select(skinjonitList,nodeB)
    pm.mel.eval('SmoothBindSkin;')
    skinclusterListB=nodeB.listHistory(type='skinCluster')
    pm.select(nodeA,nodeB)
    pm.mel.eval('copySkinWeights  -noMirror -surfaceAssociation closestPoint -uvSpace map1 map1 -influenceAssociation oneToOne -influenceAssociation label -influenceAssociation oneToOne;')
    
titleA=u'UE_MH_DNA_NeutralJoint_Custom_UI_V20230227'
class UE_MH_RDNA_UI(mayaMixin.MayaQWidgetBaseMixin,QWidget):
    def __init__(self, parent=None):
        
        getPath_dna=pm.ls(type='embeddedNodeRL4')
        binaryFilePath=''
        if (getPath_dna):
            binaryFilePath=getPath_dna[0].dnaFilePath.get()
        readStream = dna.FileStream(binaryFilePath, dna.FileStream.AccessMode_Read , dna.FileStream.OpenMode_Binary)
        self.reader = dna.BinaryStreamReader(readStream)
        self.reader.read()         
        
        super(UE_MH_RDNA_UI, self).__init__(parent)
        self.setObjectName('UE_MH_DNA_Custom_UI_V20230227')
        self.setWindowTitle(titleA)
        self.setGeometry(500, 100, 940, 500)
        self.allQVBoxLayout = QVBoxLayout()
        self.table_cMHdnaLoad_btn=QPushButton("Current_MH_DNA_load")
        self.table_cMHdnaLoad_btn.clicked.connect(self.table_cMHdnaLoad_run)
        self.table_cRjntLoad_btn=QPushButton("Custom_retagetJoint_load")
        self.table_cRjntLoad_btn.clicked.connect(self.table_cRjntLoad_run)
        self.table_import_json_btn=QPushButton("json_import")
        self.table_import_json_btn.clicked.connect(self.table_import_json_run)
        self.table_import_dna_btn=QPushButton("DNA_import")
        self.table_import_dna_btn.clicked.connect(self.table_import_dna_run)
        self.textedit_dnaPath = QLineEdit()
        self.textedit_dnaPath.setContextMenuPolicy(Qt.ActionsContextMenu)   
           
        action1 = QAction("dna file -> current MH " , self.textedit_dnaPath)
        action2 = QAction("retaget group -> rename " , self.textedit_dnaPath)
        action3 = QAction("retaget skin change - final " , self.textedit_dnaPath)
        
        action1.triggered.connect(self.textedit_dnaPath_action1_run)
        action2.triggered.connect(self.textedit_dnaPath_action2_run)
        action3.triggered.connect(self.textedit_dnaPath_action3_run)                
        
        self.textedit_dnaPath.addAction(action1)
        self.textedit_dnaPath.addAction(action2)
        self.textedit_dnaPath.addAction(action3)
        
        self.table = QTableWidget( )
        self.table.setColumnCount( 7 )

        self.table.setColumnWidth(0,170)
        self.table.setColumnWidth(1,120)
        self.table.setColumnWidth(2,120)
        self.table.setColumnWidth(3,120)
        self.table.setColumnWidth(4,120)
        self.table.setColumnWidth(5,120)
        self.table.setHorizontalHeaderLabels(["Name" ,"Tx" , "Ty", "Tz", "Rx", "Ry", "Rz" ])
        self.dna_export_json_btn=QPushButton("DNA_export_json")
        self.dna_export_json_btn.clicked.connect(self.dna_export_json_run)
        self.table_export_json_btn=QPushButton("TableWidget_export_json")        
        self.table_export_json_btn.clicked.connect(self.table_export_json_run)
        self.table_save_json_btn=QPushButton("TableWidget_TO_DNA_save")        
        self.table_save_json_btn.clicked.connect(self.table_save_json_run)
        self.allQVBoxLayout.addWidget(self.table_cMHdnaLoad_btn)
        self.allQVBoxLayout.addWidget(self.table_cRjntLoad_btn)
        self.allQVBoxLayout.addWidget(self.table_import_json_btn)
        self.allQVBoxLayout.addWidget(self.table_import_dna_btn)        
        self.allQVBoxLayout.addWidget(self.textedit_dnaPath)
        
        self.allQVBoxLayout.addWidget(self.table)
        
        self.allQVBoxLayout.addWidget(self.dna_export_json_btn)
        self.allQVBoxLayout.addWidget(self.table_export_json_btn)

        self.allQVBoxLayout.addWidget(self.table_save_json_btn)
        self.setLayout(self.allQVBoxLayout)
    def table_setRowCount(self):
        count = self.reader.getJointCount()
        self.table.setRowCount( count )
    def table_setItem_name(self):
        count = self.reader.getJointCount()
        for i in range(count):
            textA = self.reader.getJointName(i)
            itemA = QTableWidgetItem(textA)
            self.table.setItem(i,0,itemA)
    def table_setTranslate(self):
        count = self.reader.getJointCount()
        for i in range(count):
            vectorA = self.reader.getNeutralJointTranslation(i)
            itemA = QTableWidgetItem('%0.3f'%(vectorA[0]))
            itemB = QTableWidgetItem('%0.3f'%(vectorA[1]))
            itemC = QTableWidgetItem('%0.3f'%(vectorA[2]))
            self.table.setItem(i,1,itemA)
            self.table.setItem(i,2,itemB)
            self.table.setItem(i,3,itemC)
    def table_setRotate(self):
        count = self.reader.getJointCount()
        for i in range(count):
            vectorA = self.reader.getNeutralJointRotation(i)
            itemA = QTableWidgetItem('%0.3f'%(vectorA[0]))
            itemB = QTableWidgetItem('%0.3f'%(vectorA[1]))
            itemC = QTableWidgetItem('%0.3f'%(vectorA[2]))
            self.table.setItem(i,4,itemA)
            self.table.setItem(i,5,itemB)
            self.table.setItem(i,6,itemC)
    def table_cMHdnaLoad_run(self):
        self.table.clear()
        self.table.setHorizontalHeaderLabels(["Name" ,"Tx" , "Ty", "Tz", "Rx", "Ry", "Rz" ])
        getPath_dna=pm.ls(type='embeddedNodeRL4')
        binaryFilePath=getPath_dna[0].dnaFilePath.get()
        readStream = dna.FileStream(binaryFilePath, dna.FileStream.AccessMode_Read , dna.FileStream.OpenMode_Binary)
        self.reader = dna.BinaryStreamReader(readStream)
        self.reader.read()        
        self.textedit_dnaPath.setText(binaryFilePath)
        self.table_setRowCount( )
        self.table_setItem_name( )
        self.table_setTranslate( )
        self.table_setRotate( )
        #print ('a')
    def table_cRjntLoad_run(self):
        if pm.objExists('retarget'):
            retaget_space = pm.PyNode('retarget')
            head_retarget = pm.PyNode('head_retarget')
            teeth_retarget = pm.PyNode('teeth_retarget')
            saliva_retarget = pm.PyNode('saliva_retarget')
            eyeLeft_retarget = pm.PyNode('eyeLeft_retarget')
            eyeRight_retarget = pm.PyNode('eyeRight_retarget')
            eyeshell_retarget = pm.PyNode('eyeshell_retarget')
            eyelashes_retarget = pm.PyNode('eyelashes_retarget')
            eyeEdge_retarget = pm.PyNode('eyeEdge_retarget')
            cartilage_retarget = pm.PyNode('cartilage_retarget')
            org_space = pm.PyNode('head_lod0_grp')
            head_org = pm.PyNode('head_lod0_mesh')
            teeth_org = pm.PyNode('teeth_lod0_mesh')
            saliva_org = pm.PyNode('saliva_lod0_mesh')
            eyeLeft_org = pm.PyNode('eyeLeft_lod0_mesh')
            eyeRight_org = pm.PyNode('eyeRight_lod0_mesh')
            eyeshell_org = pm.PyNode('eyeshell_lod0_mesh')
            eyelashes_org = pm.PyNode('eyelashes_lod0_mesh')
            eyeEdge_org = pm.PyNode('eyeEdge_lod0_mesh')
            cartilage_org = pm.PyNode('cartilage_lod0_mesh')
            #==============================================
            pm.select( clear=True )
            pm.duplicate('DHIhead:spine_04')
            pm.select( clear=True )
            locator_retaget_list=[]
            pm.select('spine_05',hi=1)
            for i in pm.ls(sl=1,type='joint'):
                locatorShape=pm.createNode('locator',n='retaget_'+i+'Shape')
                locator_=locatorShape.getParent()
                locator_retaget_list.append(locator_)
                da=pm.pointConstraint(i,locator_,mo=0)
                pm.delete(da)
            pm.select(cl=1)
            head_ProximityPin = pm.duplicate(head_org,rr=1)
            teeth_ProximityPin = pm.duplicate(teeth_org,rr=1)
            eyeLeft_ProximityPin = pm.duplicate(eyeLeft_org,rr=1)
            eyeRight_ProximityPin = pm.duplicate(eyeRight_org,rr=1)
            joint_eye_L_retaget_list=['retaget_FACIAL_L_EyelidLowerA','retaget_FACIAL_L_EyelidLowerB','retaget_FACIAL_L_EyelidUpperB',
                                    'retaget_FACIAL_L_EyelidUpperA','retaget_FACIAL_L_Eye','retaget_FACIAL_L_EyeParallel']
            joint_eye_R_retaget_list=['retaget_FACIAL_R_EyelidLowerA','retaget_FACIAL_R_EyelidLowerB','retaget_FACIAL_R_EyelidUpperB',
                                    'retaget_FACIAL_R_EyelidUpperA','retaget_FACIAL_R_Eye','retaget_FACIAL_R_EyeParallel']
            joint_tongue_retaget_list=['retaget_FACIAL_C_TeethLower','retaget_FACIAL_C_Tongue1','retaget_FACIAL_C_Tongue2','retaget_FACIAL_C_Tongue3',
                                'retaget_FACIAL_C_TongueUpper3','retaget_FACIAL_R_TongueSide3','retaget_FACIAL_C_TongueLower3',
                                'retaget_FACIAL_L_TongueSide3','retaget_FACIAL_C_Tongue4','retaget_FACIAL_R_TongueSide2',
                                'retaget_FACIAL_C_TongueUpper2','retaget_FACIAL_L_TongueSide2','retaget_FACIAL_C_TeethUpper']
            deleteConstraintList=[]
            deleteProximityPin=[]
            for i in locator_retaget_list:
                if i.nodeName() in joint_eye_L_retaget_list:
                    pm.select(eyeLeft_ProximityPin)
                    pm.select(i,add=1)
                    deleteProximityPin.append(pm.mel.eval('ProximityPin;'))
                elif  i.nodeName() in joint_eye_R_retaget_list:  
                    pm.select(eyeRight_ProximityPin)
                    pm.select(i,add=1)
                    deleteProximityPin.append(pm.mel.eval('ProximityPin;'))
                elif  i.nodeName() in joint_tongue_retaget_list:  
                    pm.select(teeth_ProximityPin)
                    pm.select(i,add=1)
                    deleteProximityPin.append(pm.mel.eval('ProximityPin;'))
                else:
                    pm.select(head_ProximityPin)
                    pm.select(i,add=1)
                    deleteProximityPin.append(pm.mel.eval('ProximityPin;'))
            for i in locator_retaget_list:
                da=pm.pointConstraint(i,i.replace('retaget_',''),mo=0)
                deleteConstraintList.append(da)
            #blendshape
            pm.select(head_retarget,head_ProximityPin[0])
            headBlendShape=pm.mel.eval('blendShape;')
            pm.PyNode(headBlendShape[0]).weight[0].set(1)
            pm.select(teeth_retarget,teeth_ProximityPin[0])
            teethBlendShape=pm.mel.eval('blendShape;')
            pm.PyNode(teethBlendShape[0]).weight[0].set(1)
            pm.select(eyeLeft_retarget,eyeLeft_ProximityPin[0])
            eyeLeftBlendShape=pm.mel.eval('blendShape;')
            pm.PyNode(eyeLeftBlendShape[0]).weight[0].set(1)
            pm.select(eyeRight_retarget,eyeRight_ProximityPin[0])
            eyeRightBlendShape=pm.mel.eval('blendShape;')
            pm.PyNode(eyeRightBlendShape[0]).weight[0].set(1)
            listA='FACIAL_C_Neck1Root','neck_01','neck_02','FACIAL_C_Neck2Root','head','FACIAL_C_FacialRoot','spine_05','clavicle_r','upperarm_r','upperarm_correctiveRoot_r','upperarm_bck_r','upperarm_fwd_r','upperarm_out_r','upperarm_in_r','clavicle_out_r','clavicle_scap_r','clavicle_l','upperarm_l','upperarm_correctiveRoot_l','upperarm_bck_l','upperarm_fwd_l','upperarm_out_l','upperarm_in_l','clavicle_out_l','clavicle_scap_l','clavicle_pec_l','clavicle_pec_r','spine_04_latissimus_r','spine_04_latissimus_l'
            for i in listA:
                posT = pm.PyNode('DHIhead:'+i).getTranslation(space='world')
                pm.PyNode('retaget_'+i).setTranslation(posT,space='world')                
            lockMoveList="retaget_neck_01","retaget_neck_02","retaget_head","retaget_FACIAL_C_Neck1Root","retaget_FACIAL_C_Neck2Root","retaget_FACIAL_C_FacialRoot"
            set00List=[]
            for i in lockMoveList:
                inputProximityPin=pm.listConnections(i+'.offsetParentMatrix')
                set00List.append(inputProximityPin[0])
            for i in set00List:    
                pm.PyNode( i+'.envelope' ).set(0)
            for i in lockMoveList:
                da=pm.pointConstraint(i.replace('retaget_','DHIhead:'),i,mo=0)
                deleteConstraintList.append(da)  
        if pm.objExists('spine_05'):
            count = self.reader.getJointCount()
            for i in range(1,count):
                nameA = self.reader.getJointName(i)
                vectorA = pm.PyNode(nameA).t.get()
                itemA = QTableWidgetItem('%0.3f'%(vectorA[0]))
                itemB = QTableWidgetItem('%0.3f'%(vectorA[1]))
                itemC = QTableWidgetItem('%0.3f'%(vectorA[2]))
                self.table.setItem(i,1,itemA)
                self.table.setItem(i,2,itemB)
                self.table.setItem(i,3,itemC)
            pm.delete(deleteConstraintList)
            pm.delete(head_ProximityPin,teeth_ProximityPin,eyeLeft_ProximityPin,eyeRight_ProximityPin)
            pm.delete(locator_retaget_list)
            pm.delete( pm.ls('pinInput*' ,type='transform'))
    def table_import_dna_run(self):
        self.table.clear()
        self.table.setHorizontalHeaderLabels(["Name" ,"Tx" , "Ty", "Tz", "Rx", "Ry", "Rz" ])
        files, _ = QFileDialog.getOpenFileNames(self,"getdna", "","All Files (*);;DNA Files (*.dna)", options=QFileDialog.DontUseNativeDialog)
        if files:
            binaryFilePathA=files[0]
            readStream = dna.FileStream(binaryFilePathA, dna.FileStream.AccessMode_Read , dna.FileStream.OpenMode_Binary)
            self.reader = dna.BinaryStreamReader(readStream)
            self.reader.read()        
            self.textedit_dnaPath.setText(binaryFilePathA)
            self.table_setRowCount( )
            self.table_setItem_name( )
            self.table_setTranslate( )
            self.table_setRotate( )
    def dna_export_json_run(self):
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",".json","Json Files (*.json)", options=QFileDialog.DontUseNativeDialog)
        if fileName:
            getPath_dna=pm.ls(type='embeddedNodeRL4')
            binaryFilePath=getPath_dna[0].dnaFilePath.get()
            readStream = dna.FileStream(binaryFilePath, dna.FileStream.AccessMode_Read , dna.FileStream.OpenMode_Binary)
            self.reader = dna.BinaryStreamReader(readStream)
            self.reader.read()   
            jsonString='{"size":"%d"}'%self.reader.getJointCount()
            d = json.loads( jsonString )
            jointName={}
            NeutralTranslate={}
            NeutralRoattion={}
            count = self.reader.getJointCount()
            for i in range(count):
                jointName["%d"%i]        = self.reader.getJointName(i)
                NeutralTranslate["%d"%i] = self.reader.getNeutralJointTranslation(i)
                NeutralRoattion["%d"%i]  = self.reader.getNeutralJointRotation(i)
            d["jointName"]=jointName
            d["NeutralTranslate"]=NeutralTranslate
            d["NeutralRoattion"]=NeutralRoattion   
            with open(fileName, "w") as json_file:            
                json.dump(d, json_file)
    def table_export_json_run(self):
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()",".json","Json Files (*.json)", options=QFileDialog.DontUseNativeDialog)
        if fileName:        
            count=self.table.rowCount()    
            jsonString='{"size":"%d"}'%count
            d = json.loads( jsonString )  
            jointName={}
            NeutralTranslate={}
            NeutralRoattion={}
            for i in range(count):
                jointName["%d"%i]        = self.table.item(i, 0).text()            
                NeutralTranslate["%d"%i] = [ float(self.table.item(i, 1).text()) , float(self.table.item(i, 2).text()) , float(self.table.item(i, 3).text()) ]
                NeutralRoattion["%d"%i]  = [ float(self.table.item(i, 4).text()) , float(self.table.item(i, 5).text()) , float(self.table.item(i, 6).text()) ]
            d["jointName"]=jointName
            d["NeutralTranslate"]=NeutralTranslate
            d["NeutralRoattion"]=NeutralRoattion
            with open(fileName, "w") as json_file:            
                json.dump(d, json_file)
    def table_import_json_run(self):
        self.table.clear()
        self.table.setHorizontalHeaderLabels(["Name" ,"Tx" , "Ty", "Tz", "Rx", "Ry", "Rz" ])
        files, _ = QFileDialog.getOpenFileNames(self,"getdna", "","Json Files (*.json)", options=QFileDialog.DontUseNativeDialog)
        if files:  
            with open(files[0], "r") as json_file:
                json_data = json.load(json_file) 
            self.table.setRowCount( int(json_data['size']) )                             
            for i in range( int(json_data['size'])  ):
                itemZ = QTableWidgetItem( json_data['jointName']['%d'%i] ) 
                self.table.setItem(i,0,itemZ)
                itemA = QTableWidgetItem(str(json_data['NeutralTranslate']['%d'%i][0]))
                itemB = QTableWidgetItem(str(json_data['NeutralTranslate']['%d'%i][1]))
                itemC = QTableWidgetItem(str(json_data['NeutralTranslate']['%d'%i][2]))
                itemD = QTableWidgetItem(str(json_data['NeutralRoattion']['%d'%i][0]))
                itemE = QTableWidgetItem(str(json_data['NeutralRoattion']['%d'%i][1]))
                itemF = QTableWidgetItem(str(json_data['NeutralRoattion']['%d'%i][2]))
                self.table.setItem(i,1,itemA)
                self.table.setItem(i,2,itemB)
                self.table.setItem(i,3,itemC)
                self.table.setItem(i,4,itemD)
                self.table.setItem(i,5,itemE)
                self.table.setItem(i,6,itemF)                
    def table_save_json_run(self):
        pathA = self.textedit_dnaPath.text()
        fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","%s"%pathA.rsplit('/',1)[0],"DNA Files (*.dna)", options=QFileDialog.DontUseNativeDialog)
        if fileName:        
            stream = dna.FileStream(fileName, dna.FileStream.AccessMode_Write, dna.FileStream.OpenMode_Binary)
            self.writer = dna.BinaryStreamWriter(stream)
            readStream = dna.FileStream(pathA, dna.FileStream.AccessMode_Read , dna.FileStream.OpenMode_Binary)
            self.reader = dna.BinaryStreamReader(readStream)
            self.reader.read()   
            self.writer.setFrom(self.reader)
            #for i in dir(writer):
            #    print(i)
            count=self.table.rowCount() 
            setT=[]  
            for i in range(0,count):
                setT.append( [ float(self.table.item(i, 1).text()) , float(self.table.item(i, 2).text()) , float(self.table.item(i, 3).text()) ] )
                #setT.append( [ 0.0, 0.0, 0.0 ] )
            # Creates the DNA
            self.writer.setNeutralJointTranslations(setT)
            self.writer.write()                    
            print (fileName)
    def textedit_dnaPath_action1_run(self):
        getPath_dna=pm.ls(type='embeddedNodeRL4')
        if getPath_dna:
            pathA = self.textedit_dnaPath.text()
            pm.PyNode(getPath_dna[0]+'.dnaFilePath').set(pathA)
    def textedit_dnaPath_action2_run(self):
        errerCheck=False
        selObj=pm.ls(sl=1)
        selChildren=None
        if len( selObj ) == 1:
            selChildren=selObj[0].getChildren()
            if len(selChildren) ==9:
                errerCheck=True
        if errerCheck:
            print ('0k')
            selObj[0].rename('retarget')
            #delete ORG node
            for i in selChildren:
                for j in i.getChildren(s=1):
                    if j.nodeName()[-5:]!='Shape':
                        pm.delete(j)
                    # 24049
                    if j.numVertices() == 24049:
                        i.rename('head_retarget')
                    elif j.numVertices() == 552:                
                        i.rename('eyeshell_retarget')
                    elif j.numVertices() == 268:                
                        i.rename('eyeEdge_retarget')
                    elif j.numVertices() == 2144:                
                        i.rename('eyelashes_retarget')
                    elif j.numVertices() == 660:                
                        i.rename('saliva_retarget')
                    elif j.numVertices() == 4246:                
                        i.rename('teeth_retarget')
                    elif j.numVertices() == 386:                
                        i.rename('cartilage_retarget')
                    elif j.numVertices() == 770:
                        if  pm.pointPosition(j+'.vtx[0]')[0] > 0:
                            i.rename('eyeLeft_retarget')
                        else:    
                            i.rename('eyeRight_retarget')
                    else:
                        pass
        pm.reorder( 'head_retarget', b=1 )
        pm.reorder( 'teeth_retarget', b=1 )
        pm.reorder( 'saliva_retarget', b=1 )
        pm.reorder( 'eyeLeft_retarget', b=1 )
        pm.reorder( 'eyeRight_retarget', b=1 )
        pm.reorder( 'eyeshell_retarget', b=1 )
        pm.reorder( 'eyelashes_retarget', b=1 )
        pm.reorder( 'eyeEdge_retarget', b=1 )
        pm.reorder( 'cartilage_retarget', b=1 )
    def textedit_dnaPath_action3_run(self):
        retaget_space = pm.PyNode('retarget')
        head_retarget = pm.PyNode('head_retarget')
        teeth_retarget = pm.PyNode('teeth_retarget')
        saliva_retarget = pm.PyNode('saliva_retarget')
        eyeLeft_retarget = pm.PyNode('eyeLeft_retarget')
        eyeRight_retarget = pm.PyNode('eyeRight_retarget')
        eyeshell_retarget = pm.PyNode('eyeshell_retarget')
        eyelashes_retarget = pm.PyNode('eyelashes_retarget')
        eyeEdge_retarget = pm.PyNode('eyeEdge_retarget')
        cartilage_retarget = pm.PyNode('cartilage_retarget')
        org_space = pm.PyNode('head_lod0_grp')
        head_org = pm.PyNode('head_lod0_mesh')
        teeth_org = pm.PyNode('teeth_lod0_mesh')
        saliva_org = pm.PyNode('saliva_lod0_mesh')
        eyeLeft_org = pm.PyNode('eyeLeft_lod0_mesh')
        eyeRight_org = pm.PyNode('eyeRight_lod0_mesh')
        eyeshell_org = pm.PyNode('eyeshell_lod0_mesh')
        eyelashes_org = pm.PyNode('eyelashes_lod0_mesh')
        eyeEdge_org = pm.PyNode('eyeEdge_lod0_mesh')
        cartilage_org = pm.PyNode('cartilage_lod0_mesh')
        cmds.select( clear=True )
        head_blendshape = pm.duplicate(head_org,rr=1)
        teeth_blendshape = pm.duplicate(teeth_org,rr=1)
        saliva_blendshape = pm.duplicate(saliva_org,rr=1)
        eyeLeft_blendshape = pm.duplicate(eyeLeft_org,rr=1)
        eyeRight_blendshape = pm.duplicate(eyeRight_org,rr=1)
        eyeshell_blendshape = pm.duplicate(eyeshell_org,rr=1)
        eyelashes_blendshape = pm.duplicate(eyelashes_org,rr=1)
        eyeEdge_blendshape = pm.duplicate(eyeEdge_org,rr=1)
        cartilage_blendshape = pm.duplicate(cartilage_org,rr=1)        
        blendshapeweight1(head_retarget,head_blendshape)
        blendshapeweight1(teeth_retarget,teeth_blendshape)
        blendshapeweight1(saliva_retarget,saliva_blendshape)
        blendshapeweight1(eyeLeft_retarget,eyeLeft_blendshape)
        blendshapeweight1(eyeRight_retarget,eyeRight_blendshape)
        blendshapeweight1(eyeshell_retarget,eyeshell_blendshape)
        blendshapeweight1(eyelashes_retarget,eyelashes_blendshape)
        blendshapeweight1(eyeEdge_retarget,eyeEdge_blendshape)
        blendshapeweight1(cartilage_retarget,cartilage_blendshape)
        head_skinoutput = pm.duplicate(head_blendshape[0],rr=1)
        teeth_skinoutput = pm.duplicate(teeth_blendshape[0],rr=1)
        saliva_skinoutput = pm.duplicate(saliva_blendshape[0],rr=1)
        eyeLeft_skinoutput = pm.duplicate(eyeLeft_blendshape[0],rr=1)
        eyeRight_skinoutput = pm.duplicate(eyeRight_blendshape[0],rr=1)
        eyeshell_skinoutput = pm.duplicate(eyeshell_blendshape[0],rr=1)
        eyelashes_skinoutput = pm.duplicate(eyelashes_blendshape[0],rr=1)
        eyeEdge_skinoutput = pm.duplicate(eyeEdge_blendshape[0],rr=1)
        cartilage_skinoutput = pm.duplicate(cartilage_blendshape[0],rr=1)
        pm.delete(head_blendshape,teeth_blendshape,saliva_blendshape,eyeLeft_blendshape,eyeRight_blendshape,
                    eyeshell_blendshape,eyelashes_blendshape,eyeEdge_blendshape,cartilage_blendshape)
        skincopyUV(head_org,head_skinoutput[0])
        skincopyUV(teeth_org,teeth_skinoutput[0])
        skincopyUV(saliva_org,saliva_skinoutput[0])
        skincopyUV(eyeLeft_org,eyeLeft_skinoutput[0])
        skincopyUV(eyeRight_org,eyeRight_skinoutput[0])
        skincopyUV(eyeshell_org,eyeshell_skinoutput[0])
        skincopyUV(eyelashes_org,eyelashes_skinoutput[0])
        skincopyUV(eyeEdge_org,eyeEdge_skinoutput[0])
        skincopyUV(cartilage_org,cartilage_skinoutput[0])        
        retaget_space.v.set(0)          
        rl4_node_op()
        cmds.select( clear=True )        
        head_blendshape = pm.duplicate(head_org,rr=1)
        teeth_blendshape = pm.duplicate(teeth_org,rr=1)
        saliva_blendshape = pm.duplicate(saliva_org,rr=1)
        eyeLeft_blendshape = pm.duplicate(eyeLeft_org,rr=1)
        eyeRight_blendshape = pm.duplicate(eyeRight_org,rr=1)
        eyeshell_blendshape = pm.duplicate(eyeshell_org,rr=1)
        eyelashes_blendshape = pm.duplicate(eyelashes_org,rr=1)
        eyeEdge_blendshape = pm.duplicate(eyeEdge_org,rr=1)
        cartilage_blendshape = pm.duplicate(cartilage_org,rr=1)
        blendshapeweight1(head_retarget,head_blendshape)
        blendshapeweight1(teeth_retarget,teeth_blendshape)
        blendshapeweight1(saliva_retarget,saliva_blendshape)
        blendshapeweight1(eyeLeft_retarget,eyeLeft_blendshape)
        blendshapeweight1(eyeRight_retarget,eyeRight_blendshape)
        blendshapeweight1(eyeshell_retarget,eyeshell_blendshape)
        blendshapeweight1(eyelashes_retarget,eyelashes_blendshape)
        blendshapeweight1(eyeEdge_retarget,eyeEdge_blendshape)
        blendshapeweight1(cartilage_retarget,cartilage_blendshape)
        head_skinoutput = pm.duplicate(head_blendshape[0],rr=1)
        teeth_skinoutput = pm.duplicate(teeth_blendshape[0],rr=1)
        saliva_skinoutput = pm.duplicate(saliva_blendshape[0],rr=1)
        eyeLeft_skinoutput = pm.duplicate(eyeLeft_blendshape[0],rr=1)
        eyeRight_skinoutput = pm.duplicate(eyeRight_blendshape[0],rr=1)
        eyeshell_skinoutput = pm.duplicate(eyeshell_blendshape[0],rr=1)
        eyelashes_skinoutput = pm.duplicate(eyelashes_blendshape[0],rr=1)
        eyeEdge_skinoutput = pm.duplicate(eyeEdge_blendshape[0],rr=1)
        cartilage_skinoutput = pm.duplicate(cartilage_blendshape[0],rr=1)
        pm.delete(head_blendshape,teeth_blendshape,saliva_blendshape,eyeLeft_blendshape,eyeRight_blendshape,
                    eyeshell_blendshape,eyelashes_blendshape,eyeEdge_blendshape,cartilage_blendshape)
        skincopyUV(head_org,head_skinoutput[0])
        skincopyUV(teeth_org,teeth_skinoutput[0])
        skincopyUV(saliva_org,saliva_skinoutput[0])
        skincopyUV(eyeLeft_org,eyeLeft_skinoutput[0])
        skincopyUV(eyeRight_org,eyeRight_skinoutput[0])
        skincopyUV(eyeshell_org,eyeshell_skinoutput[0])
        skincopyUV(eyelashes_org,eyelashes_skinoutput[0])
        skincopyUV(eyeEdge_org,eyeEdge_skinoutput[0])
        skincopyUV(cartilage_org,cartilage_skinoutput[0])
        retaget_space.v.set(0)
        print('c')
if cmds.window(u"UE_MH_DNA_Custom_UI_V20230227", q=True, ex=True):
    cmds.deleteUI(u"UE_MH_DNA_Custom_UI_V20230227", window=True)
if cmds.window(u"UE_MH_DNA_Custom_UI_V20230227", q=True, ex=True):
    cmds.deleteUI(u"UE_MH_DNA_Custom_UI_V20230227", window=True)
UE_MH_RDNA_UI().show()

