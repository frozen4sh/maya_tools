# 튜플변수명 = (요소1, 요소2, ...)
emptyTuple = ()
numTuple = (1, 2, 3)
strTuple = ('This', 'is', 'a tuple')
print('emptyTuple = ', emptyTuple)
print('numTuple = ', numTuple)
print('strTuple = ', strTuple)
print(type(emptyTuple), '\n') # 변수 타입 확인하기

# 튜플 요소 접근하기 - 리스트와 같이 [index]로 접근 가능
print('numTuple의 2번째 요소 : ', numTuple[1], '\n')

# 리스트와 마찬가지로 튜플에는 어떠한 자료형도 포함 가능하다.
anyTuple = (1, 3.14, 'Python', ['Java', 'C'], (34, 45, 56))
print(anyTuple[0], type(anyTuple[0]))
print(anyTuple[1], type(anyTuple[1]))
print(anyTuple[2], type(anyTuple[2]))
print(anyTuple[3], type(anyTuple[3]))
print(anyTuple[4], type(anyTuple[4]))
print(anyTuple[3][0], type(anyTuple[3][0]))
print(anyTuple[4][1], type(anyTuple[4][1]))
