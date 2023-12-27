import maya.cmds as cmds

def toggle_display_type(obj):
    # Check if the object is a transform or a shape
    if cmds.objectType(obj) == 'transform':
        # If it's a transform, get the shape node
        shapes = cmds.listRelatives(obj, shapes=True)
        if shapes:
            obj = shapes[0]
        else:
            print(f"No shape node found for transform {obj}. Skipping.")
            return

    # Check if the override is already created
    override_exists = cmds.attributeQuery('overrideDisplayType', node=obj, exists=True)

    if not override_exists:
        # Create the override
        cmds.addAttr(obj, longName='overrideDisplayType', attributeType='long', defaultValue=0, hidden=False, keyable=True)

    # Get the current value of overrideDisplayType
    current_value = cmds.getAttr(obj + '.overrideDisplayType')
    print(current_value)

    # Toggle between 0 and 2
    new_value = 2 if current_value == 0 else 0

    # Set the new override value
    cmds.setAttr(obj + '.overrideDisplayType', new_value)
    print(f"{obj}: overrideDisplayType toggled to {new_value}")

# Assuming you have an object selected or specified
selected_objects = cmds.ls(selection=True)

if selected_objects:
    for obj in selected_objects:
        toggle_display_type(obj)
else:
    print("Please select an object.")
