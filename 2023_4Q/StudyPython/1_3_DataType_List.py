# 리스트변수명 = [요소1, 요소2, ...]
emptyList = []
numList = [1, 2, 3]
strList = ['This', 'is', 'a list']
print('emptyList = ', emptyList)
print('numList = ', numList)
print('strList = ', strList)
print(type(numList), '\n') # 변수 타입 확인하기

# 리스트 요소 접근하기
print('numList의 3번째 요소 : ', numList[2], '\n')

# 리스트 안에는 어떠한 자료형도 포함 가능하다.
anylist = [1, 3.14, 'Python', ['Java', 'C']]
print(anylist[0], type(anylist[0]))
print(anylist[1], type(anylist[1]))
print(anylist[2], type(anylist[2]))
print(anylist[3], type(anylist[3]))
print(anylist[3][0], type(anylist[3][0])) 

# 더하기(+)와 반복하기(*)
sumList = numList + strList
print('sumList = ', sumList)
mulList = numList * 2 
print('mulList = ', mulList)
print('\n')

# 리스트 수정, 삭제
numList2 = [2, 4, 6]
print('numList2 = ', numList2)
numList2[1] = 5 # 두 번째 요소 수정
print('numList2 = ', numList2)
del numList2[1] # 두 번째 요소 삭제
print('numList2 = ', numList2)


# 리스트 길이
# 리스트 길이를 재는 함수 len()은 머신러닝에서 필수적인 함수이므로 꼭 숙지할 것
numList1 = [1, 2, 1, 4, 5]
numList2 = [3, 6, 9]
len(numList1)
print('numList1 = ', numList1, ' 의 길이는 ', len(numList1), '\n')


# 리스트의 요소 개수 
numList1.count(1)
print('numList1에서 1의 개수는 ', numList1.count(1), '\n')

# 리스트 확장 및 요소 추가
# append는 리스트 끝에 인자로 전달된 변수를 그대로 추가한다.
# extend는 인자로 전달된 iterable의 모든 요소를 리스트에 추가한다.
# insert는 인자로 전달된 index의 위치에 요소를 추가한다.
# append, extend, insert 모두 리스트를 확장하는 함수로,
# 혼동하기 쉬우니 아래 예시를 통해 숙지하도록 한다

numList1.append(7) 
print('numList1에 7이 추가됨 => ', numList1)
numList2.append([7, 8])
print('append 함수로 numList2의 끝에 배열 [7, 8]이 통째로 추가됨 => ', numList2)
numList2.extend([7, 8])
print('extend 함수로 numList2의 끝에 배열 [7, 8]의 요소들이 추가됨 => ', numList2)
numList1.insert(0, [7, 8])
print('insert 함수로 numList1의 첫 index에 배열 [7, 8]이 추가됨 => ', numList1)
print('\n')


# 리스트 정렬
# sort함수는 기본적으로 오름차순(reverse=False)이 default이다.
# 내림차순으로 정렬하고 싶다면 reverse=True를 인자로 주면 된다.
numList3 = [3, 10, 1, 100, 34]
numList3.sort()
print('numList3 오름차순 정렬 : ', numList3)
numList3.sort(reverse=True)
print('numList3 내림차순 정렬 : ', numList3)
print('\n')

# 리스트 순서 뒤집기
numList4 = [10, 7, 6, 4, 7, 2, 3]
numList4.reverse()
print('numList4 순서 뒤집기 => ', numList4, '\n')


# 리스트 요소 위치 찾기
numList4[1]
print('numList4의 두 번째 요소 : ', numList4[1])

# 리스트 요소 제거
# del은 함수가 아니라 예약어이므로 'del 리스트[인덱스]'의 형태로 사용한다.
# remove는 리스트에서 첫 번째로 등장하는 요소를 제거한다.

del numList4[0]
print(numList4) 

numList4.remove(7) # 남은 [2, 7, 4, 6, 7, 10]에서 첫 번째로 등장하는 7을 제거
print(numList4)

numList4.remove(7) # 이후 한 번 더 같은 코드를 반복하면 남은 7도 제거됨
print(numList4)
