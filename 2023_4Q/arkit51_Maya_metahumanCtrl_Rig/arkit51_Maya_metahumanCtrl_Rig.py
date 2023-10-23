import pymel.core as pm
import maya.cmds as cmds
#pm.newFile(force=True)
#pm.openFile(r'C:\\Users\\vive\\Documents\\Megascans Library\\Downloaded\\DHI\\8gtikINv_asset\\8k\\asset_source\\MetaHumans\\Myles\\SourceAssets\\Myles_full_rig.mb')
#key51_dic={'Key:CTRL_C_jaw.tx': [(16, 'Key:CTRL_C_jaw.tx', '-1.00'),(17, 'Key:CTRL_C_jaw.tx', '1.00')], 'Key:CTRL_C_jaw.ty': [(18, 'Key:CTRL_C_jaw.ty', '1.00'),(19, 'Key:CTRL_C_jaw.ty', '1.00')], 'Key:CTRL_C_jaw_fwdBack.ty': [(15, 'Key:CTRL_C_jaw_fwdBack.ty', '-1.00')], 'Key:CTRL_C_mouth.tx': [(22, 'Key:CTRL_C_mouth.tx', '1.00'),  (23, 'Key:CTRL_C_mouth.tx', '-1.00')], 'Key:CTRL_L_brow_down.ty': [(42, 'Key:CTRL_L_brow_down.ty', '1.00')], 'Key:CTRL_L_brow_lateral.ty': [(42, 'Key:CTRL_L_brow_lateral.ty', '0.03'),         (43, 'Key:CTRL_L_brow_lateral.ty', '0.03'),         (44, 'Key:CTRL_L_brow_lateral.ty', '1.00'),         (45, 'Key:CTRL_L_brow_lateral.ty', '0.03'),         (46, 'Key:CTRL_L_brow_lateral.ty', '0.03'),         (47, 'Key:CTRL_L_brow_lateral.ty', '0.03'),         (48, 'Key:CTRL_L_brow_lateral.ty', '0.03'),         (49, 'Key:CTRL_L_brow_lateral.ty', '0.03'),         (50, 'Key:CTRL_L_brow_lateral.ty', '0.03'),         (51, 'Key:CTRL_L_brow_lateral.ty', '0.03')], 'Key:CTRL_L_brow_raiseIn.ty': [(44, 'Key:CTRL_L_brow_raiseIn.ty', '1.00'),         (45, 'Key:CTRL_L_brow_raiseIn.ty', '1.00')], 'Key:CTRL_L_brow_raiseOut.ty': [(45, 'Key:CTRL_L_brow_raiseOut.ty', '1.00')], 'Key:CTRL_L_eye.tx': [(3, 'Key:CTRL_L_eye.tx', '-1.00'),(4, 'Key:CTRL_L_eye.tx', '1.00')], 'Key:CTRL_L_eye.ty': [(2, 'Key:CTRL_L_eye.ty', '-1.00'),(5, 'Key:CTRL_L_eye.ty', '1.00')], 'Key:CTRL_L_eye_blink.ty': [(1, 'Key:CTRL_L_eye_blink.ty', '1.00'),      (7, 'Key:CTRL_L_eye_blink.ty', '-1.00')], 'Key:CTRL_L_eye_cheekRaise.ty': [(48, 'Key:CTRL_L_eye_cheekRaise.ty', '1.00')], 'Key:CTRL_L_eye_squintInner.ty': [(6,             'Key:CTRL_L_eye_squintInner.ty',             '1.00')], 'Key:CTRL_L_jaw_ChinRaiseD.ty': [(34, 'Key:CTRL_L_jaw_ChinRaiseD.ty', '1.00')], 'Key:CTRL_L_jaw_ChinRaiseU.ty': [(35, 'Key:CTRL_L_jaw_ChinRaiseU.ty', '1.00')], 'Key:CTRL_L_mouth_cornerDepress.ty': [(26,                 'Key:CTRL_L_mouth_cornerDepress.ty',                 '1.00')], 'Key:CTRL_L_mouth_cornerPull.ty': [(24,              'Key:CTRL_L_mouth_cornerPull.ty',              '1.00')], 'Key:CTRL_L_mouth_dimple.ty': [(28, 'Key:CTRL_L_mouth_dimple.ty', '1.00')], 'Key:CTRL_L_mouth_funnelD.ty': [(20, 'Key:CTRL_L_mouth_funnelD.ty', '1.00'),          (21, 'Key:CTRL_L_mouth_funnelD.ty', '0.75')], 'Key:CTRL_L_mouth_funnelU.ty': [(20, 'Key:CTRL_L_mouth_funnelU.ty', '1.00'),          (21, 'Key:CTRL_L_mouth_funnelU.ty', '0.75')], 'Key:CTRL_L_mouth_lipsBlow.ty': [(47, 'Key:CTRL_L_mouth_lipsBlow.ty', '1.00')], 'Key:CTRL_L_mouth_lipsRollD.ty': [(32,             'Key:CTRL_L_mouth_lipsRollD.ty',             '1.00')], 'Key:CTRL_L_mouth_lipsRollU.ty': [(32,             'Key:CTRL_L_mouth_lipsRollU.ty',             '0.50'),            (33,             'Key:CTRL_L_mouth_lipsRollU.ty',             '1.00')], 'Key:CTRL_L_mouth_lipsTogetherD.ty': [(19,                 'Key:CTRL_L_mouth_lipsTogetherD.ty',                 '1.00')], 'Key:CTRL_L_mouth_lipsTogetherU.ty': [(19,                 'Key:CTRL_L_mouth_lipsTogetherU.ty',                 '1.00')], 'Key:CTRL_L_mouth_lowerLipDepress.ty': [(38,'Key:CTRL_L_mouth_lowerLipDepress.ty','1.00')], 'Key:CTRL_L_mouth_pressD.ty': [(36, 'Key:CTRL_L_mouth_pressD.ty', '1.00')], 'Key:CTRL_L_mouth_pressU.ty': [(36, 'Key:CTRL_L_mouth_pressU.ty', '1.00')], 'Key:CTRL_L_mouth_purseD.ty': [(21, 'Key:CTRL_L_mouth_purseD.ty', '1.00')], 'Key:CTRL_L_mouth_purseU.ty': [(21, 'Key:CTRL_L_mouth_purseU.ty', '1.00')], 'Key:CTRL_L_mouth_stretch.ty': [(30, 'Key:CTRL_L_mouth_stretch.ty', '1.00')], 'Key:CTRL_L_mouth_suckBlow.ty': [(47, 'Key:CTRL_L_mouth_suckBlow.ty', '1.00')], 'Key:CTRL_L_mouth_towardsD.ty': [(21, 'Key:CTRL_L_mouth_towardsD.ty', '0.41')], 'Key:CTRL_L_mouth_towardsU.ty': [(21, 'Key:CTRL_L_mouth_towardsU.ty', '0.41')], 'Key:CTRL_L_mouth_upperLipRaise.ty': [(40,                 'Key:CTRL_L_mouth_upperLipRaise.ty',                 '1.00')], 'Key:CTRL_L_nose.ty': [(50, 'Key:CTRL_L_nose.ty', '1.00')], 'Key:CTRL_R_brow_down.ty': [(43, 'Key:CTRL_R_brow_down.ty', '1.00')], 'Key:CTRL_R_brow_lateral.ty': [(44, 'Key:CTRL_R_brow_lateral.ty', '1.00')], 'Key:CTRL_R_brow_raiseIn.ty': [(44, 'Key:CTRL_R_brow_raiseIn.ty', '1.00'),         (46, 'Key:CTRL_R_brow_raiseIn.ty', '1.00')], 'Key:CTRL_R_brow_raiseOut.ty': [(46, 'Key:CTRL_R_brow_raiseOut.ty', '1.00')], 'Key:CTRL_R_eye.tx': [(10, 'Key:CTRL_R_eye.tx', '1.00'),(11, 'Key:CTRL_R_eye.tx', '-1.00')], 'Key:CTRL_R_eye.ty': [(9, 'Key:CTRL_R_eye.ty', '-1.00'),(12, 'Key:CTRL_R_eye.ty', '1.00')], 'Key:CTRL_R_eye_blink.ty': [(8, 'Key:CTRL_R_eye_blink.ty', '1.00'),      (14, 'Key:CTRL_R_eye_blink.ty', '-1.00')], 'Key:CTRL_R_eye_cheekRaise.ty': [(49, 'Key:CTRL_R_eye_cheekRaise.ty', '1.00')], 'Key:CTRL_R_eye_squintInner.ty': [(13,             'Key:CTRL_R_eye_squintInner.ty',             '1.00')], 'Key:CTRL_R_jaw_ChinRaiseD.ty': [(34, 'Key:CTRL_R_jaw_ChinRaiseD.ty', '1.00')], 'Key:CTRL_R_jaw_ChinRaiseU.ty': [(35, 'Key:CTRL_R_jaw_ChinRaiseU.ty', '1.00')], 'Key:CTRL_R_mouth_cornerDepress.ty': [(27,                 'Key:CTRL_R_mouth_cornerDepress.ty',                 '1.00')], 'Key:CTRL_R_mouth_cornerPull.ty': [(25,              'Key:CTRL_R_mouth_cornerPull.ty',              '1.00')], 'Key:CTRL_R_mouth_dimple.ty': [(29, 'Key:CTRL_R_mouth_dimple.ty', '1.00')], 'Key:CTRL_R_mouth_funnelD.ty': [(20, 'Key:CTRL_R_mouth_funnelD.ty', '1.00'),          (21, 'Key:CTRL_R_mouth_funnelD.ty', '0.75')], 'Key:CTRL_R_mouth_funnelU.ty': [(20, 'Key:CTRL_R_mouth_funnelU.ty', '1.00'),          (21, 'Key:CTRL_R_mouth_funnelU.ty', '0.75')], 'Key:CTRL_R_mouth_lipsBlow.ty': [(47, 'Key:CTRL_R_mouth_lipsBlow.ty', '1.00')], 'Key:CTRL_R_mouth_lipsRollD.ty': [(32,             'Key:CTRL_R_mouth_lipsRollD.ty',             '1.00')], 'Key:CTRL_R_mouth_lipsRollU.ty': [(32,             'Key:CTRL_R_mouth_lipsRollU.ty',             '0.50'),            (33,             'Key:CTRL_R_mouth_lipsRollU.ty',             '1.00')], 'Key:CTRL_R_mouth_lipsTogetherD.ty': [(19,                 'Key:CTRL_R_mouth_lipsTogetherD.ty',                 '1.00')], 'Key:CTRL_R_mouth_lipsTogetherU.ty': [(19,                 'Key:CTRL_R_mouth_lipsTogetherU.ty',                 '1.00')], 'Key:CTRL_R_mouth_lowerLipDepress.ty': [(39,'Key:CTRL_R_mouth_lowerLipDepress.ty','1.00')], 'Key:CTRL_R_mouth_pressD.ty': [(37, 'Key:CTRL_R_mouth_pressD.ty', '1.00')], 'Key:CTRL_R_mouth_pressU.ty': [(37, 'Key:CTRL_R_mouth_pressU.ty', '1.00')], 'Key:CTRL_R_mouth_purseD.ty': [(21, 'Key:CTRL_R_mouth_purseD.ty', '1.00')], 'Key:CTRL_R_mouth_purseU.ty': [(21, 'Key:CTRL_R_mouth_purseU.ty', '1.00')], 'Key:CTRL_R_mouth_stretch.ty': [(31, 'Key:CTRL_R_mouth_stretch.ty', '1.00')], 'Key:CTRL_R_mouth_suckBlow.ty': [(47, 'Key:CTRL_R_mouth_suckBlow.ty', '1.00')], 'Key:CTRL_R_mouth_towardsD.ty': [(21, 'Key:CTRL_R_mouth_towardsD.ty', '0.41')], 'Key:CTRL_R_mouth_towardsU.ty': [(21, 'Key:CTRL_R_mouth_towardsU.ty', '0.41')], 'Key:CTRL_R_mouth_upperLipRaise.ty': [(41,                 'Key:CTRL_R_mouth_upperLipRaise.ty',                 '1.00')], 'Key:CTRL_R_nose.ty': [(51, 'Key:CTRL_R_nose.ty', '1.00')]}
key51_dic={'CTRL_C_jaw.tx': [(17, 'CTRL_C_jaw.tx', '-1.00'),(18, 'CTRL_C_jaw.tx', '1.00')], 'CTRL_C_jaw.ty': [(19, 'CTRL_C_jaw.ty', '1.00')], 'CTRL_C_jaw_fwdBack.ty': [(16, 'CTRL_C_jaw_fwdBack.ty', '-1.00')], 'CTRL_C_mouth.tx': [(22, 'CTRL_C_mouth.tx', '1.00'),  (23, 'CTRL_C_mouth.tx', '-1.00')], 'CTRL_C_tongue_inOut.ty': [(52, 'CTRL_C_tongue_inOut.ty', '-0.77')], 'CTRL_C_tongue_move.tx': [(52, 'CTRL_C_tongue_move.tx', '-0.07')], 'CTRL_C_tongue_move.ty': [(52, 'CTRL_C_tongue_move.ty', '-0.83')], 'CTRL_C_tongue_wideNarrow.ty': [(52, 'CTRL_C_tongue_wideNarrow.ty', '0.63')], 'CTRL_L_brow_down.ty': [(42, 'CTRL_L_brow_down.ty', '1.00')], 'CTRL_L_brow_lateral.ty': [(42, 'CTRL_L_brow_lateral.ty', '0.03'),         (43, 'CTRL_L_brow_lateral.ty', '0.03'),         (44, 'CTRL_L_brow_lateral.ty', '1.00'),         (45, 'CTRL_L_brow_lateral.ty', '0.03'),         (46, 'CTRL_L_brow_lateral.ty', '0.03'),         (47, 'CTRL_L_brow_lateral.ty', '0.03'),         (48, 'CTRL_L_brow_lateral.ty', '0.03'),         (49, 'CTRL_L_brow_lateral.ty', '0.03'),         (50, 'CTRL_L_brow_lateral.ty', '0.03'),         (51, 'CTRL_L_brow_lateral.ty', '0.03'),         (52, 'CTRL_L_brow_lateral.ty', '0.03')], 'CTRL_L_brow_raiseIn.ty': [(44, 'CTRL_L_brow_raiseIn.ty', '1.00'),         (45, 'CTRL_L_brow_raiseIn.ty', '1.00')], 'CTRL_L_brow_raiseOut.ty': [(45, 'CTRL_L_brow_raiseOut.ty', '1.00')], 'CTRL_L_eye.tx': [(4, 'CTRL_L_eye.tx', '-1.00'), (5, 'CTRL_L_eye.tx', '1.00')], 'CTRL_L_eye.ty': [(3, 'CTRL_L_eye.ty', '-1.00'), (6, 'CTRL_L_eye.ty', '1.00')], 'CTRL_L_eye_blink.ty': [(2, 'CTRL_L_eye_blink.ty', '1.00'),      (8, 'CTRL_L_eye_blink.ty', '-1.00')], 'CTRL_L_eye_cheekRaise.ty': [(48, 'CTRL_L_eye_cheekRaise.ty', '1.00')], 'CTRL_L_eye_squintInner.ty': [(7, 'CTRL_L_eye_squintInner.ty', '1.00')], 'CTRL_L_jaw_ChinRaiseD.ty': [(34, 'CTRL_L_jaw_ChinRaiseD.ty', '1.00')], 'CTRL_L_jaw_ChinRaiseU.ty': [(35, 'CTRL_L_jaw_ChinRaiseU.ty', '1.00')], 'CTRL_L_mouth_cornerDepress.ty': [(26,                 'CTRL_L_mouth_cornerDepress.ty',                 '1.00')], 'CTRL_L_mouth_cornerPull.ty': [(24, 'CTRL_L_mouth_cornerPull.ty', '1.00')], 'CTRL_L_mouth_dimple.ty': [(28, 'CTRL_L_mouth_dimple.ty', '1.00')], 'CTRL_L_mouth_funnelD.ty': [(20, 'CTRL_L_mouth_funnelD.ty', '1.00'),          (21, 'CTRL_L_mouth_funnelD.ty', '0.75')], 'CTRL_L_mouth_funnelU.ty': [(20, 'CTRL_L_mouth_funnelU.ty', '1.00'),          (21, 'CTRL_L_mouth_funnelU.ty', '0.75')], 'CTRL_L_mouth_lipsBlow.ty': [(47, 'CTRL_L_mouth_lipsBlow.ty', '1.00')], 'CTRL_L_mouth_lipsRollD.ty': [(32, 'CTRL_L_mouth_lipsRollD.ty', '1.00')], 'CTRL_L_mouth_lipsRollU.ty': [(32, 'CTRL_L_mouth_lipsRollU.ty', '0.50'),            (33, 'CTRL_L_mouth_lipsRollU.ty', '1.00')], 'CTRL_L_mouth_lowerLipDepress.ty': [(38,'CTRL_L_mouth_lowerLipDepress.ty','1.00')], 'CTRL_L_mouth_pressD.ty': [(36, 'CTRL_L_mouth_pressD.ty', '1.00')], 'CTRL_L_mouth_pressU.ty': [(36, 'CTRL_L_mouth_pressU.ty', '1.00')], 'CTRL_L_mouth_purseD.ty': [(21, 'CTRL_L_mouth_purseD.ty', '1.00')], 'CTRL_L_mouth_purseU.ty': [(21, 'CTRL_L_mouth_purseU.ty', '1.00')], 'CTRL_L_mouth_stretch.ty': [(30, 'CTRL_L_mouth_stretch.ty', '1.00')], 'CTRL_L_mouth_suckBlow.ty': [(47, 'CTRL_L_mouth_suckBlow.ty', '1.00')], 'CTRL_L_mouth_towardsD.ty': [(21, 'CTRL_L_mouth_towardsD.ty', '0.41')], 'CTRL_L_mouth_towardsU.ty': [(21, 'CTRL_L_mouth_towardsU.ty', '0.41')], 'CTRL_L_mouth_upperLipRaise.ty': [(40,                 'CTRL_L_mouth_upperLipRaise.ty',                 '1.00')], 'CTRL_L_nose.ty': [(50, 'CTRL_L_nose.ty', '1.00')], 'CTRL_R_brow_down.ty': [(43, 'CTRL_R_brow_down.ty', '1.00')], 'CTRL_R_brow_lateral.ty': [(44, 'CTRL_R_brow_lateral.ty', '1.00')], 'CTRL_R_brow_raiseIn.ty': [(44, 'CTRL_R_brow_raiseIn.ty', '1.00'),         (46, 'CTRL_R_brow_raiseIn.ty', '1.00')], 'CTRL_R_brow_raiseOut.ty': [(46, 'CTRL_R_brow_raiseOut.ty', '1.00')], 'CTRL_R_eye.tx': [(11, 'CTRL_R_eye.tx', '1.00'),(12, 'CTRL_R_eye.tx', '-1.00')], 'CTRL_R_eye.ty': [(10, 'CTRL_R_eye.ty', '-1.00'),(13, 'CTRL_R_eye.ty', '1.00')], 'CTRL_R_eye_blink.ty': [(9, 'CTRL_R_eye_blink.ty', '1.00'),      (15, 'CTRL_R_eye_blink.ty', '-1.00')], 'CTRL_R_eye_cheekRaise.ty': [(49, 'CTRL_R_eye_cheekRaise.ty', '1.00')], 'CTRL_R_eye_squintInner.ty': [(14, 'CTRL_R_eye_squintInner.ty', '1.00')], 'CTRL_R_jaw_ChinRaiseD.ty': [(34, 'CTRL_R_jaw_ChinRaiseD.ty', '1.00')], 'CTRL_R_jaw_ChinRaiseU.ty': [(35, 'CTRL_R_jaw_ChinRaiseU.ty', '1.00')], 'CTRL_R_mouth_cornerDepress.ty': [(27,                 'CTRL_R_mouth_cornerDepress.ty',                 '1.00')], 'CTRL_R_mouth_cornerPull.ty': [(25, 'CTRL_R_mouth_cornerPull.ty', '1.00')], 'CTRL_R_mouth_dimple.ty': [(29, 'CTRL_R_mouth_dimple.ty', '1.00')], 'CTRL_R_mouth_funnelD.ty': [(20, 'CTRL_R_mouth_funnelD.ty', '1.00'),          (21, 'CTRL_R_mouth_funnelD.ty', '0.75')], 'CTRL_R_mouth_funnelU.ty': [(20, 'CTRL_R_mouth_funnelU.ty', '1.00'),          (21, 'CTRL_R_mouth_funnelU.ty', '0.75')], 'CTRL_R_mouth_lipsBlow.ty': [(47, 'CTRL_R_mouth_lipsBlow.ty', '1.00')], 'CTRL_R_mouth_lipsRollD.ty': [(32, 'CTRL_R_mouth_lipsRollD.ty', '1.00')], 'CTRL_R_mouth_lipsRollU.ty': [(32, 'CTRL_R_mouth_lipsRollU.ty', '0.50'),            (33, 'CTRL_R_mouth_lipsRollU.ty', '1.00')], 'CTRL_R_mouth_lowerLipDepress.ty': [(39,'CTRL_R_mouth_lowerLipDepress.ty','1.00')], 'CTRL_R_mouth_pressD.ty': [(37, 'CTRL_R_mouth_pressD.ty', '1.00')], 'CTRL_R_mouth_pressU.ty': [(37, 'CTRL_R_mouth_pressU.ty', '1.00')], 'CTRL_R_mouth_purseD.ty': [(21, 'CTRL_R_mouth_purseD.ty', '1.00')], 'CTRL_R_mouth_purseU.ty': [(21, 'CTRL_R_mouth_purseU.ty', '1.00')], 'CTRL_R_mouth_stretch.ty': [(31, 'CTRL_R_mouth_stretch.ty', '1.00')], 'CTRL_R_mouth_suckBlow.ty': [(47, 'CTRL_R_mouth_suckBlow.ty', '1.00')], 'CTRL_R_mouth_towardsD.ty': [(21, 'CTRL_R_mouth_towardsD.ty', '0.41')], 'CTRL_R_mouth_towardsU.ty': [(21, 'CTRL_R_mouth_towardsU.ty', '0.41')], 'CTRL_R_mouth_upperLipRaise.ty': [(41,                 'CTRL_R_mouth_upperLipRaise.ty',                 '1.00')], 'CTRL_R_nose.ty': [(51, 'CTRL_R_nose.ty', '1.00')]}    
#listAttrA=['Key:CTRL_L_nose_wrinkleUpper.ty', 'Key:CTRL_L_mouth_cornerSharpnessU.tx', 'Key:CTRL_L_mouth_cornerSharpnessU.ty', 'Key:CTRL_L_mouth_tightenU.ty', 'Key:CTRL_L_mouth_pressD.ty', 'Key:CTRL_C_jaw_fwdBack.tx', 'Key:CTRL_C_jaw_fwdBack.ty', 'Key:CTRL_R_mouth_lipsTogetherD.ty', 'Key:CTRL_neck_throatUpDown.tx', 'Key:CTRL_neck_throatUpDown.ty', 'Key:CTRL_L_mouth_stickyInnerD.ty', 'Key:CTRL_L_eyelashes_tweakerOut.tx', 'Key:CTRL_L_eyelashes_tweakerOut.ty', 'Key:CTRL_R_mouth_lipsRollU.tx', 'Key:CTRL_R_mouth_lipsRollU.ty', 'Key:CTRL_R_mouth_towardsU.ty', 'Key:CTRL_L_mouth_funnelU.ty', 'Key:CTRL_R_mouth_stickyOuterU.ty', 'Key:CTRL_R_eyelashes_tweakerIn.tx', 'Key:CTRL_R_eyelashes_tweakerIn.ty', 'Key:CTRL_L_brow_lateral.ty', 'Key:CTRL_L_eye_blink.tx', 'Key:CTRL_L_eye_blink.ty', 'Key:CTRL_C_tongue_inOut.tx', 'Key:CTRL_C_tongue_inOut.ty', 'Key:CTRL_L_mouth_corner.tx', 'Key:CTRL_L_mouth_corner.ty', 'Key:CTRL_L_neck_stretch.ty', 'Key:CTRL_L_mouth_lipsRollU.tx', 'Key:CTRL_L_mouth_lipsRollU.ty', 'Key:CTRL_L_brow_raiseIn.ty', 'Key:CTRL_C_eye_parallelLook.ty', 'Key:CTRL_L_mouth_lipsTowardsTeethU.ty', 'Key:CTRL_C_tongue_narrowWide.tx', 'Key:CTRL_C_tongue_narrowWide.ty', 'Key:CTRL_L_mouth_stretchLipsClose.ty', 'Key:CTRL_R_neck_mastoidContract.ty', 'Key:CTRL_L_mouth_cornerPull.ty', 'Key:CTRL_L_mouth_towardsD.ty', 'Key:CTRL_L_eye_pupil.tx', 'Key:CTRL_L_eye_pupil.ty', 'Key:CTRL_R_jaw_chinCompress.ty', 'Key:CTRL_R_ear_up.ty', 'Key:CTRL_L_mouth_towardsU.ty', 'Key:CTRL_R_mouth_lipsTowardsTeethU.ty', 'Key:CTRL_R_jaw_ChinRaiseU.ty', 'Key:CTRL_L_eye_squintInner.ty', 'Key:CTRL_L_mouth_dimple.ty', 'Key:CTRL_C_mouth_stickyD.ty', 'Key:CTRL_C_mouth_lipShiftD.tx', 'Key:CTRL_C_mouth_lipShiftD.ty', 'Key:CTRL_L_mouth_purseD.ty', 'Key:CTRL_C_teeth_fwdBackU.tx', 'Key:CTRL_C_teeth_fwdBackU.ty', 'Key:CTRL_R_nose_nasolabialDeepen.ty', 'Key:CTRL_R_brow_down.ty', 'Key:CTRL_C_tongue_roll.tx', 'Key:CTRL_C_tongue_roll.ty', 'Key:CTRL_L_mouth_pushPullU.tx', 'Key:CTRL_L_mouth_pushPullU.ty', 'Key:CTRL_L_mouth_lowerLipDepress.ty', 'Key:CTRL_R_eye_faceScrunch.ty', 'Key:CTRL_R_brow_raiseIn.ty', 'Key:CTRL_L_mouth_stickyInnerU.ty', 'Key:CTRL_R_mouth_stretch.ty', 'Key:CTRL_R_mouth_lipBiteU.ty', 'Key:CTRL_R_mouth_upperLipRaise.ty', 'Key:CTRL_R_eye_lidPress.ty', 'Key:CTRL_R_mouth_stickyInnerU.ty', 'Key:CTRL_L_mouth_lipBiteU.ty', 'Key:CTRL_R_eyelashes_tweakerOut.tx', 'Key:CTRL_R_eyelashes_tweakerOut.ty', 'Key:CTRL_R_mouth_lipBiteD.ty', 'Key:CTRL_R_jaw_clench.ty', 'Key:CTRL_L_mouth_sharpCornerPull.ty', 'Key:CTRL_R_eye_squintInner.ty', 'Key:CTRL_C_eye.tx', 'Key:CTRL_C_eye.ty', 'Key:CTRL_L_mouth_thicknessD.tx', 'Key:CTRL_L_mouth_thicknessD.ty', 'Key:CTRL_L_eye_cheekRaise.ty', 'Key:CTRL_L_ear_up.ty', 'Key:CTRL_neck_digastricUpDown.tx', 'Key:CTRL_neck_digastricUpDown.ty', 'Key:CTRL_L_mouth_lipsTogetherU.ty', 'Key:CTRL_L_jaw_chinCompress.ty', 'Key:CTRL_R_mouth_suckBlow.tx', 'Key:CTRL_R_mouth_suckBlow.ty', 'Key:CTRL_R_mouth_lipsPressU.ty', 'Key:CTRL_L_mouth_pushPullD.tx', 'Key:CTRL_L_mouth_pushPullD.ty', 'Key:CTRL_L_neck_mastoidContract.ty', 'Key:CTRL_C_teethD.tx', 'Key:CTRL_C_teethD.ty', 'Key:CTRL_R_mouth_pressU.ty', 'Key:CTRL_C_neck_swallow.ty', 'Key:CTRL_C_mouth.tx', 'Key:CTRL_C_mouth.ty', 'Key:CTRL_R_mouth_lipsTogetherU.ty', 'Key:CTRL_R_mouth_thicknessD.tx', 'Key:CTRL_R_mouth_thicknessD.ty', 'Key:CTRL_L_mouth_tightenD.ty', 'Key:CTRL_R_neck_stretch.ty', 'Key:CTRL_L_mouth_lipBiteD.ty', 'Key:CTRL_R_eye_pupil.tx', 'Key:CTRL_R_eye_pupil.ty', 'Key:CTRL_R_mouth_cornerSharpnessD.tx', 'Key:CTRL_R_mouth_cornerSharpnessD.ty', 'Key:CTRL_R_eye_eyelidD.tx', 'Key:CTRL_R_eye_eyelidD.ty', 'Key:CTRL_R_eye.tx', 'Key:CTRL_R_eye.ty', 'Key:CTRL_R_mouth_stretchLipsClose.ty', 'Key:CTRL_R_jaw_ChinRaiseD.ty', 'Key:CTRL_R_mouth_purseU.ty', 'Key:CTRL_L_mouth_lipsPressU.ty', 'Key:CTRL_R_mouth_lipsBlow.ty', 'Key:CTRL_L_mouth_lipSticky.ty', 'Key:CTRL_R_eye_eyelidU.tx', 'Key:CTRL_R_eye_eyelidU.ty', 'Key:CTRL_L_mouth_lipsRollD.tx', 'Key:CTRL_L_mouth_lipsRollD.ty', 'Key:CTRL_L_jaw_ChinRaiseU.ty', 'Key:CTRL_R_mouth_stickyInnerD.ty', 'Key:CTRL_R_mouth_thicknessU.tx', 'Key:CTRL_R_mouth_thicknessU.ty', 'Key:CTRL_R_mouth_tightenD.ty', 'Key:CTRL_R_mouth_purseD.ty', 'Key:CTRL_R_mouth_dimple.ty', 'Key:CTRL_L_mouth_lipsTogetherD.ty', 'Key:CTRL_R_eye_cheekRaise.ty', 'Key:CTRL_R_brow_lateral.ty', 'Key:CTRL_R_nose.tx', 'Key:CTRL_R_nose.ty', 'Key:CTRL_R_mouth_pressD.ty', 'Key:CTRL_L_mouth_stretch.ty', 'Key:CTRL_L_mouth_pressU.ty', 'Key:CTRL_L_mouth_lipsTowardsTeethD.ty', 'Key:CTRL_L_mouth_suckBlow.tx', 'Key:CTRL_L_mouth_suckBlow.ty', 'Key:CTRL_L_mouth_cornerSharpnessD.tx', 'Key:CTRL_L_mouth_cornerSharpnessD.ty', 'Key:CTRL_R_mouth_lipSticky.ty', 'Key:CTRL_neck_throatExhaleInhale.tx', 'Key:CTRL_neck_throatExhaleInhale.ty', 'Key:CTRL_L_mouth_funnelD.ty', 'Key:CTRL_R_eye_blink.tx', 'Key:CTRL_R_eye_blink.ty', 'Key:CTRL_R_mouth_pushPullU.tx', 'Key:CTRL_R_mouth_pushPullU.ty', 'Key:CTRL_R_mouth_lipsTowardsTeethD.ty', 'Key:CTRL_L_jaw_ChinRaiseD.ty', 'Key:CTRL_C_mouth_stickyU.ty', 'Key:CTRL_R_mouth_funnelU.ty', 'Key:CTRL_C_tongue_tip.tx', 'Key:CTRL_C_tongue_tip.ty', 'Key:CTRL_L_nose.tx', 'Key:CTRL_L_nose.ty', 'Key:CTRL_R_mouth_stickyOuterD.ty', 'Key:CTRL_C_mouth_lipShiftU.tx', 'Key:CTRL_C_mouth_lipShiftU.ty', 'Key:CTRL_R_mouth_tightenU.ty', 'Key:CTRL_L_mouth_cornerDepress.ty', 'Key:CTRL_R_nose_wrinkleUpper.ty', 'Key:CTRL_L_jaw_clench.ty', 'Key:CTRL_R_mouth_lipsRollD.tx', 'Key:CTRL_R_mouth_lipsRollD.ty', 'Key:CTRL_L_eyelashes_tweakerIn.tx', 'Key:CTRL_L_eyelashes_tweakerIn.ty', 'Key:CTRL_C_teethU.tx', 'Key:CTRL_C_teethU.ty', 'Key:CTRL_R_mouth_cornerDepress.ty', 'Key:CTRL_L_mouth_upperLipRaise.ty', 'Key:CTRL_L_eye_eyelidD.tx', 'Key:CTRL_L_eye_eyelidD.ty', 'Key:CTRL_R_mouth_corner.tx', 'Key:CTRL_R_mouth_corner.ty', 'Key:CTRL_R_mouth_pushPullD.tx', 'Key:CTRL_R_mouth_pushPullD.ty', 'Key:CTRL_L_mouth_lipsBlow.ty', 'Key:CTRL_L_brow_raiseOut.ty', 'Key:CTRL_L_mouth_stickyOuterU.ty', 'Key:CTRL_C_teeth_fwdBackD.tx', 'Key:CTRL_C_teeth_fwdBackD.ty', 'Key:CTRL_R_mouth_cornerPull.ty', 'Key:CTRL_L_eye_eyelidU.tx', 'Key:CTRL_L_eye_eyelidU.ty', 'Key:CTRL_L_nose_nasolabialDeepen.ty', 'Key:CTRL_C_tongue_press.ty', 'Key:CTRL_L_eye.tx', 'Key:CTRL_L_eye.ty', 'Key:CTRL_R_mouth_funnelD.ty', 'Key:CTRL_R_mouth_towardsD.ty', 'Key:CTRL_L_eye_lidPress.ty', 'Key:CTRL_L_mouth_purseU.ty', 'Key:CTRL_C_jaw_openExtreme.ty', 'Key:CTRL_L_brow_down.ty', 'Key:CTRL_L_mouth_thicknessU.tx', 'Key:CTRL_L_mouth_thicknessU.ty', 'Key:CTRL_R_mouth_cornerSharpnessU.tx', 'Key:CTRL_R_mouth_cornerSharpnessU.ty', 'Key:CTRL_L_eye_faceScrunch.ty', 'Key:CTRL_C_tongue.tx', 'Key:CTRL_C_tongue.ty', 'Key:CTRL_L_mouth_stickyOuterD.ty', 'Key:CTRL_R_mouth_sharpCornerPull.ty', 'Key:CTRL_R_mouth_lowerLipDepress.ty', 'Key:CTRL_C_jaw.tx', 'Key:CTRL_C_jaw.ty', 'Key:CTRL_lookAtSwitch.ty', 'Key:CTRL_R_brow_raiseOut.ty'] 
listAttrA=['CTRL_L_brow_lateral.ty', 'CTRL_R_mouth_purseD.ty', 'CTRL_C_teeth_fwdBackU.tx', 'CTRL_C_teeth_fwdBackU.ty', 'CTRL_L_mouth_pushPullD.tx', 'CTRL_L_mouth_pushPullD.ty', 'CTRL_L_mouth_stickyOuterU.ty', 'CTRL_L_eyelashes_tweakerIn.tx', 'CTRL_L_eyelashes_tweakerIn.ty', 'CTRL_R_mouth_lipsTowardsTeethD.ty', 'CTRL_C_mouth_lipShiftD.tx', 'CTRL_C_mouth_lipShiftD.ty', 'CTRL_C_tongue_inOut.tx', 'CTRL_C_tongue_inOut.ty', 'CTRL_neck_digastricUpDown.tx', 'CTRL_neck_digastricUpDown.ty', 'CTRL_R_ear_up.ty', 'CTRL_L_eyelashes_tweakerOut.tx', 'CTRL_L_eyelashes_tweakerOut.ty', 'CTRL_L_mouth_lipBiteD.ty', 'CTRL_R_brow_raiseOut.ty', 'CTRL_R_eye_blink.tx', 'CTRL_R_eye_blink.ty', 'CTRL_R_mouth_lipsTogetherD.ty', 'CTRL_R_eye_lidPress.ty', 'CTRL_C_tongue_press.ty', 'CTRL_L_mouth_thicknessD.tx', 'CTRL_L_mouth_thicknessD.ty', 'CTRL_R_mouth_pressU.ty', 'CTRL_lookAtSwitch.ty', 'CTRL_R_nose_wrinkleUpper.ty', 'CTRL_L_mouth_pressD.ty', 'CTRL_R_jaw_ChinRaiseU.ty', 'CTRL_L_eye_blink.tx', 'CTRL_L_eye_blink.ty', 'CTRL_L_mouth_upperLipRaise.ty', 'CTRL_L_mouth_stickyInnerU.ty', 'CTRL_L_mouth_lipsRollD.tx', 'CTRL_L_mouth_lipsRollD.ty', 'CTRL_C_jaw.tx', 'CTRL_C_jaw.ty', 'CTRL_L_mouth_funnelU.ty', 'CTRL_R_eye_squintInner.ty', 'CTRL_C_teethU.tx', 'CTRL_C_teethU.ty', 'CTRL_R_neck_stretch.ty', 'CTRL_L_mouth_purseD.ty', 'CTRL_C_jaw_openExtreme.ty', 'CTRL_R_mouth_pushPullU.tx', 'CTRL_R_mouth_pushPullU.ty', 'CTRL_C_mouth_lipShiftU.tx', 'CTRL_C_mouth_lipShiftU.ty', 'CTRL_R_mouth_stretchLipsClose.ty', 'CTRL_R_mouth_thicknessInwardD.tx', 'CTRL_R_mouth_thicknessInwardD.ty', 'CTRL_R_mouth_cornerSharpnessU.tx', 'CTRL_R_mouth_cornerSharpnessU.ty', 'CTRL_R_brow_raiseIn.ty', 'CTRL_L_ear_up.ty', 'CTRL_R_mouth_lipsRollU.tx', 'CTRL_R_mouth_lipsRollU.ty', 'CTRL_R_mouth_upperLipRaise.ty', 'CTRL_L_brow_raiseIn.ty', 'CTRL_L_mouth_lipsTowardsTeethU.ty', 'CTRL_R_mouth_sharpCornerPull.ty', 'CTRL_R_mouth_lipSticky.ty', 'CTRL_L_eye_faceScrunch.ty', 'CTRL_faceGUIfollowHead.ty', 'CTRL_R_mouth_towardsD.ty', 'CTRL_R_mouth_cornerPull.ty', 'CTRL_L_mouth_stickyOuterD.ty', 'CTRL_L_mouth_sharpCornerPull.ty', 'CTRL_R_mouth_thicknessU.tx', 'CTRL_R_mouth_thicknessU.ty', 'CTRL_R_mouth_lipsTogetherU.ty', 'CTRL_L_jaw_chinCompress.ty', 'CTRL_L_mouth_lipsBlow.ty', 'CTRL_R_neck_mastoidContract.ty', 'CTRL_L_mouth_lipBiteU.ty', 'CTRL_C_tongue_roll.ty', 'CTRL_C_eye.tx', 'CTRL_C_eye.ty', 'CTRL_L_mouth_stretch.ty', 'CTRL_R_mouth_lipsTowardsTeethU.ty', 'CTRL_R_eye_pupil.tx', 'CTRL_R_eye_pupil.ty', 'CTRL_C_eye_parallelLook.ty', 'CTRL_L_mouth_towardsD.ty', 'CTRL_R_mouth_purseU.ty', 'CTRL_R_eye_eyelidD.tx', 'CTRL_R_eye_eyelidD.ty', 'CTRL_R_mouth_stickyInnerU.ty', 'CTRL_L_mouth_lipsTogetherU.ty', 'CTRL_L_mouth_cornerSharpnessU.tx', 'CTRL_L_mouth_cornerSharpnessU.ty', 'CTRL_neck_throatUpDown.tx', 'CTRL_neck_throatUpDown.ty', 'CTRL_R_eye_cheekRaise.ty', 'CTRL_R_mouth_pressD.ty', 'CTRL_L_brow_down.ty', 'CTRL_R_mouth_towardsU.ty', 'CTRL_L_mouth_tightenD.ty', 'CTRL_R_mouth_tightenD.ty', 'CTRL_L_eye_lidPress.ty', 'CTRL_R_mouth_cornerDepress.ty', 'CTRL_R_mouth_lipsBlow.ty', 'CTRL_C_neck_swallow.ty', 'CTRL_L_nose_wrinkleUpper.ty', 'CTRL_R_mouth_stickyInnerD.ty', 'CTRL_R_mouth_stretch.ty', 'CTRL_R_mouth_pushPullD.tx', 'CTRL_R_mouth_pushPullD.ty', 'CTRL_R_nose_nasolabialDeepen.ty', 'CTRL_L_mouth_lipsPressU.ty', 'CTRL_R_mouth_thicknessInwardU.tx', 'CTRL_R_mouth_thicknessInwardU.ty', 'CTRL_L_mouth_lipSticky.ty', 'CTRL_R_mouth_funnelU.ty', 'CTRL_C_jaw_fwdBack.tx', 'CTRL_C_jaw_fwdBack.ty', 'CTRL_L_mouth_lowerLipDepress.ty', 'CTRL_R_brow_down.ty', 'CTRL_C_teeth_fwdBackD.tx', 'CTRL_C_teeth_fwdBackD.ty', 'CTRL_R_jaw_ChinRaiseD.ty', 'CTRL_L_eye_squintInner.ty', 'CTRL_R_mouth_funnelD.ty', 'CTRL_L_eye.tx', 'CTRL_L_eye.ty', 'CTRL_L_neck_stretch.ty', 'CTRL_R_mouth_thicknessD.tx', 'CTRL_R_mouth_thicknessD.ty', 'CTRL_C_tongue_tipMove.tx', 'CTRL_C_tongue_tipMove.ty', 'CTRL_L_mouth_stickyInnerD.ty', 'CTRL_R_mouth_dimple.ty', 'CTRL_R_mouth_corner.tx', 'CTRL_R_mouth_corner.ty', 'CTRL_L_eye_eyelidU.tx', 'CTRL_L_eye_eyelidU.ty', 'CTRL_R_brow_lateral.ty', 'CTRL_L_mouth_cornerSharpnessD.tx', 'CTRL_L_mouth_cornerSharpnessD.ty', 'CTRL_L_mouth_tightenU.ty', 'CTRL_L_jaw_clench.ty', 'CTRL_L_mouth_thicknessU.tx', 'CTRL_L_mouth_thicknessU.ty', 'CTRL_R_mouth_suckBlow.tx', 'CTRL_R_mouth_suckBlow.ty', 'CTRL_R_mouth_stickyOuterU.ty', 'CTRL_R_eye.tx', 'CTRL_R_eye.ty', 'CTRL_L_mouth_thicknessInwardU.tx', 'CTRL_L_mouth_thicknessInwardU.ty', 'CTRL_R_jaw_chinCompress.ty', 'CTRL_L_jaw_ChinRaiseD.ty', 'CTRL_C_mouth_stickyD.ty', 'CTRL_R_eye_eyelidU.tx', 'CTRL_R_eye_eyelidU.ty', 'CTRL_L_jaw_ChinRaiseU.ty', 'CTRL_neck_throatExhaleInhale.tx', 'CTRL_neck_throatExhaleInhale.ty', 'CTRL_L_mouth_lipsRollU.tx', 'CTRL_L_mouth_lipsRollU.ty', 'CTRL_L_eye_cheekRaise.ty', 'CTRL_L_mouth_lipsTogetherD.ty', 'CTRL_L_mouth_pushPullU.tx', 'CTRL_L_mouth_pushPullU.ty', 'CTRL_L_mouth_towardsU.ty', 'CTRL_R_mouth_lipsPressU.ty', 'CTRL_C_teethD.tx', 'CTRL_C_teethD.ty', 'CTRL_L_nose_nasolabialDeepen.ty', 'CTRL_C_mouth.tx', 'CTRL_C_mouth.ty', 'CTRL_C_tongue_move.tx', 'CTRL_C_tongue_move.ty', 'CTRL_L_mouth_cornerDepress.ty', 'CTRL_R_jaw_clench.ty', 'CTRL_R_mouth_lipBiteD.ty', 'CTRL_R_mouth_lipsRollD.tx', 'CTRL_R_mouth_lipsRollD.ty', 'CTRL_L_eye_pupil.tx', 'CTRL_L_eye_pupil.ty', 'CTRL_L_mouth_funnelD.ty', 'CTRL_R_eye_faceScrunch.ty', 'CTRL_C_tongue_wideNarrow.tx', 'CTRL_C_tongue_wideNarrow.ty', 'CTRL_R_mouth_lipBiteU.ty', 'CTRL_L_eye_eyelidD.tx', 'CTRL_L_eye_eyelidD.ty', 'CTRL_eyesAimFollowHead.ty', 'CTRL_L_mouth_suckBlow.tx', 'CTRL_L_mouth_suckBlow.ty', 'CTRL_L_mouth_cornerPull.ty', 'CTRL_R_mouth_lowerLipDepress.ty', 'CTRL_L_neck_mastoidContract.ty', 'CTRL_R_eyelashes_tweakerIn.tx', 'CTRL_R_eyelashes_tweakerIn.ty', 'CTRL_L_mouth_pressU.ty', 'CTRL_C_tongue_bendTwist.tx', 'CTRL_C_tongue_bendTwist.ty', 'CTRL_C_mouth_stickyU.ty', 'CTRL_L_nose.tx', 'CTRL_L_nose.ty', 'CTRL_R_mouth_cornerSharpnessD.tx', 'CTRL_R_mouth_cornerSharpnessD.ty', 'CTRL_R_nose.tx', 'CTRL_R_nose.ty', 'CTRL_L_mouth_lipsTowardsTeethD.ty', 'CTRL_R_mouth_stickyOuterD.ty', 'CTRL_L_mouth_stretchLipsClose.ty', 'CTRL_L_mouth_corner.tx', 'CTRL_L_mouth_corner.ty', 'CTRL_L_mouth_purseU.ty', 'CTRL_R_mouth_tightenU.ty', 'CTRL_R_eyelashes_tweakerOut.tx', 'CTRL_R_eyelashes_tweakerOut.ty', 'CTRL_L_brow_raiseOut.ty', 'CTRL_L_mouth_dimple.ty', 'CTRL_L_mouth_thicknessInwardD.tx', 'CTRL_L_mouth_thicknessInwardD.ty', 'CTRL_C_tongue_thickThin.tx', 'CTRL_C_tongue_thickThin.ty']
arkit51listA=["arkit51","EyeBlinkLeft","EyeLookDownLeft","EyeLookinLeft","EyeLookOutLeft","EyeLookUpLeft","EyeSquintLeft","EyewideLeft","EyeBlinkRight","EyeLookDownRight","EyeLookinRight","EyeLookOutRight","EyeLookUpRight","EyeSquintRight","EyewideRight","JawForward","JawLeft","JawRight","JawOpen","MouthFunnel","MouthPucker","MouthLeft","MouthRight","MouthSmileLeft","MouthSmileRight","MouthFrownLeft","MouthFrownRight","MouthDimpleLeft","MouthDimpleRight","MouthStretchLeft","MouthStretchRight","MouthRollLower","MouthRollUpper","MouthShrugLower","MouthShrugUpper","MouthPressLeft","MouthPressRight","MouthLowerDownLeft","MouthLowerDownRight","MouthUpperUpLeft","MouthUpperUpRight","BrowDownLeft","BrowDownRight","BrowinnerUp","BrowOuterUpLeft","BrowOuterUpRight","CheekPuff","CheekSquintLeft","CheekSquintRight","NoseSneerLeft","NoseSneerRight","TongueOut"]
len(arkit51listA)
# ctrl
arkit51_Ctrl=pm.createNode('transform',n='arkit51_Ctrl')
for i in arkit51listA:
    arkit51_Ctrl.addAttr(i,type='float',k=1,min=0.0,max=1.0)
