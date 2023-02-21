#-*- coding:utf-8 -*-
from maya import cmds
import pymel.core as pm
import maya.api.OpenMaya as om
#print 'a'
#내가 필요한 폴리곤 ?? 수정된 폴리곤 Retaget polygon 
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
# 원본이름  
#=============================================
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
# 1차 공정  더미 조인트 를  수정된 폴리곤에 맞춰  조인트 이동
pm.select( clear=True )
# 이동될 조인트 생성 ( 네임스페이스만 없어짐 )
pm.duplicate('DHIhead:spine_04')
pm.select( clear=True )
# 폴리 버텍스 갯수가 몇개인지 체크 
# def 리스트와 폴리곤 이름을 넘기면 조인트 위치변경 ??   # 폴리곤 이름 과 조인트 넘길때 버텍스 숫자 다시 새야함
locator_retaget_list=[]
pm.select('spine_05',hi=1)
for i in pm.ls(sl=1,type='joint'):
    locatorShape=pm.createNode('locator',n='retaget_'+i+'Shape')
    locator_=locatorShape.getParent()
    locator_retaget_list.append(locator_)
    da=pm.pointConstraint(i,locator_,mo=0)
    pm.delete(da)
pm.select(cl=1)
# 로케이터는 만들었고 ProximityPin 메쉬 생성 
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
"""
posT = pm.PyNode('DHIhead:FACIAL_C_Neck1Root').getTranslation(space='world')
pm.PyNode('retaget_FACIAL_C_Neck1Root').setTranslation(posT,space='world')

posT = pm.PyNode('DHIhead:neck_01').getTranslation(space='world')
pm.PyNode('retaget_neck_01').setTranslation(posT,space='world')

posT = pm.PyNode('DHIhead:neck_02').getTranslation(space='world')
pm.PyNode('retaget_neck_02').setTranslation(posT,space='world')

posT = pm.PyNode('DHIhead:FACIAL_C_Neck2Root').getTranslation(space='world')
pm.PyNode('retaget_FACIAL_C_Neck2Root').setTranslation(posT,space='world')

posT = pm.PyNode('DHIhead:head').getTranslation(space='world')
pm.PyNode('retaget_head').setTranslation(posT,space='world')


posT = pm.PyNode('DHIhead:FACIAL_C_FacialRoot').getTranslation(space='world')
pm.PyNode('retaget_FACIAL_C_FacialRoot').setTranslation(posT,space='world')
"""

listA='FACIAL_C_Neck1Root','neck_01','neck_02','FACIAL_C_Neck2Root','head','FACIAL_C_FacialRoot','spine_05','clavicle_r','upperarm_r','upperarm_correctiveRoot_r','upperarm_bck_r','upperarm_fwd_r','upperarm_out_r','upperarm_in_r','clavicle_out_r','clavicle_scap_r','clavicle_l','upperarm_l','upperarm_correctiveRoot_l','upperarm_bck_l','upperarm_fwd_l','upperarm_out_l','upperarm_in_l','clavicle_out_l','clavicle_scap_l','clavicle_pec_l','clavicle_pec_r','spine_04_latissimus_r','spine_04_latissimus_l'

for i in listA:
    posT = pm.PyNode('DHIhead:'+i).getTranslation(space='world')
    pm.PyNode('retaget_'+i).setTranslation(posT,space='world')
    
    
pm.delete(deleteConstraintList)
pm.delete(head_ProximityPin,teeth_ProximityPin,eyeLeft_ProximityPin,eyeRight_ProximityPin)
pm.delete(locator_retaget_list)
pm.delete( pm.ls('pinInput*' ,type='transform'))
# 언리얼 엔진  노드 이름변경 
rigLogicNode=pm.ls(type='embeddedNodeRL4')[0]
rigLogicNode.rename('rigLogicNode')

