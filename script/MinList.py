numberList=[12,2,3,23,6,78,33,4]
min=numberList[0]
for num in numberList:
    if min>num:
        min=num
        print(num)