# dic connect
for i in key51_dic.keys():
    addName=(i.replace('.','_') )
    outName=( pm.PyNode( i )  )
    pm.createNode('plusMinusAverage',n=addName) 
    # connect
    if pm.objExists(outName):
        pm.PyNode( addName ).output1D >> pm.PyNode( outName )
        #print (addName,i.replace('Key:',''))
    for j in range(0,len(key51_dic[i])+1):
        #if int(key51_dic[i][j][0])  >=0:
        try:
            #20230712
            arkitblendshapeString=arkit51listA[int(key51_dic[i][j][0])-1]
            # createNode multDoubleLinear
            _MDL=pm.createNode('multDoubleLinear',n=arkitblendshapeString+'_MDL')
            pm.PyNode(_MDL).output >> pm.PyNode(addName+'.input1D[%d]'%j)
            _MDL.input2.set(1)
            driven = pm.PyNode(_MDL+'.input1')
            driver = pm.PyNode('arkit51_Ctrl.'+arkitblendshapeString)
            driven.set(0)
            driver.set(0)
            # Set Driven Key 
            pm.setDrivenKeyframe(driven, cd=driver)
            driver.set(1)
            driven.set(float( key51_dic[i][j][2] ))
            pm.setDrivenKeyframe(driven, cd=driver)
            driver.set(0)
        except Exception:    
            pass  

