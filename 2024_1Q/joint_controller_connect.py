import maya.cmds as cmds

class BoneControllerUI:
    def __init__(self):
        self.window_name = "boneControllerWindow"
        self.column_layout = "columnLayout"
        self.bone_list = ["Bone1", "Bone2", "Bone3"]  # Replace with your bone names
        self.controller_list = ["Controller1", "Controller2", "Controller3"]  # Replace with your controller names

    def create_ui(self):
        # Check if the window exists and delete it if it does
        if cmds.window(self.window_name, exists=True):
            cmds.deleteUI(self.window_name, window=True)

        # Create the main window
        cmds.window(self.window_name, title="Bone Controller Connect", widthHeight=(350, 250))

        # Create a column layout for the UI
        cmds.columnLayout(self.column_layout, adjustableColumn=True)

        # Create headers for "Bone" and "Controller" columns
        cmds.rowLayout(numberOfColumns=2, columnWidth2=(150, 150), columnAttach=[(1, 'both', 0), (2, 'both', 0)])
        cmds.text(label="Bone", align="center", font="boldLabelFont")
        cmds.text(label="Controller", align="center", font="boldLabelFont")
        cmds.setParent(self.column_layout)

        # Create rows for each bone and controller pair
        for bone, controller in zip(self.bone_list, self.controller_list):
            cmds.rowLayout(numberOfColumns=2, columnWidth2=(150, 150), columnAttach=[(1, 'both', 0), (2, 'both', 0)])
            cmds.text(label=bone, align="left")
            cmds.text(label=controller, align="left")
            cmds.setParent(self.column_layout)

        # Add button on the right side
        cmds.button(label="Add Bone", command=self.add_bone_button_callback, width=50)

        # Add button on the right side
        cmds.button(label="Add Controller", command=self.add_controller_button_callback, width=50)

        # Connect button at the bottom
        cmds.button(label="Connect", command=self.connect_button_callback)

        # Show the window
        cmds.showWindow(self.window_name)

    # def update_ui(self):
    #     # Clear the existing UI elements
    #     children = cmds.columnLayout(self.column_layout, query=True, childArray=True) or []
    #     for child in children:
    #         cmds.deleteUI(child)

    #     # Recreate the UI with the updated data
    #     # (similar to the code in create_ui method)

    def add_bone_button_callback(self, *args):
        # Get the selected bone
        selected_bone = cmds.ls(selection=True, type="joint")
        if not selected_bone:
            cmds.warning("Please select a bone.")
            return

        # Add the selected bone to the bone_list
        self.bone_list.append(selected_bone[0])

        # Update the UI with the new bone_list
        # self.update_ui()

        print(f"Bone '{selected_bone[0]}' added to the list.")

    def add_controller_button_callback(self, *args):
        # Get the selected controller
        selected_controller = cmds.ls(selection=True, type="transform")
        if not selected_controller:
            cmds.warning("Please select a controller.")
            return

        # Add the selected controller to the controller_list
        self.controller_list.append(selected_controller[0])
        

        print(f"Controller '{selected_controller[0]}' added to the list.")

    def connect_button_callback(self, *args):
        # Add your logic for the "Connect" button here
        print("Connect button clicked")


# Create an instance of the BoneControllerUI class and show the UI
bone_controller_ui = BoneControllerUI()
bone_controller_ui.create_ui()
