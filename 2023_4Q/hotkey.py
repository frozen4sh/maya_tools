# Reset_T alt shift w


import maya.cmds as cmds 
objs = cmds.ls(sl= True) 
axis = ['X','Y','Z'] 
for obj in objs: 
    for i,j in enumerate(axis): 
        if not cmds.getAttr('{0}.translate{1}'.format(obj, j), lock= True): 
            if cmds.getAttr('{0}.translate{1}'.format(obj, j), keyable= True): 
                cmds.setAttr('{0}.translate{1}'.format(obj, j), 0) 



# Reset_T alt shift e

import maya.cmds as cmds 
objs = cmds.ls(sl= True) 
axis = ['X','Y','Z'] 
for obj in objs: 
    for i,j in enumerate(axis): 
        if not cmds.getAttr('{0}.rotate{1}'.format(obj, j), lock= True): 
            if cmds.getAttr('{0}.rotate{1}'.format(obj, j), keyable= True): 
                cmds.setAttr('{0}.rotate{1}'.format(obj, j), 0) 


# Reset_T alt shift r

import maya.cmds as cmds 
objs = cmds.ls(sl= True) 
axis = ['X','Y','Z'] 
for obj in objs: 
    for i,j in enumerate(axis): 
        if not cmds.getAttr('{0}.scale{1}'.format(obj, j), lock= True): 
            if cmds.getAttr('{0}.scale{1}'.format(obj, j), keyable= True): 
                cmds.setAttr('{0}.scale{1}'.format(obj, j), 1) 


# ctrl v
# timeSliderPasteKey false;
# ctrl c
# timeSliderCopyKey;

#{  string $currentPanel = `getPanel -withFocus`;   int $match = `gmatch $currentPanel "modelPanel*"`;   if($match == 1) {    string $state = `isolateSelect -q -state $currentPanel`;    if ($state)      enableIsolateSelect $currentPanel false;    else      enableIsolateSelect $currentPanel true;  }}