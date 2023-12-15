import maya.cmds as cmds

# Replace 'yourPrefix' with the actual prefix you want to use
prefix = 'CC_'

# Use ls command to get all joints
all_joints = cmds.ls(type='joint')

# Filter joints based on the prefix using a list comprehension
joints_with_prefix = [joint for joint in all_joints if joint.startswith(prefix)]

# Select the joints
cmds.select(joints_with_prefix, replace=True)

# Store the selected joints in a variable
selected_joints = cmds.ls(selection=True)

# Set the range of frames to copy
start_frame = 0
end_frame = 10

# Iterate over the selected joints
for joint in selected_joints:
    # Get the corresponding joint on the other side
    mirrored_joint = joint.replace('_R_', '_L_')
    print (mirrored_joint)

    # Check if there are animation keys on the current joint
    if cmds.keyframe(joint, query=True, keyframeCount=True) > 0:
        # Copy the animation keys from the current joint to the mirrored joint
        cmds.copyKey(joint, time=(start_frame, end_frame))

        # Paste the animation keys onto the mirrored joint
        cmds.pasteKey(mirrored_joint)
    # else:
    #     print("No animation keys found on", joint)

# Set the current time back to frame 1 (or the starting frame of your animation)
cmds.currentTime(0)
