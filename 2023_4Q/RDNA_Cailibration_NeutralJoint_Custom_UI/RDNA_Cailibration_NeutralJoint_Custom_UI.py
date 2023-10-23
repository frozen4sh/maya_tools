#-*- coding:utf-8 -*-
import shutil
import datetime
from maya import cmds
import pymel.core as pm
import maya.api.OpenMaya as om
import os
import subprocess
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
dic_Curve={'FACIAL_D_NeckA1':( 0,0.3,0 ,2.5 ),
    'FACIAL_C_NeckF1':( 0,0.3,0 ,2.5 ),
    'FACIAL_C_NeckB1':( 0,0.3,0 ,2.5 ),
    'FACIAL_L_NeckA1':( 0,0.3,0 ,2.5 ),
    'FACIAL_L_NeckB1':( 0,0.3,0 ,2.5 ),
    'FACIAL_L_NeckC1':( 0,0.3,0 ,2.5 ),
    'FACIAL_L_NeckD1':( 0,0.3,0 ,2.5 ),
    'FACIAL_R_NeckA1':( 0,0.3,0 ,2.5 ),
    'FACIAL_R_NeckB1':( 0,0.3,0 ,2.5 ),
    'FACIAL_R_NeckC1':( 0,0.3,0 ,2.5 ),
    'FACIAL_R_NeckD1':( 0,0.3,0 ,2.5 ),
    'FACIAL_C_UnderChin':( 0.5,0.2,0.2 ,2.5 ),
    'FACIAL_C_UnderChin_A':( 0.5,0.2,0.2 ,2.5 ),
    'FACIAL_C_UnderChin_B':( 0.5,0.2,0.2 ,2.5 ),
    'FACIAL_C_Jawline':( 0.5,0.2,0.2 ,2.5 ),
    'FACIAL_C_Jawline_A':( 0.5,0.2,0.2 ,2.5 ),
    'FACIAL_C_Jawline_B':( 0.5,0.2,0.2 ,2.5 ),
    'FACIAL_C_Jawline_C':( 0.5,0.2,0.2 ,2.5 ),
    'FACIAL_C_Chin1':( 0.3,0.1,0.1 ,2.5 ),
    'FACIAL_LR_12IPV_ChinS1':( 0.3,0.1,0.1 ,2.5 ),
    'FACIAL_LR_12IPV_ChinS2':( 0.3,0.1,0.1 ,2.5 ),
    'FACIAL_R_12IPV_ChinA':( 0.4,0.0,0.1 ,1.5 ),
    'FACIAL_R_12IPV_ChinB':( 0.4,0.0,0.1 ,1.5 ),
    'FACIAL_C_12IPV_ChinA':( 0.4,0.0,0.1 ,1.5 ),
    'FACIAL_L_12IPV_ChinA':( 0.4,0.0,0.1 ,1.5 ),
    'FACIAL_L_12IPV_ChinB':( 0.4,0.0,0.1 ,1.5 ),
    'FACIAL_C_Chin':( 0.3,0.1,0.1 ,2.5 ),
    'FACIAL_R_12IPV_MouthInteriorLower1':( 0.7,0.3,0.3 ,1.5 ),
    'FACIAL_C_LipLowerSkin':( 0.9,0.9,0.0 ,1.5 ),
    'FACIAL_C_12IPV_LipLowerSkin1':( 0.9,0.9,0.0 ,1.5 ),
    'FACIAL_C_12IPV_LipLowerSkin2':( 0.9,0.9,0.0 ,1.5 ),
    'FACIAL_C_LipUpper':( 0.7,0.3,0.2 ,1.5 ),
    'FACIAL_C_LipLower':( 0.7,0.3,0.2 ,1.5 ),
    'FACIAL_R_JawBulge':( 0.9,0.2,0.2 ,1.5 ),
    'FACIAL_R_12IPV_MouthInteriorUpper1':( 0.9,0.2,0.2 ,1.5 ),
    'FACIAL_C_TeethUpper':( 0.9,0.2,0.2 ,1.5 ),
    'FACIAL_C_Tongue1':( 1.0,1.0,1.0 ,1.0 ),
    'FACIAL_R_TongueSide2':( 1.0,1.0,1.0 ,1.0 ),
    'FACIAL_R_TongueSide3':( 1.0,1.0,1.0 ,1.0 ),
    'FACIAL_C_MouthUpper':( 0.2,0.9,0.2 ,1.5 ),
    'FACIAL_C_Nose':( 0.2,0.9,0.2 ,1.5 ),
    'FACIAL_R_Ear_Cheek':( 0.2,0.9,0.2 ,1.5 ),
    'FACIAL_C_Forehead':( 0.2,0.9,0.2 ,1.5 ),
    'FACIAL_Eye':( 1.0,0.1,0.2 ,1.5 ),
    'FACIAL_L_Eye':( 1.0,0.1,0.2 ,1.5 ),
    'FACIAL_R_Eye':( 1.0,0.1,0.2 ,1.5 ),
    'FACIAL_Hair_A':( 0,0.3,0 ,2.5 ),
    'FACIAL_Hair_B':( 0,0.3,0 ,2.5 ),
    'FACIAL_Hair_C':( 0,0.3,0 ,2.5 ),
    'FACIAL_Hair_D':( 0,0.3,0 ,2.5 ),
    'FACIAL_R_Forehead_A':( 0,0.3,0 ,2.5 ),
    'FACIAL_R_Forehead_B':( 0,0.3,0 ,2.5 ),
    'FACIAL_R_Forehead_C':( 0,0.3,0 ,2.5 ),
    'FACIAL_R_Forehead_D':( 0,0.3,0 ,2.5 ),
    'FACIAL_R_Forehead_E':( 0,0.3,0 ,2.5 ),
    'FACIAL_R_EyeCorner':( 0.9,0.2,0.2 ,1.5 ),
    'FACIAL_L_12IPV_CheekOuter1':( 0.9,0.2,0.2 ,1.5 ),
    'FACIAL_R_12IPV_CheekOuter1':( 0.9,0.2,0.2 ,1.5 ),
    'FACIAL_L_EyesackUpper4':( 0.9,0.2,0.2 ,1.5 ),
    'FACIAL_R_EyesackUpper4':( 0.9,0.2,0.2 ,1.5 ),
    'FACIAL_C_NoseBridge':( 0.0,0.0,0.9 ,1.5 ),
    'FACIAL_C_NoseUpper':( 0.0,0.0,0.9 ,1.5 ),
    'FACIAL_C_12IPV_NoseBridge1':( 0.1,0.1,0.9 ,1.5 ),
    'FACIAL_C_12IPV_NoseUpper1':( 0.1,0.1,0.9 ,1.5 ),
    'FACIAL_L_12IPV_NasolabialF1':( 0.1,0.9,0.9 ,1.5 ),
    'FACIAL_R_12IPV_NasolabialF1':( 0.1,0.9,0.9 ,1.5 ),
    'FACIAL_C_LipUpperSkin':( 0.9,0.9,0.0 ,1.5 ),
    'FACIAL_C_12IPV_LipUpperSkin1':( 0.9,0.9,0.0 ,1.5 ),
    'FACIAL_C_12IPV_LipUpperSkin2':( 0.9,0.9,0.0 ,1.5 ),
    'FACIAL_R_NasolabialFurrow':( 0.0,0.9,0.9 ,1.5 ),
    'FACIAL_L_NasolabialFurrow':( 0.0,0.9,0.9 ,1.5 ),
    'FACIAL_C_LowerLipRotation':( 0.0,0.9,0.9 ,1.5 ),
    'FACIAL_R_Ear':( 0.9,0.9,0.0 ,1.5 ),
    'FACIAL_L_Ear':( 0.9,0.9,0.0 ,1.5 ),
    'FACIAL_R_CheekOuter':( 0.2,0.9,0.2 ,1.5 ),
    'FACIAL_L_CheekOuter':( 0.2,0.9,0.2 ,1.5 ),
    'FACIAL_R_CheekLower1':( 0.2,0.9,0.2 ,1.5 ),
    'FACIAL_L_CheekLower1':( 0.2,0.9,0.2 ,1.5 ),
    'FACIAL_R_12IPV_NasolabialB1':( 0.0,0.9,0.9 ,1.5 ),
    'FACIAL_L_12IPV_NasolabialB1':( 0.0,0.9,0.9 ,1.5 ),
    'FACIAL_R_NasolabialBulge1':( 0.0,0.9,0.9 ,1.5 ),
    'FACIAL_L_NasolabialBulge1':( 0.0,0.9,0.9 ,1.5 ),
    'FACIAL_R_CheekInner1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_L_CheekInner1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_R_12IPV_EyesackL2':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_L_12IPV_EyesackL2':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_R_12IPV_EyesackL1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_L_12IPV_EyesackL1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_R_EyelidLowerB1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_R_EyelidLowerA1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_R_EyelashesUpperA1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_R_EyelidUpperA1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_R_EyelidUpperB1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_R_EyelidUpperFurrow1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_R_EyesackUpper1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_R_EyeCornerInner1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_L_EyelidLowerB1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_L_EyelidLowerA1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_L_EyelashesUpperA1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_L_EyelidUpperA1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_L_EyelidUpperB1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_L_EyelidUpperFurrow1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_L_EyesackUpper1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_L_EyeCornerInner1':( 0.9,0.1,0.1 ,1.5 ),
    'FACIAL_C_12IPV_NoseUpper2':( 0.1,0.1,0.9 ,1.5 ),
    'FACIAL_R_12IPV_Nostril1':( 0.1,0.1,0.9 ,1.5 ),
    'FACIAL_L_12IPV_Nostril1':( 0.1,0.1,0.9 ,1.5 ),
    'FACIAL_C_12IPV_NoseTip1':( 0.1,0.1,0.9 ,1.5 ),
    'FACIAL_R_12IPV_LipUpper5':( 0.9,0.3,0.0 ,1.5 ),
    'FACIAL_C_LipUpper3':( 0.9,0.3,0.0 ,1.5 ),
    'FACIAL_C_LipUpper2':( 0.9,0.3,0.0 ,1.5 ),
    'FACIAL_C_LipUpper1':( 0.9,0.3,0.0 ,1.5 ),
    'FACIAL_R_12IPV_LipUpper1':( 0.9,0.3,0.0 ,1.5 ),
    'FACIAL_R_12IPV_LipLower1':( 0.9,0.3,0.0 ,1.5 ),
    'FACIAL_R_12IPV_LipLower5':( 0.9,0.3,0.0 ,1.5 ),
    'FACIAL_C_LipLower3':( 0.9,0.3,0.0 ,1.5 ),
    'FACIAL_C_LipLower1':( 0.9,0.3,0.0 ,1.5 ),
    'FACIAL_C_LipLower2':( 0.9,0.3,0.0 ,1.5 ),
    'FACIAL_R_ForeheadInA1':( 0.3,1.0,0.0 ,1.5 ),
    'FACIAL_L_ForeheadInA1':( 0.3,1.0,0.0 ,1.5 ),    
    'FACIAL_R_12IPV_ForeheadIn1':( 0.3,1.0,0.0 ,1.5 ),
    'FACIAL_L_12IPV_ForeheadIn1':( 0.3,1.0,0.0 ,1.5 ),
    'FACIAL_C_Forehead2':( 0.3,1.0,0.0 ,1.5 ),
    'FACIAL_C_12IPV_Forehead1':( 0.3,1.0,0.0 ,1.5 ),
    'FACIAL_L_LipCornerA1':( 0.3,1.0,0.0 ,1.5 ),
    'FACIAL_R_LipCornerA1':( 0.3,1.0,0.0 ,1.5 ),
    'FACIAL_C_12IPV_NoseLA1':( 0.3,1.0,0.0 ,1.5 )    
    }