"""
# 조인트 배치 끝 
def move_constraint():
    #move neck_01 parent bone
    cmds.select('DHIhead:neck_01')
    neck_01DHIB = cmds.ls( selection=True )
    cmds.select('neck_01')
    neck_01B = cmds.ls( selection=True )

    neck_01B_XF = cmds.xform(neck_01B,q=1,ws=1,t=1)
    cmds.move( neck_01B_XF[0], neck_01B_XF[1], neck_01B_XF[2], neck_01DHIB, absolute=True, ws=True )

    #move FACIAL_C_Neck1Root parent bone
    cmds.select('DHIhead:FACIAL_C_Neck1Root')
    FACIAL_C_Neck1RootDHIB = cmds.ls( selection=True )
    cmds.select('FACIAL_C_Neck1Root')
    FACIAL_C_Neck1RootB = cmds.ls( selection=True )

    FACIAL_C_Neck1RootB_XF = cmds.xform(FACIAL_C_Neck1RootB,q=1,ws=1,t=1)
    cmds.move( FACIAL_C_Neck1RootB_XF[0], FACIAL_C_Neck1RootB_XF[1], FACIAL_C_Neck1RootB_XF[2], FACIAL_C_Neck1RootDHIB, absolute=True, ws=True )

    #move neck_02 parent bone
    cmds.select('DHIhead:neck_02')
    neck_02DHIB = cmds.ls( selection=True )
    cmds.select('neck_02')
    neck_02B = cmds.ls( selection=True )

    neck_02B_XF = cmds.xform(neck_02B,q=1,ws=1,t=1)
    cmds.move( neck_02B_XF[0], neck_02B_XF[1], neck_02B_XF[2], neck_02DHIB, absolute=True, ws=True )

    #move FACIAL_C_Neck2Root parent bone
    cmds.select('DHIhead:FACIAL_C_Neck2Root')
    FACIAL_C_Neck2RootDHIB = cmds.ls( selection=True )
    cmds.select('FACIAL_C_Neck2Root')
    FACIAL_C_Neck2RootB = cmds.ls( selection=True )

    FACIAL_C_Neck2RootB_XF = cmds.xform(FACIAL_C_Neck2RootB,q=1,ws=1,t=1)
    cmds.move( FACIAL_C_Neck2RootB_XF[0], FACIAL_C_Neck2RootB_XF[1], FACIAL_C_Neck2RootB_XF[2], FACIAL_C_Neck2RootDHIB, absolute=True, ws=True )


    #move head parent bone
    cmds.select('DHIhead:head')
    headDHIB = cmds.ls( selection=True )
    cmds.select('head')
    headB = cmds.ls( selection=True )

    headB_XF = cmds.xform(headB,q=1,ws=1,t=1)
    cmds.move( headB_XF[0], headB_XF[1], headB_XF[2], headDHIB, absolute=True, ws=True )

    #move FACIAL_C_FacialRoot parent bone
    cmds.select('DHIhead:FACIAL_C_FacialRoot')
    FACIAL_C_FacialRootDHIB = cmds.ls( selection=True )
    cmds.select('FACIAL_C_FacialRoot')
    FACIAL_C_FacialRootB = cmds.ls( selection=True )

    FACIAL_C_FacialRootB_XF = cmds.xform(FACIAL_C_FacialRootB,q=1,ws=1,t=1)
    cmds.move( FACIAL_C_FacialRootB_XF[0], FACIAL_C_FacialRootB_XF[1], FACIAL_C_FacialRootB_XF[2], FACIAL_C_FacialRootDHIB, absolute=True, ws=True )

move_constraint()
cmds.select( clear=True )


def rl4_node_op():

    #getting all bones connected to rl4 node
    rigBoneLists = []
    rigBones = []
    rigBoneStrippedList = []
    jto = 0
    while jto < 2563:
        jto_ID = 'rigLogicNode.jntTranslationOutputs[%s]'%jto
        rigBoneLists.append(cmds.connectionInfo( jto_ID, destinationFromSource = 1))
        rigBones.append(rigBoneLists[jto][0])
        rigBoneStripped = rigBones[jto][:-11]

        
        rigBoneStrippedList.append(rigBoneStripped)
        jto = jto+1
        


    ndBoneList = []
    for nd in rigBoneStrippedList:
        if nd not in ndBoneList:
            ndBoneList.append(nd)
            

    #get same duplicate bone
    dupNDBoneList = []
    offsetLIST = []

    preffix = "DHIhead:"

    ndBoneList_ID1 = 0
    while ndBoneList_ID1 < len(ndBoneList):
        dupBoneNameE = ndBoneList[ndBoneList_ID1]
        duplicateBoneName = dupBoneNameE[len(preffix):]
        dupNDBoneList.append(duplicateBoneName)
        
        #getting each of the two sets of bones
        OriginalBoneListID = ndBoneList[ndBoneList_ID1]
        DuplicateBoneListID = dupNDBoneList[ndBoneList_ID1]
        
        #getting translate value of Original Bone List with each ID
        TranslateX_OBLI = cmds.getAttr("%s.translateX" % OriginalBoneListID)
        TranslateY_OBLI = cmds.getAttr("%s.translateY" % OriginalBoneListID)
        TranslateZ_OBLI = cmds.getAttr("%s.translateZ" % OriginalBoneListID)
        
        #getting translate value of Duplicated Bone List with each ID
        TranslateX_DBLI = cmds.getAttr("%s.translateX" % DuplicateBoneListID)
        TranslateY_DBLI = cmds.getAttr("%s.translateY" % DuplicateBoneListID)
        TranslateZ_DBLI = cmds.getAttr("%s.translateZ" % DuplicateBoneListID)
        
        #calculating different between Duplicated bones and DHI	
        ADL_X = TranslateX_DBLI - TranslateX_OBLI
        ADL_Y = TranslateY_DBLI - TranslateY_OBLI
        ADL_Z = TranslateZ_DBLI - TranslateZ_OBLI
        
        
        offsetLIST.append(ADL_X)
        offsetLIST.append(ADL_Y)
        offsetLIST.append(ADL_Z)
        
        
        ndBoneList_ID1 = ndBoneList_ID1 + 1
        

    del offsetLIST[987]
    del offsetLIST[987]
    del offsetLIST[1951]
    del offsetLIST[1952]
    del offsetLIST[2390]


    #using ADL to RL4 Node


    bone_TransformID = 0
    while bone_TransformID < len(rigBones):
        bone_transform = rigBones[bone_TransformID]
        #Create Add Double Linear Node and connect them
        adlName = 'ADL_%s'%rigBones[bone_TransformID]
        adlName1 = adlName.replace(":","")
        adlName2 = adlName1.replace(".","_")
        
        #create ADL node
        cmds.createNode( 'addDoubleLinear', n=adlName2 )
        rlno = 'rigLogicNode.jntTranslationOutputs[%s]'%bone_TransformID
        adlNNI = '%s.input1'%adlName2
        
        #Connect ADL to RL4
        cmds.connectAttr(rlno, adlNNI)
        bo = rigBones[bone_TransformID]
        adlNNO = '%s.output'%adlName2
        
        #Connect ADL to Joint
        cmds.connectAttr(adlNNO, bo, force=1)
        pm.delete(deleteConstraintList)
pm.delete(head_ProximityPin,teeth_ProximityPin,eyeLeft_ProximityPin,eyeRight_ProximityPin)
pm.delete(locator_retaget_list)
pm.delete( pm.ls('pinInput*' ,type='transform'))
# 언리얼 엔진  노드 이름변경 
rigLogicNode=pm.ls(type='embeddedNodeRL4')[0]
rigLogicNode.rename('rigLogicNode')
"""
# 조인트 배치 끝 
def move_constraint():
    #move neck_01 parent bone
    cmds.select('DHIhead:neck_01')
    neck_01DHIB = cmds.ls( selection=True )
    cmds.select('neck_01')
    neck_01B = cmds.ls( selection=True )

    neck_01B_XF = cmds.xform(neck_01B,q=1,ws=1,t=1)
    cmds.move( neck_01B_XF[0], neck_01B_XF[1], neck_01B_XF[2], neck_01DHIB, absolute=True, ws=True )

    #move FACIAL_C_Neck1Root parent bone
    cmds.select('DHIhead:FACIAL_C_Neck1Root')
    FACIAL_C_Neck1RootDHIB = cmds.ls( selection=True )
    cmds.select('FACIAL_C_Neck1Root')
    FACIAL_C_Neck1RootB = cmds.ls( selection=True )

    FACIAL_C_Neck1RootB_XF = cmds.xform(FACIAL_C_Neck1RootB,q=1,ws=1,t=1)
    cmds.move( FACIAL_C_Neck1RootB_XF[0], FACIAL_C_Neck1RootB_XF[1], FACIAL_C_Neck1RootB_XF[2], FACIAL_C_Neck1RootDHIB, absolute=True, ws=True )

    #move neck_02 parent bone
    cmds.select('DHIhead:neck_02')
    neck_02DHIB = cmds.ls( selection=True )
    cmds.select('neck_02')
    neck_02B = cmds.ls( selection=True )

    neck_02B_XF = cmds.xform(neck_02B,q=1,ws=1,t=1)
    cmds.move( neck_02B_XF[0], neck_02B_XF[1], neck_02B_XF[2], neck_02DHIB, absolute=True, ws=True )

    #move FACIAL_C_Neck2Root parent bone
    cmds.select('DHIhead:FACIAL_C_Neck2Root')
    FACIAL_C_Neck2RootDHIB = cmds.ls( selection=True )
    cmds.select('FACIAL_C_Neck2Root')
    FACIAL_C_Neck2RootB = cmds.ls( selection=True )

    FACIAL_C_Neck2RootB_XF = cmds.xform(FACIAL_C_Neck2RootB,q=1,ws=1,t=1)
    cmds.move( FACIAL_C_Neck2RootB_XF[0], FACIAL_C_Neck2RootB_XF[1], FACIAL_C_Neck2RootB_XF[2], FACIAL_C_Neck2RootDHIB, absolute=True, ws=True )


    #move head parent bone
    cmds.select('DHIhead:head')
    headDHIB = cmds.ls( selection=True )
    cmds.select('head')
    headB = cmds.ls( selection=True )

    headB_XF = cmds.xform(headB,q=1,ws=1,t=1)
    cmds.move( headB_XF[0], headB_XF[1], headB_XF[2], headDHIB, absolute=True, ws=True )

    #move FACIAL_C_FacialRoot parent bone
    cmds.select('DHIhead:FACIAL_C_FacialRoot')
    FACIAL_C_FacialRootDHIB = cmds.ls( selection=True )
    cmds.select('FACIAL_C_FacialRoot')
    FACIAL_C_FacialRootB = cmds.ls( selection=True )

    FACIAL_C_FacialRootB_XF = cmds.xform(FACIAL_C_FacialRootB,q=1,ws=1,t=1)
    cmds.move( FACIAL_C_FacialRootB_XF[0], FACIAL_C_FacialRootB_XF[1], FACIAL_C_FacialRootB_XF[2], FACIAL_C_FacialRootDHIB, absolute=True, ws=True )

