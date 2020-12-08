# -*-coding:utf-8 -*-
import numpy as np
class Sloution:
    def ZuiXiaoLJ(self,list):
        m,n=np.shape(list)
        for i in range(m):
            for j in range(n):
                if i==j==0: continue
                elif i==0: list[i][j]=list[i][j-1]+list[i][j]
                elif j==0: list[i][j]=list[i-1][j]+list[i][j]
                else:list[i][j]=min(list[i-1][j],list[i][j-1])+list[i][j]
        return list[-1][-1]

if __name__=='__main__':
    n=int(input("Please input the number:"))
    Grid=[[0]*n]*n
    for i in range(n):
        Grid[i]=input().split(" ")
        #做整数转换
        Grid[i]=[int(i) for i in Grid[i]]
    S=Sloution()
    print(S.ZuiXiaoLJ(Grid))

'''
Python输入一维数组
方法一：
将输入每个数以空格键隔开做成数组
dp=[int(n) for n in input().split()]
方法二：
dp=list(map(int,input().strip().split()))

Python输入二维数组
Python Split方法：过指定分隔符对字符串进行切片，分隔符，默认为所有的空字符，包括空格、换行(\n)、制表符(\t)等。
Python Strip方法：方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。只能删除开头或者结尾的字符，不能删除中间的。
n=int(input())
line=[[0]*n]*n
for i in range(m):
    将输入每个数以空格键隔开做成数组
    line[i]=input().split(" ")
    #做整数转换
    line[i]=[int(i) for i in line[i]]
print(line)'''

62-66
