index = 3

# index가 1보다 클 때까지만 수행하는 while문
while index > 1: 
    print("index is %d" % index)
    index = index - 1
print('\n')

idx = 0
while idx < 10:
    idx = idx + 1
    if idx == 5: # idx가 5이면 아래 블록을 건너뛰고 while의 조건문으로 이동
        continue
    if idx == 7: # idx가 7이면 while문 빠져나오기
        break
    if idx % 2 == 0:
        print("{} is even number.".format(idx))
    else:
        print("{} is odd number.".format(idx))