move_constraint()
cmds.select( clear=True )
#dir( pm.PyNode('rigLogicNode.jntTranslationOutputs').getNumElements())

def rl4_node_op():

    #getting all bones connected to rl4 node
    rigBoneLists = []
    rigBones = []
    rigBoneStrippedList = []
    jto = 0
    while jto < pm.PyNode('rigLogicNode.jntTranslationOutputs').getNumElements() :
        jto_ID = 'rigLogicNode.jntTranslationOutputs[%s]'%jto
        rigBoneLists.append(cmds.connectionInfo( jto_ID, destinationFromSource = 1))
        rigBones.append(rigBoneLists[jto][0])
        rigBoneStripped = rigBones[jto][:-11]

        
        rigBoneStrippedList.append(rigBoneStripped)
        jto = jto+1
        


    ndBoneList = []
    for nd in rigBoneStrippedList:
        if nd not in ndBoneList:
            ndBoneList.append(nd)
            

    #get same duplicate bone
    dupNDBoneList = []
    offsetLIST = []

    preffix = "DHIhead:"

    ndBoneList_ID1 = 0
    while ndBoneList_ID1 < len(ndBoneList):
        dupBoneNameE = ndBoneList[ndBoneList_ID1]
        duplicateBoneName = dupBoneNameE[len(preffix):]
        dupNDBoneList.append(duplicateBoneName)
        #getting each of the two sets of bones
        OriginalBoneListID = ndBoneList[ndBoneList_ID1]
        DuplicateBoneListID = dupNDBoneList[ndBoneList_ID1]
        if cmds.objExists( "%s.translateX" % OriginalBoneListID ):

            #getting translate value of Original Bone List with each ID
            TranslateX_OBLI = cmds.getAttr("%s.translateX" % OriginalBoneListID)
            TranslateY_OBLI = cmds.getAttr("%s.translateY" % OriginalBoneListID)
            TranslateZ_OBLI = cmds.getAttr("%s.translateZ" % OriginalBoneListID)
            #getting translate value of Duplicated Bone List with each ID
            TranslateX_DBLI = cmds.getAttr("%s.translateX" % DuplicateBoneListID)
            TranslateY_DBLI = cmds.getAttr("%s.translateY" % DuplicateBoneListID)
            TranslateZ_DBLI = cmds.getAttr("%s.translateZ" % DuplicateBoneListID)
            #calculating different between Duplicated bones and DHI	
            ADL_X = TranslateX_DBLI - TranslateX_OBLI
            ADL_Y = TranslateY_DBLI - TranslateY_OBLI
            ADL_Z = TranslateZ_DBLI - TranslateZ_OBLI
            offsetLIST.append(ADL_X)
            offsetLIST.append(ADL_Y)
            offsetLIST.append(ADL_Z)

        ndBoneList_ID1 = ndBoneList_ID1 + 1
        

    del offsetLIST[987]
    del offsetLIST[987]
    del offsetLIST[1951]
    del offsetLIST[1952]
    del offsetLIST[2390]


    #using ADL to RL4 Node


    bone_TransformID = 0
    while bone_TransformID < len(rigBones):
        bone_transform = rigBones[bone_TransformID]
        #Create Add Double Linear Node and connect them
        adlName = 'ADL_%s'%rigBones[bone_TransformID]
        adlName1 = adlName.replace(":","")
        adlName2 = adlName1.replace(".","_")
        
        #create ADL node
        cmds.createNode( 'addDoubleLinear', n=adlName2 )
        rlno = 'rigLogicNode.jntTranslationOutputs[%s]'%bone_TransformID
        adlNNI = '%s.input1'%adlName2
        
        #Connect ADL to RL4
        cmds.connectAttr(rlno, adlNNI)
        bo = rigBones[bone_TransformID]
        adlNNO = '%s.output'%adlName2
        
        #Connect ADL to Joint
        cmds.connectAttr(adlNNO, bo, force=1)
        
        #Give ADL I2 Values	
        adlNNI2 = '%s.input2'%adlName2	
        cmds.setAttr(adlNNI2, offsetLIST[bone_TransformID])
        
        
        bone_TransformID = bone_TransformID+1
        