customcurvelist={
'FACIAL_D_NeckA1':("DHIhead:FACIAL_L_12IPV_NeckB3","DHIhead:FACIAL_L_12IPV_NeckB5","DHIhead:FACIAL_L_12IPV_NeckB7",
           "DHIhead:FACIAL_L_12IPV_NeckBackB2","DHIhead:FACIAL_C_12IPV_NeckBackB2","DHIhead:FACIAL_R_12IPV_NeckBackB2","DHIhead:FACIAL_R_12IPV_NeckB7","DHIhead:FACIAL_R_12IPV_NeckB5","DHIhead:FACIAL_R_12IPV_NeckB3"),
'FACIAL_C_NeckF1':("DHIhead:FACIAL_C_12IPV_AdamsA1","DHIhead:FACIAL_C_AdamsApple",
           "DHIhead:FACIAL_C_12IPV_AdamsA2","DHIhead:FACIAL_C_12IPV_NeckB1","DHIhead:FACIAL_C_NeckB","DHIhead:FACIAL_C_12IPV_NeckB2"),
'FACIAL_C_NeckB1':("DHIhead:FACIAL_C_12IPV_NeckBackA1","DHIhead:FACIAL_C_NeckBackA","DHIhead:FACIAL_C_12IPV_NeckBackA2",
           "DHIhead:FACIAL_C_12IPV_NeckBackB1","DHIhead:FACIAL_C_NeckBackB"),
'FACIAL_L_NeckA1':("DHIhead:FACIAL_L_12IPV_NeckA3","DHIhead:FACIAL_L_NeckA2","DHIhead:FACIAL_L_12IPV_NeckA4",
           "DHIhead:FACIAL_L_12IPV_NeckB4","DHIhead:FACIAL_L_NeckB1"),
'FACIAL_L_NeckB1':("DHIhead:FACIAL_L_12IPV_NeckA5","DHIhead:FACIAL_L_NeckA3","DHIhead:FACIAL_L_12IPV_NeckA6",
           "DHIhead:FACIAL_L_12IPV_NeckB6","DHIhead:FACIAL_L_NeckB2"),
'FACIAL_L_NeckC1':("DHIhead:FACIAL_L_12IPV_NeckBackA1","DHIhead:FACIAL_L_NeckBackA","DHIhead:FACIAL_L_12IPV_NeckBackA2",
           "DHIhead:FACIAL_L_12IPV_NeckBackB1","DHIhead:FACIAL_L_NeckBackB"),
'FACIAL_L_NeckD1':("DHIhead:FACIAL_L_12IPV_NeckA1","DHIhead:FACIAL_L_NeckA1","DHIhead:FACIAL_L_12IPV_NeckA2"),

'FACIAL_R_NeckA1':("DHIhead:FACIAL_R_12IPV_NeckA3","DHIhead:FACIAL_R_NeckA2","DHIhead:FACIAL_R_12IPV_NeckA4",
           "DHIhead:FACIAL_R_12IPV_NeckB4","DHIhead:FACIAL_R_NeckB1"),
'FACIAL_R_NeckB1':("DHIhead:FACIAL_R_12IPV_NeckA5","DHIhead:FACIAL_R_NeckA3","DHIhead:FACIAL_R_12IPV_NeckA6",
           "DHIhead:FACIAL_R_12IPV_NeckB6","DHIhead:FACIAL_R_NeckB2"),
'FACIAL_R_NeckC1':("DHIhead:FACIAL_R_12IPV_NeckBackA1","DHIhead:FACIAL_R_NeckBackA","DHIhead:FACIAL_R_12IPV_NeckBackA2",
           "DHIhead:FACIAL_R_12IPV_NeckBackB1","DHIhead:FACIAL_R_NeckBackB"),
'FACIAL_R_NeckD1':("DHIhead:FACIAL_R_12IPV_NeckA1","DHIhead:FACIAL_R_NeckA1","DHIhead:FACIAL_R_12IPV_NeckA2"),

'FACIAL_C_UnderChin':("DHIhead:FACIAL_R_UnderChin","DHIhead:FACIAL_C_UnderChin","DHIhead:FACIAL_L_UnderChin"),

'FACIAL_C_UnderChin_A':("DHIhead:FACIAL_R_12IPV_UnderChin5","DHIhead:FACIAL_R_12IPV_UnderChin3",
                      "DHIhead:FACIAL_R_12IPV_UnderChin1","DHIhead:FACIAL_L_12IPV_UnderChin1","DHIhead:FACIAL_L_12IPV_UnderChin3","DHIhead:FACIAL_L_12IPV_UnderChin5"),
'FACIAL_C_UnderChin_B':("DHIhead:FACIAL_R_12IPV_UnderChin6","DHIhead:FACIAL_R_12IPV_UnderChin4",
                      "DHIhead:FACIAL_R_12IPV_UnderChin2","DHIhead:FACIAL_L_12IPV_UnderChin2","DHIhead:FACIAL_L_12IPV_UnderChin4","DHIhead:FACIAL_L_12IPV_UnderChin6"),
'FACIAL_C_Jawline':("DHIhead:FACIAL_R_Jawline","DHIhead:FACIAL_C_Jawline","DHIhead:FACIAL_L_Jawline"),

'FACIAL_C_Jawline_B':("DHIhead:FACIAL_R_12IPV_Jawline6","DHIhead:FACIAL_R_12IPV_Jawline4","DHIhead:FACIAL_R_12IPV_Jawline2",
                    "DHIhead:FACIAL_L_12IPV_Jawline2","DHIhead:FACIAL_L_12IPV_Jawline4","DHIhead:FACIAL_L_12IPV_Jawline6"),
'FACIAL_C_Jawline_A':("DHIhead:FACIAL_R_12IPV_Jawline5","DHIhead:FACIAL_R_12IPV_Jawline3","DHIhead:FACIAL_R_12IPV_Jawline1",
                    "DHIhead:FACIAL_L_12IPV_Jawline1","DHIhead:FACIAL_L_12IPV_Jawline3","DHIhead:FACIAL_L_12IPV_Jawline5"),
'FACIAL_C_Jawline_C':("DHIhead:FACIAL_R_Jawline2","DHIhead:FACIAL_R_Jawline1","DHIhead:FACIAL_L_Jawline1",
                    "DHIhead:FACIAL_L_Jawline2"),

'FACIAL_C_Chin1': ("DHIhead:FACIAL_R_Chin1","DHIhead:FACIAL_C_Chin1","DHIhead:FACIAL_L_Chin1","DHIhead:FACIAL_L_Chin2",
                  "DHIhead:FACIAL_C_Chin2","DHIhead:FACIAL_R_Chin2","DHIhead:FACIAL_R_Chin3","DHIhead:FACIAL_C_Chin3","DHIhead:FACIAL_L_Chin3"),

'FACIAL_LR_12IPV_ChinS1':("DHIhead:FACIAL_R_12IPV_ChinS1","DHIhead:FACIAL_R_12IPV_ChinS3","DHIhead:FACIAL_L_12IPV_ChinS3",
                        "DHIhead:FACIAL_L_12IPV_ChinS1"),
'FACIAL_LR_12IPV_ChinS2':("DHIhead:FACIAL_R_12IPV_ChinS2","DHIhead:FACIAL_R_12IPV_ChinS4","DHIhead:FACIAL_L_12IPV_ChinS4",
                        "DHIhead:FACIAL_L_12IPV_ChinS2"),

'FACIAL_R_12IPV_ChinA':("DHIhead:FACIAL_R_12IPV_Chin12","DHIhead:FACIAL_R_12IPV_Chin11","DHIhead:FACIAL_R_12IPV_Chin10",
                      "DHIhead:FACIAL_R_12IPV_Chin9"),
'FACIAL_R_12IPV_ChinB': ("DHIhead:FACIAL_R_12IPV_Chin14","DHIhead:FACIAL_R_12IPV_Chin13","DHIhead:FACIAL_R_12IPV_Chin8",
                        "DHIhead:FACIAL_R_12IPV_Chin2","DHIhead:FACIAL_R_12IPV_Chin7","DHIhead:FACIAL_R_12IPV_Chin6","DHIhead:FACIAL_R_12IPV_Chin1","DHIhead:FACIAL_R_12IPV_Chin5"),

'FACIAL_C_12IPV_ChinA':("DHIhead:FACIAL_C_12IPV_Chin3","DHIhead:FACIAL_C_12IPV_Chin4"),
'FACIAL_L_12IPV_ChinA':("DHIhead:FACIAL_L_12IPV_Chin12","DHIhead:FACIAL_L_12IPV_Chin11","DHIhead:FACIAL_L_12IPV_Chin10",
                      "DHIhead:FACIAL_L_12IPV_Chin9"),
'FACIAL_L_12IPV_ChinB': ("DHIhead:FACIAL_L_12IPV_Chin14","DHIhead:FACIAL_L_12IPV_Chin13","DHIhead:FACIAL_L_12IPV_Chin8",
                        "DHIhead:FACIAL_L_12IPV_Chin2","DHIhead:FACIAL_L_12IPV_Chin7","DHIhead:FACIAL_L_12IPV_Chin6","DHIhead:FACIAL_L_12IPV_Chin1","DHIhead:FACIAL_L_12IPV_Chin5"),
'FACIAL_C_Chin': ("DHIhead:FACIAL_R_ChinSide","DHIhead:FACIAL_C_Chin","DHIhead:FACIAL_L_ChinSide"),

'FACIAL_R_12IPV_MouthInteriorLower1': ("DHIhead:FACIAL_R_12IPV_MouthInteriorLower2",
                                      "DHIhead:FACIAL_R_12IPV_MouthInteriorLower1","DHIhead:FACIAL_L_12IPV_MouthInteriorLower1","DHIhead:FACIAL_L_12IPV_MouthInteriorLower2"),
'FACIAL_C_LipLowerSkin': ("DHIhead:FACIAL_R_LipLowerOuterSkin","DHIhead:FACIAL_R_LipLowerSkin","DHIhead:FACIAL_C_LipLowerSkin",
                         "DHIhead:FACIAL_L_LipLowerSkin","DHIhead:FACIAL_L_LipLowerOuterSkin"),
'FACIAL_C_12IPV_LipLowerSkin1':("DHIhead:FACIAL_R_12IPV_LipLowerOuterSkin3","DHIhead:FACIAL_R_12IPV_LipLowerOuterSkin1",
                              "DHIhead:FACIAL_C_12IPV_LipLowerSkin1","DHIhead:FACIAL_L_12IPV_LipLowerOuterSkin1","DHIhead:FACIAL_L_12IPV_LipLowerOuterSkin3"),
'FACIAL_C_12IPV_LipLowerSkin2':("DHIhead:FACIAL_R_12IPV_LipLowerOuterSkin2","DHIhead:FACIAL_R_12IPV_LipLowerSkin",
                              "DHIhead:FACIAL_C_12IPV_LipLowerSkin2","DHIhead:FACIAL_L_12IPV_LipLowerSkin",
                              "DHIhead:FACIAL_L_12IPV_LipLowerOuterSkin2"),

'FACIAL_C_LipUpper':("DHIhead:FACIAL_R_LipCorner","DHIhead:FACIAL_R_LipUpperOuter","DHIhead:FACIAL_R_LipUpper",
                    "DHIhead:FACIAL_C_LipUpper","DHIhead:FACIAL_L_LipUpper","DHIhead:FACIAL_L_LipUpperOuter","DHIhead:FACIAL_L_LipCorner"),
'FACIAL_C_LipLower':("DHIhead:FACIAL_R_LipLowerOuter","DHIhead:FACIAL_R_LipLower","DHIhead:FACIAL_C_LipLower",
                   "DHIhead:FACIAL_L_LipLower","DHIhead:FACIAL_L_LipLowerOuter"),

'FACIAL_R_JawBulge':("DHIhead:FACIAL_R_JawBulge","DHIhead:FACIAL_R_CheekLower","DHIhead:FACIAL_R_NasolabialBulge",
                   "DHIhead:FACIAL_L_NasolabialBulge","DHIhead:FACIAL_L_CheekLower","DHIhead:FACIAL_L_JawBulge"),
'FACIAL_R_12IPV_MouthInteriorUpper1':("DHIhead:FACIAL_R_12IPV_MouthInteriorUpper2",
                                    "DHIhead:FACIAL_R_12IPV_MouthInteriorUpper1",
                                    "DHIhead:FACIAL_L_12IPV_MouthInteriorUpper1","DHIhead:FACIAL_L_12IPV_MouthInteriorUpper2"),

'FACIAL_C_TeethUpper':("DHIhead:FACIAL_C_TeethUpper","DHIhead:FACIAL_C_TeethLower"),
'FACIAL_C_Tongue1':("DHIhead:FACIAL_C_Tongue1","DHIhead:FACIAL_C_Tongue2","DHIhead:FACIAL_C_Tongue3",
                    "DHIhead:FACIAL_C_Tongue4"),
'FACIAL_R_TongueSide2':("DHIhead:FACIAL_R_TongueSide2","DHIhead:FACIAL_C_TongueUpper2","DHIhead:FACIAL_L_TongueSide2"),
'FACIAL_R_TongueSide3':("DHIhead:FACIAL_R_TongueSide3","DHIhead:FACIAL_C_TongueUpper3","DHIhead:FACIAL_L_TongueSide3",
                      "DHIhead:FACIAL_C_TongueLower3"),
'FACIAL_C_MouthUpper':("DHIhead:FACIAL_C_MouthUpper","DHIhead:FACIAL_C_MouthLower"),

'FACIAL_C_Nose': ("DHIhead:FACIAL_C_Nose","DHIhead:FACIAL_R_Nostril","DHIhead:FACIAL_C_NoseTip","DHIhead:FACIAL_C_NoseLower",
                 "DHIhead:FACIAL_L_Nostril"),
'FACIAL_R_Ear_Cheek':("DHIhead:FACIAL_R_Ear","DHIhead:FACIAL_R_CheekOuter","DHIhead:FACIAL_R_CheekInner",
                    "DHIhead:FACIAL_L_CheekInner","DHIhead:FACIAL_L_CheekOuter","DHIhead:FACIAL_L_Ear"),
'FACIAL_C_Forehead':("DHIhead:FACIAL_R_ForeheadOut","DHIhead:FACIAL_R_ForeheadMid","DHIhead:FACIAL_R_ForeheadIn",
                   "DHIhead:FACIAL_C_Forehead","DHIhead:FACIAL_L_ForeheadIn","DHIhead:FACIAL_L_ForeheadMid","DHIhead:FACIAL_L_ForeheadOut"),
'FACIAL_R_Eye':("DHIhead:FACIAL_R_EyesackUpper","DHIhead:FACIAL_R_EyelidUpperFurrow","DHIhead:FACIAL_R_EyelidUpperB",
              "DHIhead:FACIAL_R_EyelidUpperA","DHIhead:FACIAL_R_EyeParallel","DHIhead:FACIAL_R_EyelidLowerA","DHIhead:FACIAL_R_EyelidLowerB","DHIhead:FACIAL_R_EyesackLower"),

'FACIAL_L_Eye':("DHIhead:FACIAL_L_EyesackUpper","DHIhead:FACIAL_L_EyelidUpperFurrow","DHIhead:FACIAL_L_EyelidUpperB",
              "DHIhead:FACIAL_L_EyelidUpperA","DHIhead:FACIAL_L_EyeParallel","DHIhead:FACIAL_L_EyelidLowerA","DHIhead:FACIAL_L_EyelidLowerB","DHIhead:FACIAL_L_EyesackLower"),

'FACIAL_Hair_A':("DHIhead:FACIAL_R_HairC4","DHIhead:FACIAL_R_HairC3","DHIhead:FACIAL_R_HairB5","DHIhead:FACIAL_R_HairA6",
               "DHIhead:FACIAL_C_Hair6","DHIhead:FACIAL_L_HairA6","DHIhead:FACIAL_L_HairB5","DHIhead:FACIAL_L_HairC3","DHIhead:FACIAL_L_HairC4"),
'FACIAL_Hair_B':("DHIhead:FACIAL_R_JawRecess","DHIhead:FACIAL_R_Sideburn6","DHIhead:FACIAL_R_Sideburn3",
               "DHIhead:FACIAL_R_HairC2","DHIhead:FACIAL_R_HairB4","DHIhead:FACIAL_R_HairA5","DHIhead:FACIAL_C_Hair5","DHIhead:FACIAL_L_HairA5","DHIhead:FACIAL_L_HairB4","DHIhead:FACIAL_L_HairC2","DHIhead:FACIAL_L_Sideburn3","DHIhead:FACIAL_L_Sideburn6","DHIhead:FACIAL_L_JawRecess"),
'FACIAL_Hair_C':("DHIhead:FACIAL_R_Sideburn5","DHIhead:FACIAL_R_Sideburn2","DHIhead:FACIAL_R_HairC1","DHIhead:FACIAL_R_HairB3",
               "DHIhead:FACIAL_R_HairA4","DHIhead:FACIAL_C_Hair4","DHIhead:FACIAL_L_HairA4","DHIhead:FACIAL_L_HairB3","DHIhead:FACIAL_L_HairC1","DHIhead:FACIAL_L_Sideburn2","DHIhead:FACIAL_L_Sideburn5"),
'FACIAL_Hair_D':("DHIhead:FACIAL_R_Masseter","DHIhead:FACIAL_R_Sideburn4","DHIhead:FACIAL_R_Sideburn1",
               "DHIhead:FACIAL_R_12IPV_Temple4","DHIhead:FACIAL_R_HairB2","DHIhead:FACIAL_R_HairA3","DHIhead:FACIAL_C_Hair3","DHIhead:FACIAL_L_HairA3","DHIhead:FACIAL_L_HairB2","DHIhead:FACIAL_L_12IPV_Temple4","DHIhead:FACIAL_L_Sideburn1","DHIhead:FACIAL_L_Sideburn4","DHIhead:FACIAL_L_Masseter"),


'FACIAL_R_Forehead_A':("DHIhead:FACIAL_R_12IPV_Temple3","DHIhead:FACIAL_R_ForeheadOutSkin","DHIhead:FACIAL_R_ForeheadMidSkin",
                     "DHIhead:FACIAL_R_12IPV_ForeheadSkin6","DHIhead:FACIAL_R_12IPV_ForeheadSkin4","DHIhead:FACIAL_R_12IPV_ForeheadSkin2","DHIhead:FACIAL_L_12IPV_ForeheadSkin2","DHIhead:FACIAL_L_12IPV_ForeheadSkin4","DHIhead:FACIAL_L_12IPV_ForeheadSkin6","DHIhead:FACIAL_L_ForeheadMidSkin","DHIhead:FACIAL_L_ForeheadOutSkin","DHIhead:FACIAL_L_12IPV_Temple3"),
'FACIAL_R_Forehead_B':("DHIhead:FACIAL_R_ForeheadInSkin","DHIhead:FACIAL_C_ForeheadSkin","DHIhead:FACIAL_L_ForeheadInSkin"),
'FACIAL_R_Forehead_C':("DHIhead:FACIAL_R_12IPV_ForeheadSkin5","DHIhead:FACIAL_R_12IPV_ForeheadSkin3",
                     "DHIhead:FACIAL_R_12IPV_ForeheadSkin1","DHIhead:FACIAL_L_12IPV_ForeheadSkin1","DHIhead:FACIAL_L_12IPV_ForeheadSkin3","DHIhead:FACIAL_L_12IPV_ForeheadSkin5"),
'FACIAL_R_Forehead_D':("DHIhead:FACIAL_R_Temple","DHIhead:FACIAL_R_HairB1","DHIhead:FACIAL_R_HairA1",
                     "DHIhead:FACIAL_R_12IPV_Hair1","DHIhead:FACIAL_C_Hair1","DHIhead:FACIAL_L_12IPV_Hair1","DHIhead:FACIAL_L_HairA1","DHIhead:FACIAL_L_HairB1","DHIhead:FACIAL_L_Temple"),
'FACIAL_R_Forehead_E':("DHIhead:FACIAL_R_HairA2","DHIhead:FACIAL_C_Hair2","DHIhead:FACIAL_L_HairA2"),

'FACIAL_R_EyeCorner':("DHIhead:FACIAL_R_EyeCornerOuter","DHIhead:FACIAL_R_EyeCornerInner","DHIhead:FACIAL_L_EyeCornerInner",
                    "DHIhead:FACIAL_L_EyeCornerOuter"),

'FACIAL_L_12IPV_CheekOuter1':("DHIhead:FACIAL_L_12IPV_CheekOuter1","DHIhead:FACIAL_L_12IPV_CheekOuter2",
                            "DHIhead:FACIAL_L_12IPV_CheekOuter4","DHIhead:FACIAL_L_12IPV_CheekOuter3"),
'FACIAL_R_12IPV_CheekOuter1':("DHIhead:FACIAL_R_12IPV_CheekOuter1","DHIhead:FACIAL_R_12IPV_CheekOuter2",
                            "DHIhead:FACIAL_R_12IPV_CheekOuter4","DHIhead:FACIAL_R_12IPV_CheekOuter3"),

'FACIAL_L_EyesackUpper4':("DHIhead:FACIAL_L_12IPV_Temple1","DHIhead:FACIAL_L_12IPV_Temple2","DHIhead:FACIAL_L_CheekOuter4",
                        "DHIhead:FACIAL_L_EyesackUpper4","DHIhead:FACIAL_L_12IPV_EyeCornerO1","DHIhead:FACIAL_L_12IPV_EyeCornerO2"),
'FACIAL_R_EyesackUpper4':("DHIhead:FACIAL_R_12IPV_Temple1","DHIhead:FACIAL_R_12IPV_Temple2","DHIhead:FACIAL_R_CheekOuter4",
                        "DHIhead:FACIAL_R_EyesackUpper4","DHIhead:FACIAL_R_12IPV_EyeCornerO1","DHIhead:FACIAL_R_12IPV_EyeCornerO2"),
'FACIAL_C_NoseBridge':("DHIhead:FACIAL_R_12IPV_EyesackU0","DHIhead:FACIAL_R_NoseBridge","DHIhead:FACIAL_C_NoseBridge",
                     "DHIhead:FACIAL_L_NoseBridge","DHIhead:FACIAL_L_12IPV_EyesackU0"),
'FACIAL_C_NoseUpper': ("DHIhead:FACIAL_R_NoseUpper","DHIhead:FACIAL_C_NoseUpper","DHIhead:FACIAL_L_NoseUpper"),

'FACIAL_C_12IPV_NoseBridge1': ("DHIhead:FACIAL_R_12IPV_NoseBridge1","DHIhead:FACIAL_C_12IPV_NoseBridge1",
                              "DHIhead:FACIAL_L_12IPV_NoseBridge1","DHIhead:FACIAL_L_12IPV_NoseBridge2","DHIhead:FACIAL_C_12IPV_NoseBridge2","DHIhead:FACIAL_R_12IPV_NoseBridge2"),

'FACIAL_Eye':("DHIhead:FACIAL_R_Eye","DHIhead:FACIAL_L_Eye"),

'FACIAL_C_12IPV_NoseUpper1':("DHIhead:FACIAL_R_12IPV_NoseUpper5","DHIhead:FACIAL_R_12IPV_NoseUpper3",
                           "DHIhead:FACIAL_R_12IPV_NoseUpper1","DHIhead:FACIAL_C_12IPV_NoseUpper1","DHIhead:FACIAL_L_12IPV_NoseUpper1","DHIhead:FACIAL_L_12IPV_NoseUpper3","DHIhead:FACIAL_L_12IPV_NoseUpper5","DHIhead:FACIAL_L_12IPV_NoseUpper6","DHIhead:FACIAL_L_12IPV_NoseUpper4","DHIhead:FACIAL_L_12IPV_NoseUpper2","DHIhead:FACIAL_C_12IPV_NoseUpper2","DHIhead:FACIAL_R_12IPV_NoseUpper2","DHIhead:FACIAL_R_12IPV_NoseUpper4","DHIhead:FACIAL_R_12IPV_NoseUpper6"),

'FACIAL_R_12IPV_NasolabialF1':("DHIhead:FACIAL_R_12IPV_NasolabialF1","DHIhead:FACIAL_R_12IPV_NasolabialF2",
                             "DHIhead:FACIAL_R_12IPV_NasolabialF3","DHIhead:FACIAL_R_12IPV_NasolabialF4","DHIhead:FACIAL_R_12IPV_NasolabialF5","DHIhead:FACIAL_R_12IPV_NasolabialF6","DHIhead:FACIAL_R_12IPV_NasolabialF7","DHIhead:FACIAL_R_12IPV_NasolabialF8","DHIhead:FACIAL_R_12IPV_NasolabialF9"),
'FACIAL_L_12IPV_NasolabialF1':("DHIhead:FACIAL_L_12IPV_NasolabialF1","DHIhead:FACIAL_L_12IPV_NasolabialF2",
                             "DHIhead:FACIAL_L_12IPV_NasolabialF3","DHIhead:FACIAL_L_12IPV_NasolabialF4","DHIhead:FACIAL_L_12IPV_NasolabialF5","DHIhead:FACIAL_L_12IPV_NasolabialF6","DHIhead:FACIAL_L_12IPV_NasolabialF7","DHIhead:FACIAL_L_12IPV_NasolabialF8","DHIhead:FACIAL_L_12IPV_NasolabialF9"),

'FACIAL_C_LipUpperSkin':("DHIhead:FACIAL_R_LipUpperOuterSkin","DHIhead:FACIAL_R_LipUpperSkin",
                       "DHIhead:FACIAL_C_LipUpperSkin","DHIhead:FACIAL_L_LipUpperSkin","DHIhead:FACIAL_L_LipUpperOuterSkin"),


'FACIAL_C_12IPV_LipUpperSkin1':("DHIhead:FACIAL_R_12IPV_LipUpperOuterSkin1","DHIhead:FACIAL_R_12IPV_LipUpperSkin",
                              "DHIhead:FACIAL_C_12IPV_LipUpperSkin1","DHIhead:FACIAL_L_12IPV_LipUpperSkin","DHIhead:FACIAL_L_12IPV_LipUpperOuterSkin1"),
'FACIAL_C_12IPV_LipUpperSkin2':("DHIhead:FACIAL_R_12IPV_LipUpperOuterSkin2","DHIhead:FACIAL_C_12IPV_LipUpperSkin2",
                              "DHIhead:FACIAL_L_12IPV_LipUpperOuterSkin2"),

'FACIAL_R_NasolabialFurrow':("DHIhead:FACIAL_R_12IPV_NasolabialB14","DHIhead:FACIAL_R_12IPV_NasolabialB15",
                           "DHIhead:FACIAL_R_NasolabialBulge1","DHIhead:FACIAL_R_12IPV_NasolabialB13","DHIhead:FACIAL_R_NasolabialFurrow"),
'FACIAL_L_NasolabialFurrow':("DHIhead:FACIAL_L_12IPV_NasolabialB14","DHIhead:FACIAL_L_12IPV_NasolabialB15",
                           "DHIhead:FACIAL_L_NasolabialBulge1","DHIhead:FACIAL_L_12IPV_NasolabialB13","DHIhead:FACIAL_L_NasolabialFurrow"),
'FACIAL_C_LowerLipRotation':("DHIhead:FACIAL_C_LowerLipRotation","DHIhead:FACIAL_C_Jaw","DHIhead:FACIAL_C_Skull"),

'FACIAL_R_Ear':("DHIhead:FACIAL_R_Ear","DHIhead:FACIAL_R_Ear1","DHIhead:FACIAL_R_Ear2","DHIhead:FACIAL_R_Ear3","DHIhead:FACIAL_R_Ear4"),
'FACIAL_L_Ear':("DHIhead:FACIAL_L_Ear","DHIhead:FACIAL_L_Ear1","DHIhead:FACIAL_L_Ear2","DHIhead:FACIAL_L_Ear3","DHIhead:FACIAL_L_Ear4"),

'FACIAL_R_CheekOuter':("DHIhead:FACIAL_R_CheekOuter3","DHIhead:FACIAL_R_CheekOuter1","DHIhead:FACIAL_R_CheekOuter2"),
'FACIAL_L_CheekOuter':("DHIhead:FACIAL_L_CheekOuter3","DHIhead:FACIAL_L_CheekOuter1","DHIhead:FACIAL_L_CheekOuter2"),

'FACIAL_R_CheekLower1':("DHIhead:FACIAL_R_12IPV_CheekL3","DHIhead:FACIAL_R_12IPV_CheekL1","DHIhead:FACIAL_R_CheekLower2",
                      "DHIhead:FACIAL_R_CheekLower1","DHIhead:FACIAL_R_12IPV_CheekL4","DHIhead:FACIAL_R_12IPV_CheekL2"),
'FACIAL_L_CheekLower1':("DHIhead:FACIAL_L_12IPV_CheekL3","DHIhead:FACIAL_L_12IPV_CheekL1","DHIhead:FACIAL_L_CheekLower2",
                      "DHIhead:FACIAL_L_CheekLower1","DHIhead:FACIAL_L_12IPV_CheekL4","DHIhead:FACIAL_L_12IPV_CheekL2"),

'FACIAL_R_12IPV_NasolabialB1':("DHIhead:FACIAL_R_12IPV_NasolabialB1","DHIhead:FACIAL_R_12IPV_NasolabialB2",
                             "DHIhead:FACIAL_R_12IPV_NasolabialB3","DHIhead:FACIAL_R_12IPV_NasolabialB4","DHIhead:FACIAL_R_12IPV_NasolabialB5","DHIhead:FACIAL_R_12IPV_NasolabialB6","DHIhead:FACIAL_R_12IPV_NasolabialB7","DHIhead:FACIAL_R_12IPV_NasolabialB8","DHIhead:FACIAL_R_12IPV_NasolabialB9","DHIhead:FACIAL_R_12IPV_NasolabialB10","DHIhead:FACIAL_R_12IPV_NasolabialB11","DHIhead:FACIAL_R_12IPV_NasolabialB12"),
'FACIAL_L_12IPV_NasolabialB1':("DHIhead:FACIAL_L_12IPV_NasolabialB1","DHIhead:FACIAL_L_12IPV_NasolabialB2",
                             "DHIhead:FACIAL_L_12IPV_NasolabialB3","DHIhead:FACIAL_L_12IPV_NasolabialB4","DHIhead:FACIAL_L_12IPV_NasolabialB5","DHIhead:FACIAL_L_12IPV_NasolabialB6","DHIhead:FACIAL_L_12IPV_NasolabialB7","DHIhead:FACIAL_L_12IPV_NasolabialB8","DHIhead:FACIAL_L_12IPV_NasolabialB9","DHIhead:FACIAL_L_12IPV_NasolabialB10","DHIhead:FACIAL_L_12IPV_NasolabialB11","DHIhead:FACIAL_L_12IPV_NasolabialB12"),
'FACIAL_R_NasolabialBulge1':("DHIhead:FACIAL_R_NasolabialBulge1","DHIhead:FACIAL_R_NasolabialBulge2",
                           "DHIhead:FACIAL_R_NasolabialBulge3"),
'FACIAL_L_NasolabialBulge1':("DHIhead:FACIAL_L_NasolabialBulge1","DHIhead:FACIAL_L_NasolabialBulge2",
                           "DHIhead:FACIAL_L_NasolabialBulge3"),

'FACIAL_R_CheekInner1':("DHIhead:FACIAL_R_CheekOuter3","DHIhead:FACIAL_R_CheekOuter1","DHIhead:FACIAL_R_CheekInner3",
                      "DHIhead:FACIAL_R_CheekInner1"),
'FACIAL_L_CheekInner1':("DHIhead:FACIAL_L_CheekOuter3","DHIhead:FACIAL_L_CheekOuter1","DHIhead:FACIAL_L_CheekInner3",
                      "DHIhead:FACIAL_L_CheekInner1"),

'FACIAL_R_12IPV_EyesackL2':("DHIhead:FACIAL_R_12IPV_EyesackL8","DHIhead:FACIAL_R_12IPV_EyesackL6",
                           "DHIhead:FACIAL_R_12IPV_EyesackL4","DHIhead:FACIAL_R_12IPV_EyesackL2"),
'FACIAL_L_12IPV_EyesackL2':("DHIhead:FACIAL_L_12IPV_EyesackL8","DHIhead:FACIAL_L_12IPV_EyesackL6",
                           "DHIhead:FACIAL_L_12IPV_EyesackL4","DHIhead:FACIAL_L_12IPV_EyesackL2"),
'FACIAL_R_12IPV_EyesackL1': ("DHIhead:FACIAL_R_12IPV_EyesackL7","DHIhead:FACIAL_R_EyesackLower2","DHIhead:FACIAL_R_12IPV_EyesackL5",
                            "DHIhead:FACIAL_R_12IPV_EyesackL3","DHIhead:FACIAL_R_EyesackLower1","DHIhead:FACIAL_R_12IPV_EyesackL1"),
'FACIAL_L_12IPV_EyesackL1': ("DHIhead:FACIAL_L_12IPV_EyesackL7","DHIhead:FACIAL_L_EyesackLower2","DHIhead:FACIAL_L_12IPV_EyesackL5",
                            "DHIhead:FACIAL_L_12IPV_EyesackL3","DHIhead:FACIAL_L_EyesackLower1","DHIhead:FACIAL_L_12IPV_EyesackL1"),

'FACIAL_R_EyelidLowerB1':("DHIhead:FACIAL_R_EyelidLowerB3","DHIhead:FACIAL_R_EyelidLowerB2","DHIhead:FACIAL_R_EyelidLowerB1"),
'FACIAL_R_EyelidLowerA1':("DHIhead:FACIAL_R_EyelidLowerA3","DHIhead:FACIAL_R_EyelidLowerA2","DHIhead:FACIAL_R_EyelidLowerA1"),
'FACIAL_R_EyelashesUpperA1':("DHIhead:FACIAL_R_EyelashesUpperA3","DHIhead:FACIAL_R_EyelashesUpperA2",
                           "DHIhead:FACIAL_R_EyelashesUpperA1"),
'FACIAL_R_EyelidUpperA1':("DHIhead:FACIAL_R_EyelidUpperA3","DHIhead:FACIAL_R_EyelidUpperA2","DHIhead:FACIAL_R_EyelidUpperA1"),
'FACIAL_R_EyelidUpperB1':("DHIhead:FACIAL_R_EyelidUpperB3","DHIhead:FACIAL_R_EyelidUpperB2","DHIhead:FACIAL_R_EyelidUpperB1"),

'FACIAL_R_EyelidUpperFurrow1':("DHIhead:FACIAL_R_EyelidUpperFurrow3","DHIhead:FACIAL_R_EyelidUpperFurrow2",
                             "DHIhead:FACIAL_R_EyelidUpperFurrow1"),
'FACIAL_R_EyesackUpper1':("DHIhead:FACIAL_R_EyesackUpper3","DHIhead:FACIAL_R_EyesackUpper2","DHIhead:FACIAL_R_EyesackUpper1"),
'FACIAL_R_EyeCornerInner1':("DHIhead:FACIAL_R_EyeCornerOuter1","DHIhead:FACIAL_R_EyeCornerOuter2","DHIhead:FACIAL_R_EyeCornerInner2","DHIhead:FACIAL_R_EyeCornerInner1"),


'FACIAL_L_EyelidLowerB1':("DHIhead:FACIAL_L_EyelidLowerB3","DHIhead:FACIAL_L_EyelidLowerB2","DHIhead:FACIAL_L_EyelidLowerB1"),
'FACIAL_L_EyelidLowerA1':("DHIhead:FACIAL_L_EyelidLowerA3","DHIhead:FACIAL_L_EyelidLowerA2","DHIhead:FACIAL_L_EyelidLowerA1"),
'FACIAL_L_EyelashesUpperA1':("DHIhead:FACIAL_L_EyelashesUpperA3","DHIhead:FACIAL_L_EyelashesUpperA2",
                           "DHIhead:FACIAL_L_EyelashesUpperA1"),
'FACIAL_L_EyelidUpperA1':("DHIhead:FACIAL_L_EyelidUpperA3","DHIhead:FACIAL_L_EyelidUpperA2","DHIhead:FACIAL_L_EyelidUpperA1"),
'FACIAL_L_EyelidUpperB1':("DHIhead:FACIAL_L_EyelidUpperB3","DHIhead:FACIAL_L_EyelidUpperB2","DHIhead:FACIAL_L_EyelidUpperB1"),

'FACIAL_L_EyelidUpperFurrow1':("DHIhead:FACIAL_L_EyelidUpperFurrow3","DHIhead:FACIAL_L_EyelidUpperFurrow2",
                             "DHIhead:FACIAL_L_EyelidUpperFurrow1"),
'FACIAL_L_EyesackUpper1':("DHIhead:FACIAL_L_EyesackUpper3","DHIhead:FACIAL_L_EyesackUpper2","DHIhead:FACIAL_L_EyesackUpper1"),
'FACIAL_L_EyeCornerInner1':("DHIhead:FACIAL_L_EyeCornerOuter1","DHIhead:FACIAL_L_EyeCornerOuter2","DHIhead:FACIAL_L_EyeCornerInner2","DHIhead:FACIAL_L_EyeCornerInner1"),

'FACIAL_C_12IPV_NoseUpper2':("DHIhead:FACIAL_R_CheekInner4","DHIhead:FACIAL_R_CheekInner2","DHIhead:FACIAL_R_12IPV_NoseUpper6",
                           "DHIhead:FACIAL_R_12IPV_NoseUpper4","DHIhead:FACIAL_R_12IPV_NoseUpper2","DHIhead:FACIAL_C_12IPV_NoseUpper2","DHIhead:FACIAL_L_12IPV_NoseUpper2","DHIhead:FACIAL_L_12IPV_NoseUpper4","DHIhead:FACIAL_L_12IPV_NoseUpper6","DHIhead:FACIAL_L_CheekInner2","DHIhead:FACIAL_L_CheekInner4"),


'FACIAL_R_12IPV_Nostril1':("DHIhead:FACIAL_R_12IPV_Nostril1","DHIhead:FACIAL_R_12IPV_Nostril4",
                         "DHIhead:FACIAL_R_12IPV_Nostril6","DHIhead:FACIAL_R_12IPV_Nostril9","DHIhead:FACIAL_R_NostrilThickness1","DHIhead:FACIAL_R_NostrilThickness2","DHIhead:FACIAL_R_12IPV_Nostril10","DHIhead:FACIAL_R_12IPV_Nostril7","DHIhead:FACIAL_R_12IPV_Nostril5","DHIhead:FACIAL_R_12IPV_Nostril2","DHIhead:FACIAL_R_12IPV_Nostril3","DHIhead:FACIAL_R_12IPV_Nostril8","DHIhead:FACIAL_R_12IPV_Nostril11","DHIhead:FACIAL_R_12IPV_Nostril12","DHIhead:FACIAL_R_12IPV_Nostril14","DHIhead:FACIAL_R_12IPV_Nostril13"),
'FACIAL_L_12IPV_Nostril1':("DHIhead:FACIAL_L_12IPV_Nostril1","DHIhead:FACIAL_L_12IPV_Nostril4",
                         "DHIhead:FACIAL_L_12IPV_Nostril6","DHIhead:FACIAL_L_12IPV_Nostril9","DHIhead:FACIAL_L_NostrilThickness1","DHIhead:FACIAL_L_NostrilThickness2","DHIhead:FACIAL_L_12IPV_Nostril10","DHIhead:FACIAL_L_12IPV_Nostril7","DHIhead:FACIAL_L_12IPV_Nostril5","DHIhead:FACIAL_L_12IPV_Nostril2","DHIhead:FACIAL_L_12IPV_Nostril3","DHIhead:FACIAL_L_12IPV_Nostril8","DHIhead:FACIAL_L_12IPV_Nostril11","DHIhead:FACIAL_L_12IPV_Nostril12","DHIhead:FACIAL_L_12IPV_Nostril14","DHIhead:FACIAL_L_12IPV_Nostril13"),

'FACIAL_C_12IPV_NoseTip1':("DHIhead:FACIAL_R_12IPV_NoseTip1","DHIhead:FACIAL_C_12IPV_NoseTip1",
                         "DHIhead:FACIAL_L_12IPV_NoseTip1","DHIhead:FACIAL_L_12IPV_NoseTip2","DHIhead:FACIAL_C_12IPV_NoseTip2","DHIhead:FACIAL_R_12IPV_NoseTip2","DHIhead:FACIAL_R_12IPV_NoseTip3","DHIhead:FACIAL_C_12IPV_NoseTip3","DHIhead:FACIAL_L_12IPV_NoseTip3"),

'FACIAL_R_12IPV_LipUpper5':("DHIhead:FACIAL_R_12IPV_LipUpper24","DHIhead:FACIAL_R_12IPV_LipUpper22",
                          "DHIhead:FACIAL_R_12IPV_LipUpper15","DHIhead:FACIAL_R_12IPV_LipUpper13","DHIhead:FACIAL_R_12IPV_LipUpper5","DHIhead:FACIAL_L_12IPV_LipUpper5","DHIhead:FACIAL_L_12IPV_LipUpper13","DHIhead:FACIAL_L_12IPV_LipUpper15","DHIhead:FACIAL_L_12IPV_LipUpper22","DHIhead:FACIAL_L_12IPV_LipUpper24"),

'FACIAL_C_LipUpper3':("DHIhead:FACIAL_R_12IPV_LipUpper23","DHIhead:FACIAL_R_LipUpperOuter3","DHIhead:FACIAL_R_12IPV_LipUpper21",
                    "DHIhead:FACIAL_R_12IPV_LipUpper14","DHIhead:FACIAL_R_LipUpper3","DHIhead:FACIAL_R_12IPV_LipUpper12","DHIhead:FACIAL_R_12IPV_LipUpper4","DHIhead:FACIAL_C_LipUpper3","DHIhead:FACIAL_L_12IPV_LipUpper4","DHIhead:FACIAL_L_12IPV_LipUpper12","DHIhead:FACIAL_L_LipUpper3","DHIhead:FACIAL_L_12IPV_LipUpper14","DHIhead:FACIAL_L_12IPV_LipUpper21","DHIhead:FACIAL_L_LipUpperOuter3","DHIhead:FACIAL_L_12IPV_LipUpper23"),

'FACIAL_C_LipUpper2':("DHIhead:FACIAL_R_12IPV_LipUpper20","DHIhead:FACIAL_R_LipUpperOuter2","DHIhead:FACIAL_R_12IPV_LipUpper19",
                    "DHIhead:FACIAL_R_12IPV_LipUpper11","DHIhead:FACIAL_R_LipUpper2","DHIhead:FACIAL_R_12IPV_LipUpper10","DHIhead:FACIAL_R_12IPV_LipUpper3","DHIhead:FACIAL_C_LipUpper2","DHIhead:FACIAL_L_12IPV_LipUpper3","DHIhead:FACIAL_L_12IPV_LipUpper10","DHIhead:FACIAL_L_LipUpper2","DHIhead:FACIAL_L_12IPV_LipUpper11","DHIhead:FACIAL_L_12IPV_LipUpper19","DHIhead:FACIAL_L_LipUpperOuter2","DHIhead:FACIAL_L_12IPV_LipUpper20"),

'FACIAL_C_LipUpper1':("DHIhead:FACIAL_R_12IPV_LipUpper18","DHIhead:FACIAL_R_LipUpperOuter1","DHIhead:FACIAL_R_12IPV_LipUpper17",
                    "DHIhead:FACIAL_R_12IPV_LipUpper9","DHIhead:FACIAL_R_LipUpper1","DHIhead:FACIAL_R_12IPV_LipUpper7","DHIhead:FACIAL_R_12IPV_LipUpper2","DHIhead:FACIAL_C_LipUpper1","DHIhead:FACIAL_L_12IPV_LipUpper2","DHIhead:FACIAL_L_12IPV_LipUpper7","DHIhead:FACIAL_L_LipUpper1","DHIhead:FACIAL_L_12IPV_LipUpper9","DHIhead:FACIAL_L_12IPV_LipUpper17","DHIhead:FACIAL_L_LipUpperOuter1","DHIhead:FACIAL_L_12IPV_LipUpper18"),

'FACIAL_R_12IPV_LipUpper1':("DHIhead:FACIAL_R_12IPV_LipUpper16","DHIhead:FACIAL_R_12IPV_LipUpper8",
                          "DHIhead:FACIAL_R_12IPV_LipUpper6","DHIhead:FACIAL_R_12IPV_LipUpper1","DHIhead:FACIAL_L_12IPV_LipUpper1","DHIhead:FACIAL_L_12IPV_LipUpper6","DHIhead:FACIAL_L_12IPV_LipUpper8","DHIhead:FACIAL_L_12IPV_LipUpper16"),

'FACIAL_R_12IPV_LipLower1':("DHIhead:FACIAL_R_12IPV_LipLower16","DHIhead:FACIAL_R_12IPV_LipLower8",
                          "DHIhead:FACIAL_R_12IPV_LipLower6","DHIhead:FACIAL_R_12IPV_LipLower1","DHIhead:FACIAL_L_12IPV_LipLower1","DHIhead:FACIAL_L_12IPV_LipLower6","DHIhead:FACIAL_L_12IPV_LipLower8","DHIhead:FACIAL_L_12IPV_LipLower16"),

'FACIAL_R_12IPV_LipLower5':("DHIhead:FACIAL_R_12IPV_LipLower24","DHIhead:FACIAL_R_12IPV_LipLower22",
                          "DHIhead:FACIAL_R_12IPV_LipLower15","DHIhead:FACIAL_R_12IPV_LipLower13","DHIhead:FACIAL_R_12IPV_LipLower5","DHIhead:FACIAL_L_12IPV_LipLower5","DHIhead:FACIAL_L_12IPV_LipLower13","DHIhead:FACIAL_L_12IPV_LipLower15","DHIhead:FACIAL_L_12IPV_LipLower22","DHIhead:FACIAL_L_12IPV_LipLower24"),

'FACIAL_C_LipLower3':("DHIhead:FACIAL_R_12IPV_LipLower23","DHIhead:FACIAL_R_LipLowerOuter3","DHIhead:FACIAL_R_12IPV_LipLower21",
                    "DHIhead:FACIAL_R_12IPV_LipLower14","DHIhead:FACIAL_R_LipLower3","DHIhead:FACIAL_R_12IPV_LipLower12","DHIhead:FACIAL_R_12IPV_LipLower4","DHIhead:FACIAL_C_LipLower3","DHIhead:FACIAL_L_12IPV_LipLower4","DHIhead:FACIAL_L_12IPV_LipLower12","DHIhead:FACIAL_L_LipLower3","DHIhead:FACIAL_L_12IPV_LipLower14","DHIhead:FACIAL_L_12IPV_LipLower21","DHIhead:FACIAL_L_LipLowerOuter3","DHIhead:FACIAL_L_12IPV_LipLower23"),

'FACIAL_C_LipLower1':("DHIhead:FACIAL_R_12IPV_LipLower18","DHIhead:FACIAL_R_LipLowerOuter1","DHIhead:FACIAL_R_12IPV_LipLower17",
                    "DHIhead:FACIAL_R_12IPV_LipLower9","DHIhead:FACIAL_R_LipLower1","DHIhead:FACIAL_R_12IPV_LipLower7","DHIhead:FACIAL_R_12IPV_LipLower2","DHIhead:FACIAL_C_LipLower1","DHIhead:FACIAL_L_12IPV_LipLower2","DHIhead:FACIAL_L_12IPV_LipLower7","DHIhead:FACIAL_L_LipLower1","DHIhead:FACIAL_L_12IPV_LipLower9","DHIhead:FACIAL_L_12IPV_LipLower17","DHIhead:FACIAL_L_LipLowerOuter1","DHIhead:FACIAL_L_12IPV_LipLower18"),

'FACIAL_C_LipLower2':("DHIhead:FACIAL_R_12IPV_LipLower20","DHIhead:FACIAL_R_LipLowerOuter2","DHIhead:FACIAL_R_12IPV_LipLower19",
                    "DHIhead:FACIAL_R_12IPV_LipLower11","DHIhead:FACIAL_R_LipLower2","DHIhead:FACIAL_R_12IPV_LipLower10","DHIhead:FACIAL_R_12IPV_LipLower3","DHIhead:FACIAL_C_LipLower2","DHIhead:FACIAL_L_12IPV_LipLower3","DHIhead:FACIAL_L_12IPV_LipLower10","DHIhead:FACIAL_L_LipLower2","DHIhead:FACIAL_L_12IPV_LipLower11","DHIhead:FACIAL_L_12IPV_LipLower19","DHIhead:FACIAL_L_LipLowerOuter2","DHIhead:FACIAL_L_12IPV_LipLower20"),

'FACIAL_L_ForeheadInA1':("DHIhead:FACIAL_L_ForeheadInA3","DHIhead:FACIAL_L_ForeheadInA2","DHIhead:FACIAL_L_ForeheadInB2",
                       "DHIhead:FACIAL_L_ForeheadMid2","DHIhead:FACIAL_L_ForeheadOutA2","DHIhead:FACIAL_L_ForeheadOutB2","DHIhead:FACIAL_L_ForeheadOutB1","DHIhead:FACIAL_L_ForeheadOutA1","DHIhead:FACIAL_L_ForeheadMid1","DHIhead:FACIAL_L_ForeheadInB1","DHIhead:FACIAL_L_ForeheadInA1"),

'FACIAL_R_ForeheadInA1':("DHIhead:FACIAL_R_ForeheadInA3","DHIhead:FACIAL_R_ForeheadInA2","DHIhead:FACIAL_R_ForeheadInB2",
                       "DHIhead:FACIAL_R_ForeheadMid2","DHIhead:FACIAL_R_ForeheadOutA2","DHIhead:FACIAL_R_ForeheadOutB2","DHIhead:FACIAL_R_ForeheadOutB1","DHIhead:FACIAL_R_ForeheadOutA1","DHIhead:FACIAL_R_ForeheadMid1","DHIhead:FACIAL_R_ForeheadInB1","DHIhead:FACIAL_R_ForeheadInA1"),

'FACIAL_R_12IPV_ForeheadIn1':("DHIhead:FACIAL_R_12IPV_ForeheadOut27","DHIhead:FACIAL_R_12IPV_ForeheadOut23",
                            "DHIhead:FACIAL_R_12IPV_ForeheadMid19","DHIhead:FACIAL_R_12IPV_ForeheadMid15","DHIhead:FACIAL_R_12IPV_ForeheadIn9","DHIhead:FACIAL_R_12IPV_ForeheadIn5","DHIhead:FACIAL_R_12IPV_ForeheadIn1","DHIhead:FACIAL_R_12IPV_ForeheadIn2","DHIhead:FACIAL_R_12IPV_ForeheadIn6","DHIhead:FACIAL_R_12IPV_ForeheadIn10","DHIhead:FACIAL_R_12IPV_ForeheadMid16","DHIhead:FACIAL_R_12IPV_ForeheadMid20","DHIhead:FACIAL_R_12IPV_ForeheadOut24","DHIhead:FACIAL_R_12IPV_ForeheadOut28","DHIhead:FACIAL_R_12IPV_ForeheadOut31","DHIhead:FACIAL_R_12IPV_ForeheadOut29","DHIhead:FACIAL_R_12IPV_ForeheadOut25","DHIhead:FACIAL_R_12IPV_ForeheadMid21","DHIhead:FACIAL_R_12IPV_ForeheadMid17","DHIhead:FACIAL_R_12IPV_ForeheadIn11","DHIhead:FACIAL_R_12IPV_ForeheadIn7","DHIhead:FACIAL_R_12IPV_ForeheadIn3","DHIhead:FACIAL_R_12IPV_ForeheadIn4","DHIhead:FACIAL_R_12IPV_ForeheadIn8","DHIhead:FACIAL_R_12IPV_ForeheadIn12","DHIhead:FACIAL_R_12IPV_ForeheadMid18","DHIhead:FACIAL_R_12IPV_ForeheadMid22","DHIhead:FACIAL_R_12IPV_ForeheadOut26","DHIhead:FACIAL_R_12IPV_ForeheadOut30","DHIhead:FACIAL_R_12IPV_ForeheadOut32","DHIhead:FACIAL_R_12IPV_ForeheadIn14","DHIhead:FACIAL_R_12IPV_ForeheadIn13"),

'FACIAL_L_12IPV_ForeheadIn1':("DHIhead:FACIAL_L_12IPV_ForeheadOut27","DHIhead:FACIAL_L_12IPV_ForeheadOut23",
                            "DHIhead:FACIAL_L_12IPV_ForeheadMid19","DHIhead:FACIAL_L_12IPV_ForeheadMid15","DHIhead:FACIAL_L_12IPV_ForeheadIn9","DHIhead:FACIAL_L_12IPV_ForeheadIn5","DHIhead:FACIAL_L_12IPV_ForeheadIn1","DHIhead:FACIAL_L_12IPV_ForeheadIn2","DHIhead:FACIAL_L_12IPV_ForeheadIn6","DHIhead:FACIAL_L_12IPV_ForeheadIn10","DHIhead:FACIAL_L_12IPV_ForeheadMid16","DHIhead:FACIAL_L_12IPV_ForeheadMid20","DHIhead:FACIAL_L_12IPV_ForeheadOut24","DHIhead:FACIAL_L_12IPV_ForeheadOut28","DHIhead:FACIAL_L_12IPV_ForeheadOut31","DHIhead:FACIAL_L_12IPV_ForeheadOut29","DHIhead:FACIAL_L_12IPV_ForeheadOut25","DHIhead:FACIAL_L_12IPV_ForeheadMid21","DHIhead:FACIAL_L_12IPV_ForeheadMid17","DHIhead:FACIAL_L_12IPV_ForeheadIn11","DHIhead:FACIAL_L_12IPV_ForeheadIn7","DHIhead:FACIAL_L_12IPV_ForeheadIn3","DHIhead:FACIAL_L_12IPV_ForeheadIn4","DHIhead:FACIAL_L_12IPV_ForeheadIn8","DHIhead:FACIAL_L_12IPV_ForeheadIn12","DHIhead:FACIAL_L_12IPV_ForeheadMid18","DHIhead:FACIAL_L_12IPV_ForeheadMid22","DHIhead:FACIAL_L_12IPV_ForeheadOut26","DHIhead:FACIAL_L_12IPV_ForeheadOut30","DHIhead:FACIAL_L_12IPV_ForeheadOut32","DHIhead:FACIAL_L_12IPV_ForeheadIn14","DHIhead:FACIAL_L_12IPV_ForeheadIn13"),

'FACIAL_C_Forehead2':("DHIhead:FACIAL_R_Forehead1","DHIhead:FACIAL_C_Forehead1","DHIhead:FACIAL_L_Forehead1",
                    "DHIhead:FACIAL_L_Forehead2","DHIhead:FACIAL_C_Forehead2","DHIhead:FACIAL_R_Forehead2","DHIhead:FACIAL_R_Forehead3","DHIhead:FACIAL_C_Forehead3","DHIhead:FACIAL_L_Forehead3"),

'FACIAL_C_12IPV_Forehead1':("DHIhead:FACIAL_R_12IPV_Forehead1","DHIhead:FACIAL_C_12IPV_Forehead1",
                          "DHIhead:FACIAL_L_12IPV_Forehead1","DHIhead:FACIAL_L_12IPV_Forehead2","DHIhead:FACIAL_C_12IPV_Forehead2","DHIhead:FACIAL_R_12IPV_Forehead2","DHIhead:FACIAL_R_12IPV_Forehead3","DHIhead:FACIAL_C_12IPV_Forehead3","DHIhead:FACIAL_L_12IPV_Forehead3","DHIhead:FACIAL_L_12IPV_Forehead4","DHIhead:FACIAL_C_12IPV_Forehead4","DHIhead:FACIAL_R_12IPV_Forehead4","DHIhead:FACIAL_R_12IPV_Forehead5","DHIhead:FACIAL_C_12IPV_Forehead5","DHIhead:FACIAL_L_12IPV_Forehead5","DHIhead:FACIAL_L_12IPV_Forehead6","DHIhead:FACIAL_C_12IPV_Forehead6","DHIhead:FACIAL_R_12IPV_Forehead6"),
'FACIAL_L_LipCornerA1':("DHIhead:FACIAL_L_LipCorner1","DHIhead:FACIAL_L_LipCorner2","DHIhead:FACIAL_L_LipCorner3","DHIhead:FACIAL_L_12IPV_LipCorner1","DHIhead:FACIAL_L_12IPV_LipCorner2","DHIhead:FACIAL_L_12IPV_LipCorner3"),
'FACIAL_R_LipCornerA1':("DHIhead:FACIAL_R_LipCorner1","DHIhead:FACIAL_R_LipCorner2","DHIhead:FACIAL_R_LipCorner3","DHIhead:FACIAL_R_12IPV_LipCorner1","DHIhead:FACIAL_R_12IPV_LipCorner2","DHIhead:FACIAL_R_12IPV_LipCorner3"),
'FACIAL_C_12IPV_NoseLA1':("DHIhead:FACIAL_L_NostrilThickness3","DHIhead:FACIAL_R_NostrilThickness3","DHIhead:FACIAL_C_12IPV_NoseL1","DHIhead:FACIAL_C_12IPV_NoseL2")
}

