import maya.cmds as cmds

def create_ui():
    # Create the main window
    if cmds.window("myWindow", exists=True):
        cmds.deleteUI("myWindow", window=True)
    
    window = cmds.window("myWindow", title="Two Column TextScrollList", widthHeight=(400, 200))

    # Create the main layout with two columns
    main_layout = cmds.rowLayout(numberOfColumns=2, columnWidth2=(200, 200), adjustableColumn=2)

    # Create the first column with a textScrollList
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="Column 1:")
    column1_list = cmds.textScrollList(numberOfRows=8, allowMultiSelection=True, append=["Item 1", "Item 2", "Item 3"])
    cmds.setParent(main_layout)

    # Create the second column with another textScrollList
    cmds.columnLayout(adjustableColumn=True)
    cmds.text(label="Column 2:")
    column2_list = cmds.textScrollList(numberOfRows=8, allowMultiSelection=True, append=["Item A", "Item B", "Item C"])
    cmds.setParent(main_layout)

    # Show the window
    cmds.showWindow(window)

create_ui()
