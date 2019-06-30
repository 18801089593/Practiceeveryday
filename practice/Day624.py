def sk(a_list,target):
    n = len(a_list)
    for i in range(0,n):
        for j in range(i+1,n):
            if a_list[i] + a_list[j] == target:
                print(i,j)
        exit()
    print("没有相关数据")

a_list = [1,7,11,15,34,98,100,900]
sk(a_list,8)


