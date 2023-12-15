import unreal
import csv
import tkinter as tk
from tkinter import filedialog
UR_52_CTRL=["CTRL_C_jaw.X","CTRL_C_jaw.Y","CTRL_R_jaw_clench","CTRL_C_jaw_openExtreme","CTRL_C_jaw_fwdBack","CTRL_L_jaw_clench","CTRL_L_neck_mastoidContract","CTRL_L_neck_stretch","CTRL_neck_digastricUpDown","CTRL_R_neck_stretch","CTRL_neck_throatExhaleInhale","CTRL_R_neck_mastoidContract","CTRL_neck_throatUpDown","CTRL_L_jaw_chinCompress","CTRL_R_jaw_ChinRaiseD","CTRL_R_jaw_ChinRaiseU","CTRL_L_jaw_ChinRaiseU","CTRL_R_jaw_chinCompress","CTRL_L_jaw_ChinRaiseD","CTRL_R_mouth_lipsBlow","CTRL_R_mouth_lipsPressU","CTRL_L_mouth_lipsTogetherU","CTRL_L_mouth_lipsTogetherD","CTRL_R_mouth_lipSticky","CTRL_L_mouth_lipSticky","CTRL_R_mouth_lipsTogetherU","CTRL_L_mouth_lipsPressU","CTRL_L_mouth_lipsBlow","CTRL_R_mouth_lipsTogetherD","CTRL_R_mouth_stretchLipsClose","CTRL_L_mouth_stretchLipsClose","CTRL_C_tongue_press","CTRL_C_tongue_bendTwist.X","CTRL_C_tongue_bendTwist.Y","CTRL_C_tongue_tipMove.X","CTRL_C_tongue_tipMove.Y","CTRL_C_tongue_move.X","CTRL_C_tongue_move.Y","CTRL_C_tongue_wideNarrow","CTRL_C_tongue_inOut","CTRL_C_tongue_roll","CTRL_C_mouth.X","CTRL_C_mouth.Y","CTRL_L_mouth_upperLipRaise","CTRL_L_mouth_sharpCornerPull","CTRL_L_mouth_cornerPull","CTRL_L_mouth_dimple","CTRL_L_mouth_cornerDepress","CTRL_L_mouth_stretch","CTRL_L_mouth_lowerLipDepress","CTRL_R_mouth_lowerLipDepress","CTRL_R_mouth_stretch","CTRL_L_mouth_towardsD","CTRL_R_mouth_stickyInnerU","CTRL_R_mouth_funnelU","CTRL_C_neck_swallow","CTRL_R_mouth_stickyOuterD","CTRL_C_mouth_stickyD","CTRL_L_mouth_towardsU","CTRL_R_mouth_stickyInnerD","CTRL_R_mouth_lipBiteD","CTRL_R_mouth_funnelD","CTRL_R_mouth_stickyOuterU","CTRL_C_mouth_stickyU","CTRL_L_mouth_tightenD","CTRL_L_mouth_pressU","CTRL_R_mouth_tightenD","CTRL_L_mouth_stickyInnerU","CTRL_L_mouth_funnelD","CTRL_L_mouth_suckBlow","CTRL_L_mouth_tightenU","CTRL_R_mouth_tightenU","CTRL_L_mouth_pressD","CTRL_L_mouth_funnelU","CTRL_R_mouth_towardsU","CTRL_L_mouth_stickyOuterD","CTRL_R_mouth_purseD","CTRL_L_mouth_lipBiteU","CTRL_R_mouth_pressD","CTRL_R_mouth_pressU","CTRL_L_mouth_purseD","CTRL_R_mouth_lipBiteU","CTRL_R_mouth_suckBlow","CTRL_L_mouth_purseU","CTRL_R_mouth_towardsD","CTRL_L_mouth_stickyInnerD","CTRL_L_mouth_lipBiteD","CTRL_R_mouth_purseU","CTRL_L_mouth_stickyOuterU","CTRL_R_mouth_cornerDepress","CTRL_R_mouth_upperLipRaise","CTRL_R_mouth_dimple","CTRL_R_mouth_sharpCornerPull","CTRL_R_mouth_cornerPull","CTRL_R_ear_up","CTRL_L_ear_up","CTRL_R_nose.X","CTRL_R_nose.Y","CTRL_L_nose.X","CTRL_L_nose.Y","CTRL_L_eye.X","CTRL_L_eye.Y","CTRL_L_eye_blink","CTRL_R_eye.X","CTRL_R_eye.Y","CTRL_R_eye_blink","CTRL_R_eye_pupil","CTRL_L_eye_pupil","CTRL_C_eye.X","CTRL_C_eye.Y","CTRL_C_eye_parallelLook","CTRL_L_eye_cheekRaise","CTRL_L_eye_squintInner","CTRL_L_eye_lidPress","CTRL_L_nose_wrinkleUpper","CTRL_R_nose_wrinkleUpper","CTRL_R_eye_squintInner","CTRL_R_eye_cheekRaise","CTRL_R_eye_lidPress","CTRL_R_brow_lateral","CTRL_L_brow_lateral","CTRL_R_brow_down","CTRL_L_brow_down","CTRL_L_brow_raiseOut","CTRL_L_brow_raiseIn","CTRL_R_brow_raiseIn","CTRL_R_brow_raiseOut","CTRL_lookAtSwitch","CTRL_C_teethD.X","CTRL_C_teethD.Y","CTRL_C_teethU.X","CTRL_C_teethU.Y","CTRL_C_teeth_fwdBackU","CTRL_L_mouth_corner.X","CTRL_L_mouth_corner.Y","CTRL_R_mouth_corner.X","CTRL_R_mouth_corner.Y","CTRL_C_teeth_fwdBackD","CTRL_R_eye_faceScrunch","CTRL_L_mouth_pushPullU","CTRL_R_eyelashes_tweakerOut","CTRL_R_mouth_thicknessU","CTRL_L_mouth_pushPullD","CTRL_L_mouth_thicknessU","CTRL_R_mouth_cornerSharpnessD","CTRL_C_mouth_lipShiftD","CTRL_R_mouth_lipsRollD","CTRL_L_eyelashes_tweakerOut","CTRL_L_mouth_thicknessD","CTRL_R_mouth_cornerSharpnessU","CTRL_C_mouth_lipShiftU","CTRL_R_eyelashes_tweakerIn","CTRL_R_mouth_lipsRollU","CTRL_L_eye_eyelidU","CTRL_L_mouth_lipsRollD","CTRL_L_mouth_cornerSharpnessD","CTRL_R_mouth_thicknessD","CTRL_L_eye_eyelidD","CTRL_L_mouth_lipsRollU","CTRL_L_mouth_cornerSharpnessU","CTRL_L_nose_nasolabialDeepen","CTRL_L_eye_faceScrunch","CTRL_R_mouth_pushPullU","CTRL_R_mouth_lipsTowardsTeethD","CTRL_L_mouth_lipsTowardsTeethD","CTRL_R_eye_eyelidU","CTRL_L_eyelashes_tweakerIn","CTRL_R_nose_nasolabialDeepen","CTRL_R_mouth_pushPullD","CTRL_L_mouth_lipsTowardsTeethU","CTRL_R_eye_eyelidD","CTRL_R_mouth_lipsTowardsTeethU","CTRL_R_mouth_lipsPressD","CTRL_L_mouth_lipsPressD","CTRL_faceGUIfollowHead","CTRL_eyesAimFollowHead","CTRL_C_tongue_thickThin","CTRL_R_mouth_thicknessInwardU","CTRL_L_mouth_thicknessInwardU","CTRL_R_mouth_thicknessInwardD","CTRL_L_mouth_thicknessInwardD"]
writeCSV=[]
face_anim = {}
writeCSV.append(UR_52_CTRL)
world = unreal.get_editor_subsystem(unreal.UnrealEditorSubsystem).get_editor_world()
sequence_asset = unreal.LevelSequenceEditorBlueprintLibrary.get_current_level_sequence()
editor_asset_name = unreal.EditorAssetLibrary.get_path_name_for_loaded_asset(sequence_asset).split('.')[-1]
#print (editor_asset_name)
rangeA = sequence_asset.get_playback_range()
#print (rangeA)
sequencer_objects_list_temp = unreal.SequencerTools.get_bound_objects(world, sequence_asset, sequence_asset.get_bindings(), rangeA)
#print (sequencer_objects_list_temp)

