import maya.cmds as cmds


# # Define a list of controller names
# selected_objects = cmds.ls(selection=True)
# print(selected_objects)


# # Use a list comprehension to create a new list that contains only the right-side controller names
# right_controllers = [name.replace("_L_", "_R_") for name in selected_objects]

# # Print the list of right-side controller names
# print(right_controllers)
# cmds.select(right_controllers)




# Define a list of controller names



selected_objects = cmds.ls(selection=True)
print(selected_objects)

for obj in selected_objects:
    if "_L_" in obj:
        print("왼쪽")
        right_controllers = [name.replace("_L_", "_R_") for name in selected_objects]
        cmds.select(selected_objects, right_controllers)


for obj in selected_objects:
    if "_R_" in obj:
        print("오른쪽")
        left_controllers = [name.replace("_R_", "_L_") for name in selected_objects]
        cmds.select(selected_objects, left_controllers)


# # Use a list comprehension to create a new list that contains only the right-side controller names
# right_controllers = [name.replace("_L_", "_R_") for name in selected_objects]

# # Print the list of right-side controller names
# print(right_controllers)
# cmds.select(right_controllers)

