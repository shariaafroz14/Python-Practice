## itrators in python##
l1= [23,65,22,33,76,98,]
it=iter(l1)
while True:
    try:
        print(next(it))
    except StopIteration:
        break