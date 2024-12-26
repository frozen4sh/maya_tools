import maya.cmds as cmds

# Get the list of selected objects
selected_objects = cmds.ls(selection=True)

# Loop through the selected objects
for obj in selected_objects:
    # Check if the object name starts with 'CC_Base_'
    if obj.startswith("CC_Base_"):
        # Extract the part after 'CC_Base_' (remove 'CC_Base_' from the name)
        new_value = obj.replace("CC_Base_", "")
        
        # Set the attribute for this object
        cmds.setAttr(f"{obj}.type", 18)
        cmds.setAttr(f"{obj}.otherType", new_value, type="string")
