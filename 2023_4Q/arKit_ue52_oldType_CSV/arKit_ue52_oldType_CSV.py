import csv
def oldtypeCSV(opencsv):
    lista = ['Timecode','BlendShapeCount','EyeBlinkLeft','EyeLookDownLeft','EyeLookInLeft','EyeLookOutLeft','EyeLookUpLeft','EyeSquintLeft','EyeWideLeft','EyeBlinkRight','EyeLookDownRight','EyeLookInRight','EyeLookOutRight','EyeLookUpRight','EyeSquintRight','EyeWideRight','JawForward','JawRight','JawLeft','JawOpen','MouthClose','MouthFunnel','MouthPucker','MouthRight','MouthLeft','MouthSmileLeft','MouthSmileRight','MouthFrownLeft','MouthFrownRight','MouthDimpleLeft','MouthDimpleRight','MouthStretchLeft','MouthStretchRight','MouthRollLower','MouthRollUpper','MouthShrugLower','MouthShrugUpper','MouthPressLeft','MouthPressRight','MouthLowerDownLeft','MouthLowerDownRight','MouthUpperUpLeft','MouthUpperUpRight','BrowDownLeft','BrowDownRight','BrowInnerUp','BrowOuterUpLeft','BrowOuterUpRight','CheekPuff','CheekSquintLeft','CheekSquintRight','NoseSneerLeft','NoseSneerRight','TongueOut','HeadYaw','HeadPitch','HeadRoll','LeftEyeYaw','LeftEyePitch','LeftEyeRoll','RightEyeYaw','RightEyePitch','RightEyeRoll']           
    changeNumber=[0,1,9,10,11,12,13,14,15,2,3,4,5,6,7,8,16,17,18,19,20,21,22,23,24,26,25,28,27,30,29,32,31,33,34,35,36,38,37,40,39,42,41,44,43,45,47,46,48,50,49,52,51,53,54,55,56,57,58,59,60,61,62]    
    #파일 열기 
    #opencsv='Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_1\\MH_ARKit_002_1_iPhone_cal.csv'
    #savecsv='Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_1\\MH_ARKit_002_1_iPhone_cal_OLDtype.csv'
    savecsv=opencsv.replace('.csv','_OLDtype.csv')
    writeCSV=[]
    writeCSV.append(lista)
    
    newCSV=[]
    f = open(opencsv,'r')
    rdr = csv.reader(f) 
    for line in rdr:
        newCSV.append(line)
    f.close()
    for i in range(1, len(newCSV)):
        testA=[]
        for j in range(0,63):
            testA.append(newCSV[i][j])
        testB=testA
        for j in range(0,63):
            numberA=changeNumber[j]
            testB[j]=testA[numberA]
        writeCSV.append(testB)
     
    f = open(savecsv,'w', newline='')
    wr = csv.writer(f)
    for i in writeCSV:
        wr.writerow(i) 
    f.close()  
#username='yehunHwang'   
#username='jeewonPark' 
#username='soochulPark'
username='jinwooOh'
username='kyuchulLee'
#usernumber='001'
usernumber='006'
yyyymmdd='20230626'

#print ('Z:\\DigitalHuman\\rvh\\ml\\%s\\data\\iphone\\%s_MH_ARKit_%s_%d\\MH_ARKit_%s_%d_iPhone_cal.csv'%(username,yyyymmdd,usernumber,i,usernumber,i) )
for i in range(1,11):
    oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\%s\\data\\iphone\\%s_MH_ARKit_%s_%d\\MH_ARKit_%s_%d_iPhone_cal.csv'%(username,yyyymmdd,usernumber,i,usernumber,i) )
    oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\%s\\data\\iphone\\%s_MH_ARKit_%s_%d\\MH_ARKit_%s_%d_iPhone_raw.csv'%(username,yyyymmdd,usernumber,i,usernumber,i) )

#1
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_1\\MH_ARKit_002_1_iPhone_cal.csv')
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_1\\MH_ARKit_002_1_iPhone_raw.csv')
#2
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_2\\MH_ARKit_002_2_iPhone_cal.csv')
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_2\\MH_ARKit_002_2_iPhone_raw.csv')
#3
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_3\\MH_ARKit_002_3_iPhone_cal.csv')
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_3\\MH_ARKit_002_3_iPhone_raw.csv')
#4
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_4\\MH_ARKit_002_4_iPhone_cal.csv')
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_4\\MH_ARKit_002_4_iPhone_raw.csv')
#5
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_5\\MH_ARKit_002_5_iPhone_cal.csv')
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_5\\MH_ARKit_002_5_iPhone_raw.csv')
#6
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_6\\MH_ARKit_002_6_iPhone_cal.csv')
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_6\\MH_ARKit_002_6_iPhone_raw.csv')
#7
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_7\\MH_ARKit_002_7_iPhone_cal.csv')
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_7\\MH_ARKit_002_7_iPhone_raw.csv')
#8
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_8\\MH_ARKit_002_8_iPhone_cal.csv')
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_8\\MH_ARKit_002_8_iPhone_raw.csv')
#9
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_9\\MH_ARKit_002_9_iPhone_cal.csv')
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_9\\MH_ARKit_002_9_iPhone_raw.csv')
#10
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_10\\MH_ARKit_002_10_iPhone_cal.csv')
oldtypeCSV('Z:\\DigitalHuman\\rvh\\ml\\kyuseokKim\\data\\iphone\\20230622_MH_ARKit_002_10\\MH_ARKit_002_10_iPhone_raw.csv')
