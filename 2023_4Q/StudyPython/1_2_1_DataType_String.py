# <문자열 변수>
# 문자열 변수를 만드는 방법은 총 4가지가 있다.
str1 = 'Hello'
str2 = "World"
str3 = """Hello World"""
str4 = '''Hello World'''

print('str1 : ', str1)
print('str2 : ', str2)
print('str3 : ', str3)
print('str4 : ', str4)
print(type(str1))

# 문자열 변수를 만드는 방법이 다양한 이유는 문자열 안에 따옴표를 포함시키기 위함이다. 
str5 = 'She said, "Nice to meet you."' # 문자열 안에 큰따옴표 포함시키기
str6 = "He said, \"Nice to meet you too.\"" # 백슬래시를 사용하여 큰따옴표 포함시키기
str7 = "Python's syntax" # 문자열 안에 작은따옴표 포함시키기
str8 = 'Python\'s syntax' # 백슬래시를 사용하여 작은따옴표 포함시키기

print('str5 : ', str5)
print('str6 : ', str6)
print('str7 : ', str7)
print('str8 : ', str8)

# 문자열 연산
strsum1 = str1 + str2
strsum2 = str1 + ' ' + str2 # 두 문자열 변수 사이에 띄어쓰기 넣기
strsum3 = '"' + str1 + ' ' + str2 + '"' # 큰따옴표 추가하기
strsum4 = "Peter\'s friend said, " + '"' + str1 + '"' # 문자열 덧셈 연산 응용하기
strmul1 = str1 * 20 # 문자열 곱하기 연산

print('strsum1 : ', strsum1)
print('strsum2 : ', strsum2)
print('strsum3 : ', strsum3)
print('strsum4 : ', strsum4)
print('strmul1 : ', strmul1)

# 문자열 인덱싱
print("str1의 첫 번째, 두 번째 elements : ", str1[0], str1[1])
print("str1의 뒤에서 첫 번째 element : ", str1[-1]) 
print("str1의 뒤에서 네 번째 element : ", str1[-4]) 

# 문자열의 요소들을 따로 접근하여 출력한 경우,
# 문자열의 요소들 사이에 띄어쓰기가 되어 있음을 알 수 있다.
print("문자열의 요소들을 따로 접근하여 출력 : ", str1[0], str1[1], str1[2], str1[3], str1[4]) 

# 문자열의 요소들을 띄어쓰기 없이 붙여서 출력하고 싶다면 sep을 파라미터로 넣어 주면 된다.
print("띄어쓰기를 제거하여 출력 : ", str1[0], str1[1], str1[2], str1[3], str1[4], sep = '') 


# 문자열 슬라이싱
# 대괄호 안에 시작지점의 인덱스와 끝지점의 인덱스를 넣어 슬라이싱(잘라내기)할 수 있다.
# => 변수[시작번호:끝번호]

print("str1[0:4] : ", str1[0:4])

# 원래대로라면 str1[4]는 5개의 알파벳으로 이루어진 'Hello'에서 마지막 요소인 'o'에 해당하지만
# 출력해 본 결과 'Hell'까지만 출력되는 것을 알 수 있다.
# 이렇듯 슬라이싱에서는 끝번호에 해당하는 요소는 잘라내지 않음에 주의해야 한다.


# 슬라이싱에서의 인덱스는 혼동하기 쉬우므로 아래 슬라이싱 예를 통해 숙지하도록 한다.
print('str1[0:5] : ', str1[0:5])
print('str1[0:-1] : ', str1[0:-1]) # 오른쪽에서 첫 번째 해당하는 요소인 o를 제외한 나머지 가져오기
print('str1[0:] : ', str1[0:])
print('str1[3:4] : ', str1[3:4])
print('str1[3:5] : ', str1[3:5])
print('str1[0:3] + str1[3:5] : ', str1[0:3] + str1[3:5])
print(str1[0:2] + ' ' + str1[2:-1])
