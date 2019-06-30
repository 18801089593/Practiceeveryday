
#题目：求列表中第二大的元素。

#coding = utf-8


class order():
    numlist = [1, 7, 77,100, 100, 99, 1, 15, 6]
    def order2(self):
        numlist = self.numlist
        for i in range(1, len(numlist)):
            for j in range(len(numlist) - i):
                if numlist[j] > numlist[j + 1]:
                    numlist[j], numlist[j + 1] = numlist[j + 1], numlist[j]
        a = max(numlist)
        b = []
        for i in numlist:
            if i != a:
                b.append(i)
        print(max(b))
a = order()
a.order2()
