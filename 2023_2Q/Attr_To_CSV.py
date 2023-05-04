# # # import maya.cmds as cmds
# # # import csv

# # # with open('eggs.csv', 'w', newline='') as csvfile:
# # #     spamwriter = csv.writer(csvfile, delimiter=' ',
# # #                             quotechar='|', quoting=csv.QUOTE_MINIMAL)
# # #     spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
# # #     spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])



# # # # a=("teethBackD","teethBackD","browDownL","browDownR","browLateralL","browLateralR","browRaiseInL","browRaiseInR","browRaiseOuterL","browRaiseOuterR","earUpL","earUpR","eyeBlinkL","eyeBlinkR","eyeLidPressL","eyeLidPressR","eyeWidenL","eyeWidenR",
# # # #    "eyeSquintInnerL","eyeSquintInnerR","eyeCheekRaiseL","eyeCheekRaiseR","eyeFaceScrunchL","eyeFaceScrunchR","eyeUpperLidUpL","eyeUpperLidUpR","eyeRelaxL","eyeRelaxR","eyeLowerLidUpL","eyeLowerLidUpR","eyeLowerLidDownL","eyeLowerLidDownR","eyeLookUpL","eyeLookUpR","eyeLookDownL","eyeLookDownR","eyeLookLeftL","eyeLookLeftR","eyeLookRightL","eyeLookRightR","eyePupilWideL","eyePupilWideR","eyePupilNarrowL","eyePupilNarrowR","eyeParallelLookDirection","eyelashesUpINL","eyelashesUpINR","eyelashesUpOUTL","eyelashesUpOUTR","eyelashesDownINL","eyelashesDownINR","eyelashesDownOUTL","eyelashesDownOUTR","noseWrinkleL","noseWrinkleR","noseWrinkleUpperL","noseWrinkleUpperR","noseNostrilDepressL","noseNostrilDepressR","noseNostrilDilateL","noseNostrilDilateR","noseNostrilCompressL","noseNostrilCompressR","noseNasolabialDeepenL","noseNasolabialDeepenR","mouthCheekSuckL","mouthCheekSuckR","mouthCheekBlowL","mouthCheekBlowR","mouthLipsBlowL","mouthLipsBlowR","mouthLeft","mouthRight","mouthUp","mouthDown","mouthUpperLipRaiseL","mouthUpperLipRaiseR","mouthLowerLipDepressL","mouthLowerLipDepressR","mouthCornerPullL","mouthCornerPullR","mouthStretchL","mouthStretchR","mouthStretchLipsCloseL","mouthStretchLipsCloseR","mouthDimpleL","mouthDimpleR","mouthCornerDepressL","mouthCornerDepressR","mouthPressUL","mouthPressUR","mouthPressDL","mouthPressDR","mouthLipsPurseUL","mouthLipsPurseUR","mouthLipsPurseDL","mouthLipsPurseDR","mouthLipsTowardsUL","mouthLipsTowardsUR","mouthLipsTowardsDL","mouthLipsTowardsDR","mouthFunnelUL","mouthFunnelUR","mouthFunnelDL","mouthFunnelDR","mouthLipsTogetherUL","mouthLipsTogetherUR","mouthLipsTogetherDL","mouthLipsTogetherDR","mouthUpperLipBiteL","mouthUpperLipBiteR","mouthLowerLipBiteL","mouthLowerLipBiteR","mouthLipsTightenUL","mouthLipsTightenUR","mouthLipsTightenDL","mouthLipsTightenDR","mouthLipsPressL","mouthLipsPressR","mouthSharpCornerPullL","mouthSharpCornerPullR","mouthStickyUC","mouthStickyUINL","mouthStickyUINR","mouthStickyUOUTL","mouthStickyUOUTR","mouthStickyDC","mouthStickyDINL","mouthStickyDINR","mouthStickyDOUTL","mouthStickyDOUTR","mouthLipsStickyLPh1","mouthLipsStickyLPh2","mouthLipsStickyLPh3","mouthLipsStickyRPh1","mouthLipsStickyRPh2","mouthLipsStickyRPh3","mouthLipsPushUL","mouthLipsPushUR","mouthLipsPushDL","mouthLipsPushDR","mouthLipsPullUL","mouthLipsPullUR","mouthLipsPullDL","mouthLipsPullDR","mouthLipsThinUL","mouthLipsThinUR","mouthLipsThinDL","mouthLipsThinDR","mouthLipsThickUL","mouthLipsThickUR","mouthLipsThickDL","mouthLipsThickDR","mouthCornerSharpenUL","mouthCornerSharpenUR","mouthCornerSharpenDL","mouthCornerSharpenDR","mouthCornerRounderUL","mouthCornerRounderUR","mouthCornerRounderDL","mouthCornerRounderDR","mouthUpperLipTowardsTeethL","mouthUpperLipTowardsTeethR","mouthLowerLipTowardsTeethL","mouthLowerLipTowardsTeethR","mouthUpperLipShiftLeft","mouthUpperLipShiftRight","mouthLowerLipShiftLeft","mouthLowerLipShiftRight","mouthUpperLipRollInL","mouthUpperLipRollInR","mouthUpperLipRollOutL","mouthUpperLipRollOutR","mouthLowerLipRollInL","mouthLowerLipRollInR","mouthLowerLipRollOutL","mouthLowerLipRollOutR","mouthCornerUpL","mouthCornerUpR","mouthCornerDownL","mouthCornerDownR","mouthCornerWideL","mouthCornerWideR","mouthCornerNarrowL","mouthCornerNarrowR","tongueUp","tongueDown","tongueLeft","tongueRight","tongueOut","tongueIn","tongueRollUp","tongueRollDown","tongueRollLeft","tongueRollRight","tongueTipUp","tongueTipDown","tongueTipLeft","tongueTipRight","tongueWide","tongueNarrow","tonguePress","jawOpen","jawLeft","jawRight","jawFwd","jawBack","jawClenchL","jawClenchR","jawChinRaiseDL","jawChinRaiseDR","jawChinRaiseUL","jawChinRaiseUR","jawChinCompressL","jawChinCompressR","jawOpenExtreme","neckStretchL","neckStretchR","neckSwallowPh1","neckSwallowPh2","neckSwallowPh3","neckSwallowPh4","neckMastoidContractL","neckMastoidContractR","neckThroatDown","neckThroatUp","neckDigastricDown","neckDigastricUp","neckThroatExhale","neckThroatInhale","teethUpU","teethUpD","teethDownU","teethDownD","teethLeftU","teethLeftD","teethRightU","teethRightD","teethFwdU","teethFwdD","teethBackU")