def locatorCurvePos(curveShapeName,locList):
    numi=0
    for i in locList:
        MTM=None
        DCP=None
        checkI=False
        if pm.objExists(i+'_MTM')==False:
            MTM=pm.createNode('multMatrix',n=i+'_MTM')
        else:
            MTM=pm.PyNode(i+'_MTM')
            checkI=True
        if pm.objExists(i+'_DCP')==False:    
            DCP=pm.createNode('decomposeMatrix',n=i+'_DCP')
        else:
            DCP=pm.PyNode(i+'_DCP')
            checkI=True
        if checkI==True:
            pass
        else:    
            pm.PyNode(i).worldMatrix[0] >> MTM.matrixIn[0]
            pm.PyNode(i).parentInverseMatrix[0] >> MTM.matrixIn[1]
            MTM.matrixSum >>DCP.inputMatrix
        DCP.outputTranslate >> pm.PyNode(curveShapeName+'.controlPoints[%d]'%numi)
        numi=numi+1
def curveA(stringA,colorA=[0,0,0],sizeA=1.0):
    if pm.objExists('customGuideCurve')==False:
        pm.createNode('transform',n='customGuideCurve')
    if pm.objExists('custom_Curve_Grp')==False:
        pm.createNode('transform',n='custom_Curve_Grp')
        pm.parent('custom_Curve_Grp','customGuideCurve')
    if pm.objExists('custom_Brush_Grp')==False:
        pm.createNode('transform',n='custom_Brush_Grp')
        pm.parent('custom_Brush_Grp','customGuideCurve')        
    if pm.objExists('custom_Locator_Grp')==False:
        pm.createNode('transform',n='custom_Locator_Grp')
        pm.parent('custom_Locator_Grp','customGuideCurve')         
    if pm.objExists(stringA)==False:
        p=[]
        locatorList=[]  
        listA=customcurvelist[stringA]  
        for i in listA:
            pm.PyNode(i).v.set(0)
            pos=pm.PyNode(i).getTranslation(space='world')
            p.append( pos )
            if pm.objExists(i+'_LOCShape')==False:
                locA=pm.createNode('locator',n=i+'_LOCShape')
                locB=locA.getParent()
                locB.t.set( pos )
                locB.rename(i+'_LOC')
                locB.v.set(0)
                pm.parent(locB,'custom_Locator_Grp')
            locatorList.append(i+'_LOC')  
        selectA=pm.curve(n=stringA,d=1,p=p) 
        shapeA =  selectA.getChildren(s=1)          
        locatorCurvePos(shapeA[0],locatorList)

        pm.parent(selectA,'custom_Curve_Grp')  
    if pm.objExists(stringA+'_stroke')==False:        
        pm.select(selectA)
        pm.mel.eval('AttachBrushToCurves;')
    curveNmae=stringA
    shpaeA=pm.PyNode(curveNmae).getChildren(s=1)
    strokeA=pm.listConnections(shpaeA[0]+'.worldSpace')
    strokeA[0].rename(curveNmae+'_stroke')
    strokeShapeA=pm.PyNode(strokeA[0]).getChildren(s=1)
    brushA=pm.listConnections(strokeShapeA[0]+'.brush')
    brushA[0].rename(curveNmae+'_brush')
    if pm.PyNode(curveNmae+'_stroke').getParent()!='custom_Brush_Grp':
        pm.parent(curveNmae+'_stroke','custom_Brush_Grp')
    strokeShapeA[0].pressureScale[0].pressureScale_FloatValue.set(sizeA)
    strokeShapeA[0].smoothing.set(0.1)
    brushA[0].color1.set(colorA)
    
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
    
