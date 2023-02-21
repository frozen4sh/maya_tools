import pymel.core as pm
#  retarget
#    head_retarget
#    teeth_retarget
#    saliva_retarget
#    eyeLeft_retarget
#    eyeRight_retarget
#    eyeshell_retarget
#    eyelashes_retarget
#    eyeEdge_retarget
#    cartilage_retarget
# 상위 그룹 한개 선택하면 
errerCheck=False
selObj=pm.ls(sl=1)
selChildren=None
if len( selObj ) == 1:
    selChildren=selObj[0].getChildren()
    if len(selChildren) ==9:
        errerCheck=True
if errerCheck:
    print '0k'
    selObj[0].rename('retarget')
    #delete ORG node
    for i in selChildren:
        for j in i.getChildren(s=1):
            if j.nodeName()[-5:]!='Shape':
                pm.delete(j)
            print j
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