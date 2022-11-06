num = int(input("Enter a number: "))
if num < 0 :
    for i in range(12,-1,-1):
        print("{} * {} = {}".format(i,num,i*num))
else:
    for i in range(12):
        print("{} * {} = {}".format(i,num,i*num))