for obj in sequencer_objects_list_temp:
    bound_objects = obj.bound_objects
    if type(bound_objects[0]) == unreal.Actor:
        #print (bound_objects[0].get_actor_label())
        actor = bound_objects[0]
        asset_name = bound_objects[0].get_actor_label()
        #print (actor)
        bp_possessable = sequence_asset.add_possessable(actor)
        #print (bp_possessable)
        child_possessable_list = bp_possessable.get_child_possessables()
        character_name = ''
        for current_child in child_possessable_list:
            if 'Face' in current_child.get_name():
                face_possessable = current_child
                #print(face_possessable)
        if face_possessable:
            character_name = (face_possessable.get_parent().get_display_name()) 
            #print (character_name)
            face_possessable_track_list = face_possessable.get_tracks()
            #print(face_possessable_track_list)
            face_control_rig_track=face_possessable_track_list[-1]
            face_control_channel_list = unreal.MovieSceneSectionExtensions.get_all_channels(face_control_rig_track.get_sections()[0])
            #print (face_control_channel_list)
            face_control_name_list = []
            for channel in face_control_channel_list:
                channel_name = str(channel.get_name())
                channel_nameA=channel_name.rsplit('_',1)
                face_control_name_list.append(channel_nameA[0])
                #print(channel_nameA[0])
            numKeys = face_control_channel_list[0].get_num_keys()
            print (numKeys)            
            for ctrl_num in range(0,len(UR_52_CTRL)):
                getValue=[]
                key_list = [None] * numKeys
                keys = face_control_channel_list[ctrl_num].get_keys()
                for key in range(0, numKeys):
                    key_value = keys[key].get_value()
                    key_time = keys[key].get_time(time_unit=unreal.SequenceTimeUnit.DISPLAY_RATE).frame_number.value
                    key_list[key]=([key_value, key_time])
                face_anim[UR_52_CTRL[ctrl_num]] =  key_list
            #print (face_anim)           
            
            for IntFrame in range(0,int(numKeys)):
                testA=[]
                for ctrl_num in range(0,len(UR_52_CTRL)):
                    testA.append( face_anim[UR_52_CTRL[ctrl_num]][IntFrame][0] )
                writeCSV.append(testA)
            print (writeCSV)

        #keys_file = filedialog.asksaveasfile(initialfile = str(editor_asset_name) + '_' + character_name + '_face_anim' + '.csv', defaultextension=".csv",filetypes=[("All Files","*.*"),("CSV file","*.csv")])
        #for i in writeCSV:
        #    keys_file.writerow(i) 
keys_file = filedialog.asksaveasfile(initialfile = 'test.csv', defaultextension=".csv",filetypes=[("All Files","*.*"),("CSV file","*.csv")])        
savecsv=str(keys_file.name)
f = open(savecsv,'w', newline='')
wr = csv.writer(f)
for i in writeCSV:
    wr.writerow(i) 
f.close()           
print ('wwwwwwwwwwwwwwwwwabcdefghijklopqrstuvwxyzwwwwwwwwww') 
