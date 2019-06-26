
#题目：有一个已经排好序的数组。现输入一个数，要求按原来的规律将它插入数组中。

def order():
    numlist = [7, 5, 3, 1]
    #numlist = [1,3,5,7]
    #numlist = [2, 2, 2, 2]
    num = int(input("请输入一个数字"))
    if numlist[0] < numlist[-1]:
        numlist.append(num)
        for i in range(1,len(numlist)):
            for j in range(len(numlist) - i):
                if numlist[j] > numlist[j + 1]:
                    numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
        return numlist
    elif numlist[0] == numlist[-1]:
        numlist.append(num)
        return numlist
    else:
        numlist.append(num)
        for i in range(1, len(numlist)):
            for j in range(len(numlist) - i):
                if numlist[j] < numlist[j + 1]:
                    numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
        return numlist
print(order())



