import sys
sys.path.insert(0,'FK_Controller_Tool_ui.py')


from importlib import reload

import MayaUITemplate

reload(MayaUITemplate)
MayaUITemplate.openWindow()