# # # # for j in range(100):
# # # #     cmds.currentTime(j)
# # # #     for i in a:
# # # #         v=cmds.getAttr('CTRL_expressions.'+i)
# # # #         print (j,i,v)   


# # import maya.cmds as cmds
# # import csv

# # # Define function to create UI pop-up
# # def create_ui():
# #     # Create window
# #     window_name = 'Export Attributes'
# #     if cmds.window(window_name, exists=True):
# #         cmds.deleteUI(window_name)
# #     window = cmds.window(window_name, title='Export Attributes', sizeable=False)
# #     cmds.columnLayout(adjustableColumn=True)

# #     # Add text fields for start and end frames
# #     cmds.text(label='Start Frame:')
# #     start_frame_field = cmds.intField(value=1, minValue=1)
# #     cmds.text(label='End Frame:')
# #     end_frame_field = cmds.intField(value=10, minValue=1)

# #     # Add button to export attributes
# #     cmds.separator(height=10, style='none')
# #     cmds.button(label='Export', command=lambda *args: export_attributes(start_frame_field, end_frame_field))
# #     cmds.showWindow(window)

# # # Define function to export attributes
# # def export_attributes(start_frame_field, end_frame_field):
# #     # Get start and end frames from UI fields
# #     start_frame = cmds.intField(start_frame_field, query=True, value=True)
# #     end_frame = cmds.intField(end_frame_field, query=True, value=True)

# #     # Get selected object
# #     selected_obj = cmds.ls(selection=True)

# #     # Get attributes of the selected object
# #     attributes = cmds.listAttr(selected_obj[0], visible=True, keyable=True)

# #     # Open the CSV file in write mode
# #     with open('D:\\attributes.csv', 'w', newline='') as csv_file:
# #         writer = csv.writer(csv_file)

# #         # Write header row
# #         writer.writerow(['Frame'] + attributes)