titleA=u'UE_MH_DNA_NeutralJoint_Custom_UI_V20230331'
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
        action4 = QAction("open folder " , self.textedit_dnaPath)        
        
        action1.triggered.connect(self.textedit_dnaPath_action1_run)
        action2.triggered.connect(self.textedit_dnaPath_action2_run)
        action3.triggered.connect(self.textedit_dnaPath_action3_run)                
        action4.triggered.connect(self.textedit_dnaPath_action4_run)                        
        
        self.textedit_dnaPath.addAction(action1)
        self.textedit_dnaPath.addAction(action2)
        self.textedit_dnaPath.addAction(action3)
        self.textedit_dnaPath.addAction(action4)        
        
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
        
        self.groupbox_a = QGroupBox('curve')
        self.groupbox_a.setCheckable(True)  
        self.groupbox_a.setChecked(False)

        self.groupboxLayout=QVBoxLayout()
        self.groupbox_a.setLayout( self.groupboxLayout )
        self.groupbox_createCurve_btn = QPushButton("create neutral joint curve")
        self.groupbox_locShow_btn = QPushButton("select curve locator visibility show")
        self.groupbox_locHide_btn = QPushButton("select curve locator visibility hide")
        self.groupbox_setTableWidget_btn = QPushButton("curve To TableWeight Neutral Joint V")        
        self.groupbox_a.clicked.connect(self.test)
        self.groupbox_createCurve_btn.clicked.connect(self.groupbox_createCurve_run)        
        self.groupbox_locShow_btn.clicked.connect(self.groupbox_locShow_run)        
        self.groupbox_locHide_btn.clicked.connect(self.groupbox_locHide_run)                        
        self.groupbox_setTableWidget_btn.clicked.connect(self.groupbox_setTableWidget_run)        
        self.test()
        self.groupboxLayout.addWidget(self.groupbox_createCurve_btn)
        self.groupboxLayout.addWidget(self.groupbox_locShow_btn)
        self.groupboxLayout.addWidget(self.groupbox_locHide_btn)
        self.groupboxLayout.addWidget(self.groupbox_setTableWidget_btn)
        
        
        self.allQVBoxLayout.addWidget(self.table_cMHdnaLoad_btn)
        self.allQVBoxLayout.addWidget(self.table_cRjntLoad_btn)
        self.allQVBoxLayout.addWidget(self.table_import_json_btn)
        self.allQVBoxLayout.addWidget(self.table_import_dna_btn)        
        self.allQVBoxLayout.addWidget(self.textedit_dnaPath)
        
        self.allQVBoxLayout.addWidget(self.table)
        
        self.allQVBoxLayout.addWidget(self.dna_export_json_btn)
        self.allQVBoxLayout.addWidget(self.table_export_json_btn)

        self.allQVBoxLayout.addWidget(self.table_save_json_btn)

        self.allQVBoxLayout.addWidget(self.groupbox_a)
                
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
    def groupbox_createCurve_run(self):
        num=100/len(dic_Curve)
        printNum=0
        create_progressBar_Win('create_progressBar_Curve')         
        for i in dic_Curve:
            list=dic_Curve[i]
            curveA(i,[list[0],list[1],list[2]],list[3]) 
            printNum=printNum+num
            update_progress_bar(printNum)
        delete_progressBar_Win()              

        
    def groupbox_locShow_run(self):
        selObj=pm.ls(sl=1)
        if selObj:
            for i in  customcurvelist[ (selObj[0].getName().replace('_stroke','') )]:
                pm.PyNode(i+'_LOC').v.set(1)
    def groupbox_locHide_run(self):
        if pm.objExists('custom_Locator_Grp'):
            for i in pm.PyNode('custom_Locator_Grp').getChildren():
                i.v.set(0)  
    def test(self):  
        checkA=self.groupbox_a.isChecked()
        self.groupbox_createCurve_btn.setVisible(checkA)
        self.groupbox_locShow_btn.setVisible(checkA)
        self.groupbox_locHide_btn.setVisible(checkA)
        self.groupbox_setTableWidget_btn.setVisible(checkA)        
    def groupbox_setTableWidget_run(self):
        # progressBar 시작 
        create_progressBar_Win('...ing 80% wait 1 minute')
        
        # 현재 dna 경로 가져오고
        update_progress_bar( 1 )  
        
        getPath_dna=pm.ls(type='embeddedNodeRL4')
        binaryFilePath=getPath_dna[0].dnaFilePath.get()              
        # 그 dna를 현재 시간으로 복사하고
        update_progress_bar( 10 )        
                
        now = datetime.datetime.now()
        time_str=now.strftime("%y%m%d%H%M")
        crc_path=binaryFilePath
        dst_path=''

        if binaryFilePath.find('_rl.dna') != -1:
            dst_path=binaryFilePath.replace('_rl.dna',time_str+'.dna')
            crc_path=binaryFilePath.replace('_rl.dna','.dna')
        else:    
            num = binaryFilePath.find('.dna')           
            print (binaryFilePath[num-10:num])   
            if binaryFilePath[num-10]=="2":
                dst_path = binaryFilePath[:num-10]+time_str+'.dna'
            else:    
                dst_path=binaryFilePath.replace('.dna',time_str+'.dna')
        shutil.copy(crc_path, dst_path)
        
        
        # 그걸 임포트해서 테이블에 세팅을 하고 
        update_progress_bar( 20 )                        
        
        self.table.clear()
        self.table.setHorizontalHeaderLabels(["Name" ,"Tx" , "Ty", "Tz", "Rx", "Ry", "Rz" ])
        #files, _ = QFileDialog.getOpenFileNames(self,"getdna", "","All Files (*);;DNA Files (*.dna)", options=QFileDialog.DontUseNativeDialog)
        files=dst_path
        if files:
            binaryFilePathA=files[0]
            readStream = dna.FileStream(files, dna.FileStream.AccessMode_Read , dna.FileStream.OpenMode_Binary)
            self.reader = dna.BinaryStreamReader(readStream)
            self.reader.read()        
            self.textedit_dnaPath.setText(dst_path)
            self.table_setRowCount( )
            self.table_setItem_name( )
            self.table_setTranslate( )
            self.table_setRotate( )
            
                   
        # 현재 커브 위치를 테이블에 적용하고
        update_progress_bar( 20 )     
        
        deleteA=pm.duplicate('DHIhead:spine_04')
        pm.select( clear=True )
        count=self.table.rowCount() 
        for i in range(1,count):
            stringA=(self.table.item(i, 0).text())
            if pm.objExists('DHIhead:'+stringA+'_LOC'):
                jointA=pm.ls(stringA,type='joint')
                pm.pointConstraint('DHIhead:'+stringA+'_LOC',jointA,mo=0)
        update_progress_bar( 30 )                 
        for i in range(1,count):
            stringA=(self.table.item(i, 0).text())
            if pm.objExists('DHIhead:'+stringA+'_LOC'):
                jointA=pm.ls(stringA,type='joint')
                posT=pm.PyNode(jointA[0]+'.t').get() 
                itemA = QTableWidgetItem('%0.3f'%(posT[0]))
                itemB = QTableWidgetItem('%0.3f'%(posT[1]))
                itemC = QTableWidgetItem('%0.3f'%(posT[2]))
                self.table.setItem(i,1,itemA)
                self.table.setItem(i,2,itemB)
                self.table.setItem(i,3,itemC)  
        update_progress_bar( 40 )                              
        pm.delete(deleteA)                   
        # 테이블 위젯을 dna에 적용
        update_progress_bar( 50 )   
        fileName = self.textedit_dnaPath.text()  
        #fileName, _ = QFileDialog.getSaveFileName(self,"QFileDialog.getSaveFileName()","%s"%pathA.rsplit('/',1)[0],"DNA Files (*.dna)", options=QFileDialog.DontUseNativeDialog)
        if fileName:        
            stream = dna.FileStream(fileName, dna.FileStream.AccessMode_Write, dna.FileStream.OpenMode_Binary)
            self.writer = dna.BinaryStreamWriter(stream)
            readStream = dna.FileStream(fileName, dna.FileStream.AccessMode_Read , dna.FileStream.OpenMode_Binary)
            self.reader = dna.BinaryStreamReader(readStream)
            self.reader.read()   
            self.writer.setFrom(self.reader)
            #for i in dir(writer):
            #    print(i)
            count=self.table.rowCount() 
            setT=[]  
            update_progress_bar( 60 ) 
            for i in range(0,count):
                setT.append( [ float(self.table.item(i, 1).text()) , float(self.table.item(i, 2).text()) , float(self.table.item(i, 3).text()) ] )
                #setT.append( [ 0.0, 0.0, 0.0 ] )
            # Creates the DNA
            update_progress_bar( 70 )            
            self.writer.setNeutralJointTranslations(setT)
            update_progress_bar( 80 )                        
            self.writer.write()                    
            update_progress_bar( 90 )            
            print (fileName)           
        # 수정된 커브 dna를 캐릭터에 적용 끝
        update_progress_bar( 99 ) 
        self.textedit_dnaPath_action1_run()
        delete_progressBar_Win()  
    def textedit_dnaPath_action4_run(self):
        fileName = self.textedit_dnaPath.text()  
        folder_path = os.path.dirname(fileName)  
        if os.path.exists(folder_path): # 폴더가 존재하는지 체크
            os.startfile(folder_path)
            #os.startfile("C:/Users/vive/Documents/Megascans Library/Downloaded/DHI/fskikIND_asset/8k/asset_source/MetaHumans/Ada/SourceAssets")
            #subprocess.Popen('explorer "{}"'.format(folder_path))
            #subprocess.Popen('explorer "{C:/Users/vive/Documents/Megascans Library/Downloaded/DHI/fskikIND_asset/8k/asset_source/MetaHumans/Ada/SourceAssets"}"' )
            print (folder_path)
        else:
            print("폴더가 존재하지 않습니다.")                 
