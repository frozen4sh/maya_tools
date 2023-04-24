import numpy as np
import os
import csv
import generalVals as g

dir = g.projDir
print (dir)
file_list = os.listdir(dir)
for file_name in file_list:
    if file_name.endswith('.csv'):
        nameFile=(file_name.replace('.csv',''))
        f = open(os.path.join(dir, file_name), "r")
        rdr = csv.reader(f)
        data = list(rdr)
        ctrlName = data[0][1:]
        DataMap = []
        for i in data[1:]:
            DataMap.append(i[1:])
        print(DataMap[0])
        g.CreateFolder(g.Dirs.npy)
        names = g.GetPath(g.Dirs.npy, nameFile+'ctrlName.npy')
        maps = g.GetPath(g.Dirs.npy, nameFile+'ctrlValue.npy')
        np.save(names, ctrlName)
        np.save(maps, DataMap)

