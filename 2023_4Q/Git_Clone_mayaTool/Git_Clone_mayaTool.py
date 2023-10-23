#Git test 
# Git install
# pip install gitpython
import sys
sys.version
scriptPath=r'C:\python377\Lib\site-packages'
sys.path.append(scriptPath)
scriptPath=r'Z:\Private_Folder\kyuseokKim\site-packages'
sys.path.append(scriptPath)
import os
import shutil
# 삭제할 폴더 경로
folder_to_delete = r"Z:\Private_Folder\kyuseokKim\test_Git"
try:
    # 폴더를 재귀적으로 삭제합니다.
    shutil.rmtree(folder_to_delete)
    print(f"{folder_to_delete} 폴더를 성공적으로 삭제했습니다.")
except Exception as e:
    print(f"폴더 삭제 중 오류가 발생했습니다: {e}") 
    
# 만들고자 하는 폴더 경로
folder_to_create = r"Z:\Private_Folder\kyuseokKim\test_Git"

try:
    # 폴더를 생성합니다.
    os.makedirs(folder_to_create)
    print(f"{folder_to_create} 폴더를 성공적으로 생성했습니다.")
except Exception as e:
    print(f"폴더 생성 중 오류가 발생했습니다: {e}")    
    
          
import git
import os
# 클론할 Git 리포지토리 URL
repository_url = "http://192.168.10.208:30000/kimkyuseok/maya_tools.git"
# 클론할 로컬 디렉토리 경로
local_directory = r"Z:\Private_Folder\kyuseokKim\test_Git"
# 만약 해당 디렉토리가 존재하지 않으면 생성합니다.
if not os.path.exists(local_directory):
    os.makedirs(local_directory)
# Git 리포지토리 클론
repo = git.Repo.clone_from(repository_url, local_directory)
print(f"Git 리포지토리를 {local_directory}에 성공적으로 클론했습니다.")