if cmds.window(u"UE_MH_DNA_Custom_UI_V20230227", q=True, ex=True):
    cmds.deleteUI(u"UE_MH_DNA_Custom_UI_V20230227", window=True)
if cmds.window(u"UE_MH_DNA_Custom_UI_V20230227", q=True, ex=True):
    cmds.deleteUI(u"UE_MH_DNA_Custom_UI_V20230227", window=True)
UE_MH_RDNA_UI().show()


import maya.cmds as cmds
#프로그래바 생성 부분 
def create_progressBar_Win(titleString):
    delete_progressBar_Win()    
    progress_window = cmds.window(u'Run_DNA_calibration',title=titleString,widthHeight=[300,10])
    cmds.columnLayout()
    progress_control = cmds.progressBar(u'Run_DNA_calibration_progressBar',maxValue=100, width=300)
    cmds.showWindow(progress_window)
# 프로그래스바 업데이트 함수
def update_progress_bar(value):
    cmds.progressBar('Run_DNA_calibration_progressBar', edit=True, progress=value)
#프로그래바 삭제 부분 
def delete_progressBar_Win():
    if cmds.window(u'Run_DNA_calibration', q=True, ex=True):
        cmds.deleteUI(u'Run_DNA_calibration', window=True)
# 예시 사용
create_progressBar_Win('create_progressBar_Win')
for i in range(100):
    update_progress_bar(i)
delete_progressBar_Win()   
#update_progress_bar(40)
