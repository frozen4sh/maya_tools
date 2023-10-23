import maya.cmds as cmds
import pymel.core as pm
def exportFBX():
    a=[ ('CTRL_L_mouth_stretch'),  ('CTRL_R_mouth_suckBlow'),  ('CTRL_L_mouth_suckBlow'),  ('CTRL_R_mouth_stretch'),  ('CTRL_R_mouth_lowerLipDepress'),  ('CTRL_L_mouth_lowerLipDepress'),  ('CTRL_L_mouth_stretchLipsClose'),  ('CTRL_L_mouth_purseU'),  ('CTRL_R_mouth_purseU'),  ('CTRL_R_mouth_stretchLipsClose'),  ('CTRL_R_mouth_purseD'),  ('CTRL_R_mouth_towardsU'),  ('CTRL_L_mouth_purseD'),  ('CTRL_L_mouth_towardsU'),  ('CTRL_R_mouth_funnelU'),  ('CTRL_L_mouth_towardsD'),  ('CTRL_R_mouth_towardsD'),  ('CTRL_L_mouth_funnelU'),  ('CTRL_R_mouth_funnelD'),  ('CTRL_L_mouth_funnelD'),  ('CTRL_R_mouth_lipsTogetherU'),  ('CTRL_L_mouth_lipsTogetherD'),  ('CTRL_R_mouth_lipsTogetherD'),  ('CTRL_L_mouth_lipsTogetherU'),  ('CTRL_R_eye_squintInner'),  ('CTRL_L_eye_cheekRaise'),  ('CTRL_R_eye_cheekRaise'),  ('CTRL_L_eye_squintInner'),  ('CTRL_L_eye_pupil'),  ('CTRL_L_eye_blink'),  ('CTRL_R_eye_blink'),  ('CTRL_C_eye_parallelLook'),  ('CTRL_R_eye_pupil'),  ('CTRL_L_eye_lidPress'),  ('CTRL_R_eye_lidPress'),  ('CTRL_L_nose'),  ('CTRL_L_ear_up'),  ('CTRL_R_ear_up'),  ('CTRL_L_nose_wrinkleUpper'),  ('CTRL_R_nose_wrinkleUpper'),  ('CTRL_R_nose'),  ('CTRL_C_mouth'),  ('CTRL_R_mouth_upperLipRaise'),  ('CTRL_L_mouth_upperLipRaise'),  ('CTRL_R_mouth_sharpCornerPull'),  ('CTRL_L_mouth_sharpCornerPull'),  ('CTRL_L_mouth_cornerPull'),  ('CTRL_R_mouth_dimple'),  ('CTRL_L_mouth_cornerDepress'),  ('CTRL_R_mouth_cornerPull'),  ('CTRL_R_mouth_cornerDepress'),  ('CTRL_L_mouth_dimple'),  ('CTRL_R_mouth_pressU'),  ('CTRL_L_mouth_pressD'),  ('CTRL_L_mouth_pressU'),  ('CTRL_R_mouth_pressD'),  ('CTRL_L_mouth_lipsBlow'),  ('CTRL_R_mouth_lipsBlow'),  ('CTRL_R_mouth_tightenU'),  ('CTRL_L_mouth_lipsPressU'),  ('CTRL_L_mouth_tightenU'),  ('CTRL_R_mouth_tightenD'),  ('CTRL_L_mouth_tightenD'),  ('CTRL_R_mouth_lipsPressU'),  ('CTRL_L_mouth_lipBiteU'),  ('CTRL_R_mouth_lipBiteU'),  ('CTRL_L_mouth_lipBiteD'),  ('CTRL_R_mouth_lipBiteD'),  ('CTRL_R_mouth_stickyOuterU'),  ('CTRL_L_mouth_stickyInnerU'),  ('CTRL_R_mouth_stickyInnerU'),  ('CTRL_L_mouth_stickyOuterU'),  ('CTRL_C_mouth_stickyU'),  ('CTRL_R_mouth_stickyInnerD'),  ('CTRL_C_mouth_stickyD'),  ('CTRL_R_mouth_stickyOuterD'),  ('CTRL_L_mouth_stickyOuterD'),  ('CTRL_L_mouth_stickyInnerD'),  ('CTRL_L_mouth_lipSticky'),  ('CTRL_R_mouth_lipSticky'),  ('CTRL_C_tongue_move'),  ('CTRL_C_tongue_wideNarrow'),  ('CTRL_C_tongue_tipMove'),  ('CTRL_C_tongue_inOut'),  ('CTRL_C_tongue_bendTwist'),  ('CTRL_C_tongue_press'),  ('CTRL_R_jaw_ChinRaiseU'),  ('CTRL_L_jaw_ChinRaiseU'),  ('CTRL_C_tongue_roll'),  ('CTRL_L_jaw_chinCompress'),  ('CTRL_L_jaw_ChinRaiseD'),  ('CTRL_R_jaw_ChinRaiseD'),  ('CTRL_R_jaw_chinCompress'),  ('CTRL_C_jaw'),  ('CTRL_L_jaw_clench'),  ('CTRL_L_neck_stretch'),  ('CTRL_C_jaw_fwdBack'),  ('CTRL_R_jaw_clench'),  ('CTRL_C_jaw_openExtreme'),  ('CTRL_R_neck_mastoidContract'),  ('CTRL_R_neck_stretch'),  ('CTRL_L_neck_mastoidContract'),  ('CTRL_C_neck_swallow'),  ('CTRL_neck_digastricUpDown'),  ('CTRL_neck_throatExhaleInhale'),  ('CTRL_neck_throatUpDown'),  ('CTRL_lookAtSwitch'),  ('CTRL_rigLogicSwitch'),  ('CTRL_L_mouth_pushPullD'),  ('CTRL_L_mouth_pushPullU'),  ('CTRL_R_mouth_pushPullU'),  ('CTRL_R_mouth_cornerSharpnessU'),  ('CTRL_L_mouth_cornerSharpnessD'),  ('CTRL_L_mouth_cornerSharpnessU'),  ('CTRL_R_mouth_pushPullD'),  ('CTRL_R_mouth_cornerSharpnessD'),  ('CTRL_L_mouth_thicknessU'),  ('CTRL_L_mouth_thicknessInwardU'),  ('CTRL_R_mouth_thicknessU'),  ('CTRL_L_mouth_thicknessD'),  ('CTRL_R_mouth_thicknessD'),  ('CTRL_R_mouth_thicknessInwardU'),  ('CTRL_L_mouth_thicknessInwardD'),  ('CTRL_R_mouth_thicknessInwardD'),  ('CTRL_L_mouth_lipsRollU'),  ('CTRL_R_mouth_lipsRollU'),  ('CTRL_L_nose_nasolabialDeepen'),  ('CTRL_L_mouth_lipsRollD'),  ('CTRL_R_mouth_lipsRollD'),  ('CTRL_R_eye_faceScrunch'),  ('CTRL_R_nose_nasolabialDeepen'),  ('CTRL_L_eye_faceScrunch'),  ('CTRL_C_teethU'),  ('CTRL_C_teeth_fwdBackD'),  ('CTRL_C_teeth_fwdBackU'),  ('CTRL_C_teethD'),  ('CTRL_C_mouth_lipShiftU'),  ('CTRL_C_mouth_lipShiftD'),  ('CTRL_L_mouth_lipsTowardsTeethU'),  ('CTRL_L_mouth_lipsTowardsTeethD'),  ('CTRL_R_mouth_lipsTowardsTeethU'),  ('CTRL_R_eyelashes_tweakerIn'),  ('CTRL_R_mouth_lipsTowardsTeethD'),  ('CTRL_L_eyelashes_tweakerIn'),  ('CTRL_C_eyesAim'),  ('CTRL_L_eyeAim'),  ('CTRL_R_eyeAim'),  ('CTRL_convergenceSwitch'),  ('CTRL_L_brow_raiseIn'),  ('CTRL_R_brow_raiseOut'),  ('CTRL_R_brow_raiseIn'),  ('CTRL_L_brow_down'),  ('CTRL_L_brow_raiseOut'),  ('CTRL_R_brow_lateral'),  ('CTRL_L_brow_lateral'),  ('CTRL_R_brow_down'),  ('CTRL_C_eye'),  ('CTRL_L_eye'),  ('CTRL_R_eye'),  ('CTRL_R_eyelashes_tweakerOut'),  ('CTRL_L_mouth_corner'),  ('CTRL_L_eyelashes_tweakerOut'),  ('CTRL_R_mouth_corner'),  ('CTRL_L_eye_eyelidU'),  ('CTRL_L_eye_eyelidD'),  ('CTRL_C_tongue_thickThin'),  ('CTRL_R_eye_eyelidU'),  ('CTRL_R_eye_eyelidD'),  ('CTRL_neckCorrectivesMultiplyerU'),  ('CTRL_neckCorrectivesMultiplyerM'),  ('CTRL_neckCorrectivesMultiplyerD'),  ('CTRL_faceGUIfollowHead'),  ('CTRL_eyesAimFollowHead')] 
    pm.select(cl=1)
    pm.select(a)
    current_file_path = cmds.file(q=True, sceneName=True)
    current_file_pathA=current_file_path.replace(':',':/')
    current_file_pathFBX=current_file_pathA.replace('.mb','fbx')
    end_frame = cmds.playbackOptions(q=True, maxTime=True)
    #pm.mel.eval('bakeResults -simulation true -t "0:{end_frame}" -sampleBy 1 -oversamplingRate 1 -disableImplicitControl true -preserveOutsideKeys true -sparseAnimCurveBake false -removeBakedAttributeFromLayer false -removeBakedAnimFromLayer false -bakeOnOverrideLayer false -minimizeRotation true -controlPoints false -shape true')

    start_frame = 0  # 시작 프레임
    end_frame = end_frame  # 끝 프레임

    # 베이크 옵션을 설정합니다.
    bake_options = {
        "simulation": True,  # 시뮬레이션도 함께 베이크
        "t": (start_frame, end_frame),  # 프레임 범위 설정
        "sampleBy": 1,  # 베이크 샘플 간격
        "disableImplicitControl": True,  # 암시적 컨트롤 비활성화
        "preserveOutsideKeys": True,  # 키프레임 범위 밖의 애니메이션 값 보존
        "sparseAnimCurveBake": False,  # 스파스 애니메이션 곡선 베이크 비활성화
        "removeBakedAttributeFromLayer": False,  # 베이크된 속성 레이어에서 제거하지 않음
        "bakeOnOverrideLayer": False,  # 오버라이드 레이어에서 베이크하지 않음
        "minimizeRotation": True,  # 회전 값을 최소화
        "at": ["translateX", "translateY", "translateZ", "rotateX", "rotateY", "rotateZ"],  # 베이크할 속성 지정
    }
        
    cmds.bakeResults(a, **bake_options)
    cmds.file(current_file_pathFBX, force=True, options="fbx", type="FBX export", pr=True, es=True)

file_list = os.listdir("d:/")    
for file_name in file_list:
    if file_name.find('.mb')!=-1:
        print (file_name)
        cmds.file("d:/"+file_name, open=True, force=True)
        exportFBX()
                     
