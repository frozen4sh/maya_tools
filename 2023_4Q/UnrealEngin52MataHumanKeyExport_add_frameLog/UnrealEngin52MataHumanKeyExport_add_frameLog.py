import csv
import pandas as pd
def convert_to_seconds(time_str):
    time_parts = list(map(float, time_str.split(':')))
    hours = time_parts[0] * 3600  # 1시간은 3600초입니다.
    minutes = time_parts[1] * 60  # 1분은 60초입니다.
    seconds = time_parts[2]
    frames = time_parts[3] / 60  # FPS가 60이므로, 각 프레임은 1/60초를 나타냅니다.

    total_seconds = hours + minutes + seconds + frames
    return total_seconds

load_MH_Animator = r"Z:\\DigitalHuman\\rvh\\ml\\yehunHwang\\data\\csv\\MH_Animator_001_51_iPhone.csv"
load_MH_FrameLog = r"Z:\\DigitalHuman\\rvh\\ml\\yehunHwang\\data\\iphone\\20230724_MH_Animator_001_51\\frame_log.csv"
save_Merge_CSV = r"D:\\test\\csv\\20230726\\merged_file.csv"

df1 = pd.read_csv( load_MH_Animator )
csvFilePath = load_MH_FrameLog
df = pd.read_csv(csvFilePath, usecols =[0,1,4], names=['colA', 'colB','colC'], header=None)
df['Seconds'] = df['colC'].apply(convert_to_seconds)
df['Seconds'] = df['Seconds'].apply(lambda x: x - df['Seconds'][0])
list_A=[]
inti=0
for i in df['colA']:
    if i !='D':
        list_A.append(inti)
    inti=inti+1
df_11 = df.drop(list_A, axis = 0)
df_1 = df_11.reset_index(drop=True)
# 두 데이터프레임 병합하기
merged_df = pd.concat([df1, df_1['Seconds']],join='outer',axis=1,ignore_index=False)
merged_dfA=merged_df.drop([len(df_1['colA'])], axis = 0)
# save
merged_dfA.to_csv( save_Merge_CSV , index=False )
