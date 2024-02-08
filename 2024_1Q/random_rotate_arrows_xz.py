import maya.cmds as cmds
import random

def rotate_selected_controllers_randomlyX(min_angle, max_angle):
    # Get the selected objects
    selected_objects = cmds.ls(selection=True)

    # Check if there are any selected objects
    if not selected_objects:
        print("Please select controllers before running the script.")
        return

    # Iterate through each selected object and rotate randomly
    for obj in selected_objects:
        # Generate random rotation values within the specified range
        random_rotation = [random.uniform(min_angle, max_angle) for _ in range(3)]

        # Apply the random rotation to the selected object
        cmds.rotate(random_rotation[0], random_rotation[1], random_rotation[2], obj, relative=True)

    print("Random rotation applied to selected controllers.")

# Set the range of rotation (in degrees) 아래 수치 조절로 화살 랜덤 각도 조절 10~30
min_rotation = -20.0
max_rotation = 20.0

# Call the function with the specified rotation range
rotate_selected_controllers_randomlyX(min_rotation, max_rotation)


def rotate_selected_controllers_randomlyZ(min_angle, max_angle):
    # Get the selected objects
    selected_objects = cmds.ls(selection=True)

    # Check if there are any selected objects
    if not selected_objects:
        print("Please select controllers before running the script.")
        return

    # Iterate through each selected object and rotate randomly
    for obj in selected_objects:
        # Generate random rotation values within the specified range
        random_rotation = [random.uniform(min_angle, max_angle) for _ in range(3)]

        # Apply the random rotation to the selected object
        cmds.rotate(random_rotation[0], random_rotation[1], random_rotation[2], obj, relative=True)

    print("Random rotation applied to selected controllers.")

# Set the range of rotation (in degrees) 아래 수치 조절로 화살 랜덤 각도 조절 10~30
min_rotation = -20.0
max_rotation = 20.0

# Call the function with the specified rotation range
rotate_selected_controllers_randomlyZ(min_rotation, max_rotation)