# #         # Write data rows for each frame in the range
# #         for frame in range(start_frame, end_frame+1):
# #             cmds.currentTime(frame)
# #             data_rows = [frame]
# #             for attribute in attributes:
# #                 attribute_value = cmds.getAttr(selected_obj[0] + '.' + attribute)
# #                 data_rows.append(attribute_value)
# #             writer.writerow(data_rows)
            
# #     print('Attributes saved to attributes.csv')

# # # Call the create_ui() function to start the UI
# # create_ui()

# import maya.cmds as cmds
# import csv
# import os

# cmds.select ('CTRL_expressions')

# # Define function to create UI pop-up
# def create_ui():
#     # Create window
#     window_name = 'Export Attributes'
#     if cmds.window(window_name, exists=True):
#         cmds.deleteUI(window_name)
#     window = cmds.window(window_name, title='Export Attributes', sizeable=False)
#     cmds.columnLayout(adjustableColumn=True)

#     # Add text fields for start and end frames
#     cmds.text(label='Start Frame:')
#     start_frame_field = cmds.intField(value=0, minValue=0)
#     cmds.text(label='End Frame:')
#     end_frame_field = cmds.intField(value=200, minValue=0)

#     # Add button to export attributes
#     cmds.separator(height=10, style='none')
#     cmds.button(label='Export', command=lambda *args: export_attributes(start_frame_field, end_frame_field))
#     cmds.showWindow(window)

# # Define function to export attributes
# def export_attributes(start_frame_field, end_frame_field):
#     # Get start and end frames from UI fields
#     start_frame = cmds.intField(start_frame_field, query=True, value=True)
#     end_frame = cmds.intField(end_frame_field, query=True, value=True)

#     # Get selected object
#     selected_obj = cmds.ls(selection=True)

#     # Get attributes of the selected object
#     attributes = cmds.listAttr(selected_obj[0], visible=True, keyable=True)

#     # Get scene file name without extension
#     scene_path = cmds.file(query=True, sceneName=True)
#     scene_dir, scene_file = os.path.split(scene_path)
#     scene_name, scene_ext = os.path.splitext(scene_file)

#     # Open the CSV file in write mode with scene name
#     with open(os.path.join(scene_dir, scene_name + '.csv'), 'w', newline='') as csv_file:
#         writer = csv.writer(csv_file)

#         # Write header row
#         writer.writerow(['Frame'] + attributes)

#         # Write data rows for each frame in the range
#         for frame in range(start_frame, end_frame+1):
#             cmds.currentTime(frame)
#             data_rows = [frame]
#             for attribute in attributes:
#                 attribute_value = cmds.getAttr(selected_obj[0] + '.' + attribute)
#                 data_rows.append(attribute_value)
#             writer.writerow(data_rows)
            
#     print('Attributes saved to ' + scene_name + '.csv')

# # Call the create_ui() function to start the UI
# create_ui()



# import maya.cmds as cmds
# import csv
# import os

# cmds.select ('CTRL_expressions')

# # Define function to create UI pop-up
# def create_ui():
#     # Create window
#     window_name = 'Export Attributes'
#     if cmds.window(window_name, exists=True):
#         cmds.deleteUI(window_name)
#     window = cmds.window(window_name, title='Export Attributes', sizeable=False)
#     cmds.columnLayout(adjustableColumn=True)

#     # Add text fields for start and end frames
#     cmds.text(label='Start Frame:')
#     minTime_int = cmds.playbackOptions(q=1,minTime=1)
#     start_frame_field = cmds.intField(value=minTime_int, minValue=0)
#     cmds.text(label='End Frame:')
#     maxTime_int = cmds.playbackOptions(q=1,maxTime=1)
#     end_frame_field = cmds.intField(value=maxTime_int, minValue=0)

#     # Add button to export attributes
#     cmds.separator(height=10, style='none')
#     cmds.button(label='Export', command=lambda *args: export_attributes(start_frame_field, end_frame_field))
#     cmds.showWindow(window)

# # Define function to export attributes
# def export_attributes(start_frame_field, end_frame_field):
#     # Get start and end frames from UI fields
#     start_frame = cmds.intField(start_frame_field, query=True, value=True)
#     end_frame = cmds.intField(end_frame_field, query=True, value=True)

#     # Get selected object
#     selected_obj = cmds.ls(selection=True)

