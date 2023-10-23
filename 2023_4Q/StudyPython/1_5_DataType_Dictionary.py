# 딕셔너리변수명 = {key1:value1, key2:value2, ...}  Dictionary
student_dict = {'name':'Jinho', 'age':22, 'gender':'male'}
print(student_dict)

# key를 통해 value에 access
print(student_dict['name'])
print(student_dict['age'])
print(student_dict['gender'])

# 변수 타입 확인하기
print(type(student_dict))

# key는 unique한 값이어야 한다. 중복되면 마지막 정보만 남는다.
a = {1:'one', 1:'two'}
print(a)


num_dict = {1:'one', 2:'two', 3:'three'}

# 모든 key값 추출
allkeys = num_dict.keys()
print(allkeys, type(allkeys))

# 모든 value값 추출
allvalues = num_dict.values()
print(allvalues, type(allvalues))

# key, value 쌍 얻기
kv_pairs = num_dict.items()
print(kv_pairs, type(kv_pairs))


# key를 통해 value 얻기
num_dict.get(2) 
print(num_dict.get(2))
print('\n')

# 해당 key가 딕셔너리 안에 있는지 조사
print(1 in num_dict) # 있으면 True
print(4 in num_dict)# 없으면 False
print('\n')

# 딕셔너리의 key, value 모두 제거
num_dict.clear()
print(num_dict)
