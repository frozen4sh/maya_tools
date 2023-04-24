import glob
import numpy as np
import os
import generalVals as g


projDir = g.projDir
g.CreateFolder(g.Dirs.dataSet)

train_data = []
val_data = []
train_label_var = []
val_label_var = []

# data_list = [['1_01','1_02','2_02','2_03','2_04'],
#             ['1_01','1_02','2_02','2_03','2_04','3_15','3_16'],
#             ['1_01','1_02','2_02','2_03','2_04'],
#             ['1_01','1_02','2_02','2_03','2_04','3_15','3_16'],
#             ['1_01','1_02','2_01','2_02','2_03','2_04']]


lpcNpy = g.GetPath(g.Dirs.lpc)
ctrlNpy = g.GetPath(g.Dirs.npy)


#### 파일 리스트 여기서 받아와서

lpcDataPath = [f for f in glob.glob(os.path.join(lpcNpy, "*.npy"))]
ctrlDataPath = [f for f in glob.glob(os.path.join(ctrlNpy, "*Value.npy"))]
ctrlNameDataPath = [f for f in glob.glob(os.path.join(ctrlNpy, "*Name.npy"))]

#### 여기부터 looping 시키면 됨
lpcData = np.load(lpcDataPath[0])
ctrlData = np.load(ctrlDataPath[0])
ctrlNames = np.load(ctrlNameDataPath[0])

data = np.zeros((1,32,64,1))
label = np.zeros((1, len(ctrlNames)))

data = np.vstack((data, lpcData))
label = np.vstack((label, ctrlData))

data = data[1:]
label = label[1:]

train_data.extend(data)
val_data.extend(data[-1000:])
train_label_var.extend(label[:,])
val_label_var.extend(label[-1000:,])

#####

print(np.array(train_data).shape)
print(np.array(val_data).shape)
print(np.array(train_label_var).shape)
print(np.array(val_label_var).shape)

g.CreateFolder(g.Dirs.dataSet)


np.save(g.GetPath(g.Dirs.dataSet, 'train_data.npy'), np.array(train_data).astype(np.float))
np.save(g.GetPath(g.Dirs.dataSet, 'val_data.npy'), np.array(val_data).astype(np.float))
np.save(g.GetPath(g.Dirs.dataSet, 'train_label_var.npy'), np.array(train_label_var).astype(np.float))
np.save(g.GetPath(g.Dirs.dataSet, 'val_label_var.npy'), np.array(val_label_var).astype(np.float))


