# import maya.cmds as cmds


# # show current selected controllers
# selected_objects = []
# right_controllers = []
# left_controllers = []

# selected_objects.clear()
# right_controllers.clear()
# left_controllers.clear()
# selected_objects = cmds.ls(selection=True)
# print(selected_objects)


# # select mirrored right controllers
# for obj in selected_objects:
#     if "_L_" in obj:
#         print("left")
#         right_controllers = [name.replace("_L_", "_R_") for name in selected_objects]
        
        
#     if "_R_" in obj:
#         print("right")
#         left_controllers = [name.replace("_R_", "_L_") for name in selected_objects]
        

# cmds.select(selected_objects, right_controllers, left_controllers)

# import maya.cmds as cmds

# selected_objects = cmds.ls(selection=True)
# print(selected_objects)

# right_controllers = [name.replace("_L_", "_R_") for name in selected_objects if "_L_" in name]
# left_controllers = [name.replace("_R_", "_L_") for name in selected_objects if "_R_" in name]

# cmds.select(selected_objects + right_controllers + left_controllers)


import maya.cmds as cmds

# show current selected controllers
selected_objects = cmds.ls(selection=True)
print(selected_objects)

# select mirrored right controllers
right_controllers = [name.replace("_L_", "_R_") for name in selected_objects if "_L_" in name]
left_controllers = [name.replace("_R_", "_L_") for name in selected_objects if "_R_" in name]

cmds.select(selected_objects, right_controllers, left_controllers)