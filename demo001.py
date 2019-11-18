# coding: utf-8

'''
题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
'''

# 将结果存在列表中
a  = []
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i != j and i != k and j != k:
                b = '%d%d%d'%(i,j,k)
                a.append(int(b))

# 判断列表的长度，得到互不相同三位数的个数
print(len(a))
# 遍历列表中的元素并打印出来
for i in a:
    print(i)