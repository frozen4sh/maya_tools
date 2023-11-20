# 문자열 포맷 이용하기
# 문자열 안에서는 %를 사용하여 원하는 변수의 값을 문자열에 포함시킬 수 있다.
str_f1 = "It's %d o'clock" % 3
print(str_f1)

# {} 기호를 이용하면 자료형에 상관없이 삽입이 가능하다.
str_f2 = "From {} AM To {} PM.".format(9, 6)
str_f3 = "From {} AM To {} PM.".format(9, 'Six')
print(str_f2)
print(str_f3)

# 소수점 표현하기
a = 3.141592
str_f4 = "a is {}".format(a)
print(str_f4)
str_f5 = "a is {:0.4f}".format(a) # 소수점 4자리까지 표현
print(str_f5)
str_f6 = "a is %0.3f" %a # 소수점 3자리까지 표현
print(str_f6)

# 문자 개수 세기
str1 = 'Hello'
count_hello = str1.count('l') 
print('Hello에서 l의 개수 : ', count_hello)

# 위치 찾기
find_e = str1.find('e')
index_e = str1.index('e')
print("find 함수로 'Hello'에서 e의 위치 찾기 : ", find_e)
print("index 함수로 'Hello'에서 e의 위치 찾기 : ", index_e)
print('\n')

# 문자열 합치기
hello_list = ['H', 'e', 'l', 'l', 'o'] # 5개의 캐릭터로 이루어진 리스트 변수 선언
print('hello_list : ', hello_list)
join_hello1 = ','.join(hello_list) # hello_list의 요소들 사이에 ',' 구분자를 넣어서 합치기
join_hello2 = ''.join(hello_list) # hello_list의 요소들 사이에 구분자 없이 합치기
print('element 사이에 콤마 넣어서 합치기 : ', join_hello1)
print('element 사이에 구분자 없이 합치기 : ', join_hello2)
print('\n')

# 대소문자 변환
upper_hello = str1.upper()
lower_hello = str1.lower()
print('Hello를 모두 대문자로 전환 : ', upper_hello)
print('Hello를 모두 소문자로 전환 : ', lower_hello)
print('\n')

# 공백 지우기
a = " Hi "
print(a.lstrip())
print(a.rstrip())
print(a.strip())
print('\n')

# 문자열 바꾸기
b = "That is great"
c = b.replace('That', 'Python')
print(c)

# 문자열 나누기
print(b.split(' ')) # 띄어쓰기 기준으로 나누기
print(b.split('a')) # a 기준으로 나누기
