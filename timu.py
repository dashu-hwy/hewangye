#一串字符串（a,b,c)，打印出改字符的所有排序，例如：输入2,3，4，输出243,324,324,423
# a=[2,3,4]  #3个for循环
# for i in a:

# 第一种实现方法
# tar = [2,3,4]
# for i in range(len(tar)):  # 最外层循环，确定百位数字
#     t1 = tar.copy()  # 操作临时变量，防止改变原始tar的值，影响下次循环
#     x = str(t1.pop(i))  # 取出百位数字
#     for j in range(len(t1)):  # 循环剩余列表，确定十位和个位
#         t2 = t1.copy()  # 操作临时变量，防止改变t1的值，影响下次循环
#         y = str(t2.pop(j))  # 取出十位数字
#         for k in range(len(t2)):  # 循环剩余列表，确定个位
#             print(x + y + str(t2[k]), end='  ')  # 将百位十位和个位拼接，得到一个结果（这句还有些不理解）
#     print('')  # 百位相同的结果显示为一行，百位数字改变的时候换行

# 第二种实现方法
# mlist=[1,2,3]
# numlist = [i*100+j*10+k
#            for i in mlist
#            for j in mlist
#            for k in mlist\
#            if i is not j and j is not k and k is not i]
# print(numlist)

# 第三种实现方法
a=[1,2,3]
for i in a:
    for j in a:
        for k in a:
            if i!=j and i!=k and j!=k:
                print (str(i)+str(j)+str(k),end=" ")
    print() #百位相同的结果显示为一行，百位数字改变的时候换行