rl4_node_op()
cmds.select( clear=True )
cmds.delete('spine_04')

head_blendshape = pm.duplicate(head_org,rr=1)
teeth_blendshape = pm.duplicate(teeth_org,rr=1)
saliva_blendshape = pm.duplicate(saliva_org,rr=1)
eyeLeft_blendshape = pm.duplicate(eyeLeft_org,rr=1)
eyeRight_blendshape = pm.duplicate(eyeRight_org,rr=1)
eyeshell_blendshape = pm.duplicate(eyeshell_org,rr=1)
eyelashes_blendshape = pm.duplicate(eyelashes_org,rr=1)
eyeEdge_blendshape = pm.duplicate(eyeEdge_org,rr=1)
cartilage_blendshape = pm.duplicate(cartilage_org,rr=1)

def blendshapeweight1(nodeA,listB):
    pm.select(nodeA,listB[0])
    BlendShapeA=pm.mel.eval('blendShape;')
    pm.PyNode(BlendShapeA[0]).weight[0].set(1)
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
    """
    pm.copySkinWeights( ss=skinclusterList[0], ds=skinclusterListB[0], noMirror=True, 
                        uv = [skinclusterList[0], skinclusterListB[0]], influenceAssociation="label" )
    """
#skincopyUV(pm.PyNode('pSphere1'),pm.PyNode('pSphere4'))    
#skincopyUV(pm.PyNode('saliva_lod0_mesh'),pm.PyNode('saliva_lod0_mesh2'))
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
#Give ADL I2 Values	
#adlNNI2 = '%s.input2'%adlName2	
#cmds.setAttr(adlNNI2, offsetLIST[bone_TransformID])


