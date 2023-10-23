import sys
sys.version
scriptPath=r'C:\python377\Lib\site-packages'
sys.path.append(scriptPath)
#scriptPath=r'Z:\Private_Folder\kyuseokKim\site-packages'
#sys.path.append(scriptPath)

import numpy as np
from scipy.sparse import lil_matrix, coo_matrix, save_npz

# 희소 행렬 생성 (lil_matrix 형식)
matrix = lil_matrix((5, 5))
matrix[0, 0] = 1
matrix[2, 3] = 2
matrix[4, 1] = 3

# lil_matrix을 coo_matrix로 변환
coo_matrix = coo_matrix(matrix)

# 희소 행렬을 파일로 저장
save_npz("sparse_matrix.npz", coo_matrix)
