# 숫자형 변수의 종류
num1 = 3 # 정수
num2 = 3.45 # 실수
num3 = 3.14e10 # 실수
num4 = 0b1010 # 2진수. 숫자 앞 접두어 0b
num5 = 0o14 # 8진수. 숫자 앞 접두어 0o
num6 = 0x12 # 16진수. 숫자 앞 접두어 0x

# 숫자형 변수 값과 타입을 print함수로 display하여 확인
# 머신러닝에서는 사용하고자 하는 데이터의 변수 타입을 확인하는 것이 매우 중요하다.
# 데이터의 타입은 type() 함수로 확인 가능하다.
print("아래는 숫자형 변수의 값과 타입이다.")  
print("\n") # 줄바꿈
print(num1,'의 자료형은', type(num1))
print(num2,'의 자료형은', type(num2))
print(num3,'의 자료형은', type(num3))
print(num4,'의 자료형은', type(num4))
print(num5,'의 자료형은', type(num5))
print(num6,'의 자료형은', type(num6))

# 숫자형 변수 연산 - 연산에 따른 자료형 변화에 주의
sum1 = num1 + num1 # int + int => int
sum2 = num1 + num2 # int + float => float
sub1 = num1 - num1 # int - int => int
sub2 = num2 - num1 # float - int => float
mul1 = num1 * num1 # int * int => int
mul2 = num1 * num2 # int * float => float
div1 = num1/num1 # int / int => float
div2 = num1/num2 # int / float => float
div3 = num2//num1 # 몫 구하기 연산
div4 = num2%num1 # 나머지 구하기 연산

print("숫자형 변수의 연산에 따른 자료형 변화\n") # 줄바꿈 \n는 뒤에 붙여 쓸 수 있다.
print('3 + 3 = ', sum1, type(sum1))
print('3 + 3.45 = ', sum2, type(sum2))
print('3 - 3 = ', sub1, type(sub1))
print('3.45 - 3 = ', sub2, type(sub2))
print('3 * 3 = ', mul1, type(mul1))
print('3 * 3.45 = ', mul2, type(mul2))
print('3 / 3 = ', div1, type(div1))
print('3 / 3.45 = ', div2, type(div2))
print('3.45 나누기 3의 몫은 ', div3, type(div3))
print('3.45 나누기 3의 나머지는 ', div4, type(div4))
