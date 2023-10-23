import pymel.core as pm
# base group 
# Null Grpup 3  mod jnt etc
All_Grp='All_Grp'
mod_Grp='mod_Grp'
jnt_Grp='jnt_Grp'
etc_Grp='etc_Grp'
parentDic={'All_Grp':None,'mod_Grp':'All_Grp','jnt_Grp':'All_Grp','etc_Grp':'All_Grp'}
colorDic={'All_Grp':(1.0, 0.3955000042915344, 0.3725000023841858),
        'mod_Grp':(1.0, 0.6503000259399414, 0.3725000023841858),
        'jnt_Grp':(0.5034000873565674, 1.0, 0.3725000023841858),
        'etc_Grp':(0.3725000023841858, 0.6746000647544861, 1.0)}
NullGrpList=[All_Grp,mod_Grp,jnt_Grp,etc_Grp]

for nullGrp in NullGrpList:
    if pm.objExists(nullGrp)!=True:
        newNode=pm.createNode('transform',n=nullGrp)
        newNode.useOutlinerColor.set(1)
    if parentDic[nullGrp]!=None:
       pm.parent(nullGrp,parentDic[nullGrp])
    if colorDic[nullGrp]!=None:
        pm.PyNode(nullGrp+'.outlinerColor').set( colorDic[nullGrp])
        pm.select(nullGrp)
        pm.select(cl=1)
