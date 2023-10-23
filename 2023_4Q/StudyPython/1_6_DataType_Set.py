# 집합명 = set(요소들)

numSet1 = set([1, 2, 3])
strSet = set('Hello')
print(numSet1)
print(strSet)

# 변수 타입 확인하기
print(type(numSet1))
print('\n')

# 집합 연산
numSet2 = set([3, 4, 5])

print('numSet1과 numSet2의 교집합 : ', numSet1 & numSet2) # 교집합
print('numSet1과 numSet2의 합집합 : ', numSet1 | numSet2) # 합집합
print('numSet1과 numSet2의 차집합 : ', numSet1 - numSet2) # 차집합

# difference를 사용한 차집합
print('numSet1과 numSet2의 차집합(difference) : ', numSet1.difference(numSet2)) 


# 값 1개 추가
numSet1.add(4)
print(numSet1)

# 값 여러 개 추가
numSet1.update([5, 6, 7])
print(numSet1)

# 특정 값 제거
numSet1.remove(5)
print(numSet1)
