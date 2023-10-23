# 기본 if문 사용하기
if 3>2:
    print("3>2 is True")

# if, else 사용하기
numList=[3, 6, 9, 10, 13, 15]
picknum = numList[0]
if picknum < numList[1]:
    print("picknum is smaller than 6")
else:
    print("picknum is larger than 6")
    
# if, elif, else 사용하기
print("pick ten in numList")
picknum = numList[3]
if picknum < numList[2]:
    print("%d is smaller than %d. pick another number." % (picknum,numList[2]))
elif picknum > numList[4]:
    print("%d is larger than %d. pick another number." % (picknum,numList[4]))
elif picknum == 9 or picknum == 13:
    print("pick another number.")
else:
    print("You picked the right number")
