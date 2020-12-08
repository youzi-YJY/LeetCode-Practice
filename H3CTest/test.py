#-*-coding:utf-8 -*-
#字符串压缩
'''
需要注意的点：
1.如果字符出现次数为1，则不加入最后统计结果，需要特殊处理。
2.题目中显示单个字符不能连续重复超过9次，需要特殊处理。
3.为避免出现逻辑错误，给S末尾加入字符，创建临时变量来存储结果。
'''
class Solution:
    def strComparess(self,S):
        #避免S逻辑错误，给S末尾加字符。
        S+=" "
        #设置临时变量，存储数据。
        result=""
        count=1
        n=len(S)
        #开始字符串压缩
        for i in range(1,n):
            if S[i]==S[i-1]:
                #判断一个字符是否连续出现超过了9次。
                if S.count(S[i],i,n)>9:
                    return 0
                else:
                    count+=1
            else:
                #对单个的字符不计数
                if count ==1:
                    result+=S[i-1]
                #超过2的才进行计数
                else:
                    result+=S[i-1]+str(count)
                    #结果统计完成后，将计数变量恢复
                    count=1
        #如果压缩后的长度没有发生变化，则返回原字符串，变短则返回压缩后的字符串。
        return S[:-1] if len(result) >= n-1 else result


#寻找一个整数所有因子里面最中间的那个数
'''
class Solution:
    def findnumber(self,number):
        #1是任何整数的因子
        i=1
        #创建一个临时的空间来存储数据。
        list_ys=[]
        #如果有个数能被这个整数整除，这个数就是该整数的因子。
        while i<=number:
            if number%i==0:
                list_ys.append(i)
            i+=1
        len_of_list=len(list_ys)
        mid=len_of_list//2
        return list_ys[mid]

if __name__=='__main__':
    num=int(input())
    S=Solution()
    print(S.findnumber(num))'''