#bone_TransformID = bone_TransformID+1
        
rl4_node_op()
cmds.select( clear=True )
cmds.delete('spine_04')

head_blendshape = pm.duplicate(head_org,rr=1)
teeth_blendshape = pm.duplicate(teeth_org,rr=1)
saliva_blendshape = pm.duplicate(saliva_org,rr=1)
eyeLeft_blendshape = pm.duplicate(eyeLeft_org,rr=1)
eyeRight_blendshape = pm.duplicate(eyeRight_org,rr=1)
eyeshell_blendshape = pm.duplicate(eyeshell_org,rr=1)
eyelashes_blendshape = pm.duplicate(eyelashes_org,rr=1)
eyeEdge_blendshape = pm.duplicate(eyeEdge_org,rr=1)
cartilage_blendshape = pm.duplicate(cartilage_org,rr=1)

def blendshapeweight1(nodeA,listB):
    pm.select(nodeA,listB[0])
    BlendShapeA=pm.mel.eval('blendShape;')
    pm.PyNode(BlendShapeA[0]).weight[0].set(1)
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
    """
    pm.copySkinWeights( ss=skinclusterList[0], ds=skinclusterListB[0], noMirror=True, 
                        uv = [skinclusterList[0], skinclusterListB[0]], influenceAssociation="label" )
    """
#skincopyUV(pm.PyNode('pSphere1'),pm.PyNode('pSphere4'))    
#skincopyUV(pm.PyNode('saliva_lod0_mesh'),pm.PyNode('saliva_lod0_mesh2'))
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