#     # Get attributes of the selected object
#     attributes = cmds.listAttr(selected_obj[0], visible=True, keyable=True)
#     # # 1~51 184~200
#     # poplist=[]
#     # poplistA=range(0,52)
#     # poplistB=range(184,201)
#     # poplist.extend(poplistA)
#     # poplist.extend(poplistB)
#     # poplist.reverse
#     # for i in poplist:
#     #     attribute.pop(i)
#     # Get scene file name without extension
#     scene_path = cmds.file(query=True, sceneName=True)
#     scene_dir, scene_file = os.path.split(scene_path)
#     scene_name, scene_ext = os.path.splitext(scene_file)

#     # Open the CSV file in write mode with scene name
#     with open(os.path.join(scene_dir, scene_name + '.csv'), 'w', newline='') as csv_file:
#         writer = csv.writer(csv_file)

#         # Write header row
#         writer.writerow(['Frame'] + attributes)

#         # Write data rows for each frame in the range
#         for frame in range(start_frame, end_frame+1):
#             cmds.currentTime(frame)
#             data_rows = [frame]
#             for attribute in attributes:
#                 attribute_value = cmds.getAttr(selected_obj[0] + '.' + attribute)
#                 data_rows.append(attribute_value)
#             writer.writerow(data_rows)
            
#     print('Attributes saved to ' + scene_name + '.csv')

# # Call the create_ui() function to start the UI
# create_ui()

import maya.cmds as cmds
import csv
import os

cmds.select ('CTRL_expressions')
# Define function to create UI pop-up
def create_ui():
    # Create window
    window_name = 'Export_Attributes'
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)
    window = cmds.window(window_name, title='Export Attributes', sizeable=False)
    cmds.columnLayout(adjustableColumn=True)

    # Add text fields for start and end frames
    cmds.text(label='Start Frame:')
    minTime_int = cmds.playbackOptions(q=1,minTime=1)
    start_frame_field = cmds.intField(value=minTime_int, minValue=0)
    cmds.text(label='End Frame:')
    maxTime_int = cmds.playbackOptions(q=1,maxTime=1)
    end_frame_field = cmds.intField(value=maxTime_int, minValue=0)

    # Add button to export attributes
    cmds.separator(height=10, style='none')
    cmds.button(label='Export', command=lambda *args: export_attributes(start_frame_field, end_frame_field,window))
    cmds.showWindow(window)

# Define function to export attributes
def export_attributes(start_frame_field, end_frame_field,window):
    # Get start and end frames from UI fields
    start_frame = cmds.intField(start_frame_field, query=True, value=True)
    end_frame = cmds.intField(end_frame_field, query=True, value=True)

    # Get selected object
    selected_obj = cmds.ls(selection=True)

    # Get attributes of the selected object
    attributes = cmds.listAttr(selected_obj[0], visible=True, keyable=True)
    # 1~51 184~200
    poplist=[]
    poplistA=range(0,51)
    poplistB=range(183,200)
    poplistD=range(228,259)
    poplist.extend(poplistA)
    poplist.extend(poplistB)
    poplist.extend(poplistD)
    poplistC=[]
    inti=0
    for i in range(len(poplist)):
        inti=inti+1
        poplistC.append(poplist[inti*-1])
    #reverse     
    #print ('ok1',poplistC)
    for i in poplistC:
        attributes.pop(i)
    #print (attributes)    
    
    # Get scene file name without extension
    scene_path = cmds.file(query=True, sceneName=True)
    scene_dir, scene_file = os.path.split(scene_path)
    scene_name, scene_ext = os.path.splitext(scene_file)

    # Open the CSV file in write mode with scene name
    with open(os.path.join(scene_dir, scene_name + '.csv'), 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)

        # Write header row
        writer.writerow(['Frame'] + attributes)

        # Write data rows for each frame in the range
        for frame in range(start_frame, end_frame+1):
            cmds.currentTime(frame)
            data_rows = [frame]
            for attribute in attributes:
                attribute_value = cmds.getAttr(selected_obj[0] + '.' + attribute)
                data_rows.append(attribute_value)
            writer.writerow(data_rows)
            
    print('Attributes saved to ' + scene_name + '.csv')    
    cmds.deleteUI(window)
# Call the create_ui() function to start the UI
create_ui()