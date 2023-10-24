# 기본 for문 수행하기
for i in [1, 3, 5]:
    print(i)
print('\n')

# 두 개 이상의 변수를 활용한 for문
for (food, drink) in [('hamburger', 'coca-cola'), ('sandwitch', 'milk')]:
    print("I like to eat {} with {}".format(food, drink))
print('\n')

# range로 시작 범위와 끝 범위를 직접 지정한 for문
for i in range(2, 5):
    print(i)
print('\n')

# range와 len 함수(길이 구하기 함수)를 사용한 for문
charlist = ['a', 'b', 'c']
for i in range(len(charlist)):
    print(charlist[i])
