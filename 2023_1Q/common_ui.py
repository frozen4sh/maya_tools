#-*- coding:utf-8 -*-

import pymel.core as pm
import maya.cmds as cmds
import maya.cmds as mc
import math
import os,sys
import json

import importlib
from PySide2 import QtCore,QtGui,QtWidgets,__version__
from maya.app.general import mayaMixin
from collections import OrderedDict

titleA='sequence_run_script_UI_v20210503'
class sequence_run_script_UI(mayaMixin.MayaQWidgetBaseMixin,QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(sequence_run_script_UI, self).__init__(parent)
        if pm.window(u'sequence_run_script_UI_01', q=True, ex=True):
            pm.deleteUI(u'sequence_run_script_UI_01', window=True)
        self.setObjectName('sequence_run_script_UI_01')
        self.setWindowTitle(titleA)
        self.setGeometry(500, 200, 350, 750)
        self.Log()
        self.UI()
sequence_run_script_UI().show()