arkit51_GUI=pm.createNode('transform',n='arkit51_GUI')
posX=0
for i in arkit51listA:
    #print (i)
    text = i  # 생성할 텍스트
    curve_name = i+'_curve'  # 커브 이름
    font = 'Arial'  # 사용할 폰트
    curve = cmds.textCurves( f=font, t=text, n=curve_name) 
    _Grp = pm.createNode('transform',n=curve[0].replace('_curveShape','_Grp'))
    pm.PyNode( curve[0] ).overrideEnabled.set(1)
    pm.PyNode( curve[0] ).overrideDisplayType.set(2)    
    pm.parent( curve[0] , _Grp)
    pm.parent(_Grp , arkit51_GUI)
    _S_Grp= pm.createNode('transform',n=curve[0].replace('_curveShape','_S_Grp'))
    pm.parent(_S_Grp,_Grp)
    _L_curve=pm.curve(n=curve_name.replace('_curve','_L_curve'),p=[(0,0,0),(1,0,0)],d=1)
    _L_curve.overrideEnabled.set(1)
    _L_curve.overrideDisplayType.set(2)  
    _C_curve=pm.circle(n=curve_name.replace('_curve','_CTRL'),r = 0.1 ,ch=0)
    pm.setAttr(_C_curve[0]+'.ty',l=1,k=0,ch=0)
    pm.setAttr(_C_curve[0]+'.tz',l=1,k=0,ch=0)
    pm.setAttr(_C_curve[0]+'.rx',l=1,k=0,ch=0)        
    pm.setAttr(_C_curve[0]+'.ry',l=1,k=0,ch=0)   
    pm.setAttr(_C_curve[0]+'.rz',l=1,k=0,ch=0)           
    pm.setAttr(_C_curve[0]+'.sx',l=1,k=0,ch=0)        
    pm.setAttr(_C_curve[0]+'.sy',l=1,k=0,ch=0)        
    pm.setAttr(_C_curve[0]+'.sz',l=1,k=0,ch=0)                
    pm.setAttr(_C_curve[0]+'.v',l=1,k=0,ch=0)
    #_C_curve[0].tx.setLimits(0.0, 1.0)
    pm.transformLimits( _C_curve[0] ,tx=(0,1))
    pm.transformLimits( _C_curve[0] ,etx=(1,1))
    pm.parent(_C_curve,_S_Grp)
    pm.parent(_L_curve,_S_Grp)
    _S_Grp.s.set(5,5,5) 
    _S_Grp.tx.set(11)
    _Grp.translateY.set(posX)
    posX=posX-2    
    pm.PyNode(_C_curve[0]+'.tx') >>pm.PyNode( arkit51_Ctrl+'.'+i)
pm.parent(arkit51_Ctrl,arkit51_GUI)
arkit51_GUI.t.set(-20,-8,180)
arkit51_GUI.r.set(90,0,0)
arkit51_GUI.s.set(0.33,0.33,0.33)
pm.PyNode('arkit51_S_Grp').v.set(0)