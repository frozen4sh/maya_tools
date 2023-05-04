import os

PATH=0
FILE=1


filePath = cmds.file(q=True, sceneName=True)
splittedPath = os.path.split(filePath)

fullPath = os.path.join(splittedPath[PATH], "babo.txt")
print(fullPath)