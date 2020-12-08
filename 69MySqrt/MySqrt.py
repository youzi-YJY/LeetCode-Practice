# -*-coding:utf-8 -*-
'''
Binary_search model
查找区间为：[l,r)
def binary_search(l,r):
    while l<r:
        mid=l+(r-l)//2
        if f(m): #判断找打了没有
            return m
        if g(m):
            r=m #new range(l,m)
        else:
            l=m+1
    retrun l

class Solution:
    def mysqrt(self,x):

        #param x: type int
        #return: int

        left,right=0,x+1
        while left<right:
            mid=left+(right-left)//2
            if mid ** 2 == x:
                return mid
            if mid ** 2 <x:
                left=mid+1
            else:
                right=mid
        return left-1

if __name__=="__main__":
    S=Solution()
    number=int(input())
    print(S.mysqrt(number))'''

'''
Method Two Math function
求f(x)=num-x^2的零点
泰勒级数的一阶展开式：f(x)=f(x0)+(x-x0)f'(x0)
得到
从牛顿法递推公式：X(n+1)=X(n)-f(X(n))/f'(X(n))
带入f'(x)=-2x
得到X(n+1)=(num/X(n)+X(n))/2
到本题为：num=(num+x//num)//2'''

class Solution:
    def mysqrt(self,x):
    
        #param x: int
        #return: int
        
        num=x
        while num*num>x:
            num=(num+x//num)//2
        return num
if __name__=="__main__":
    S=Solution()
    number=int(input())
    print(S.mysqrt(number))

