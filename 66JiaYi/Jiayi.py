# -*-coding:utf-8 -*-
class Solution:
    def AddOne(self,digits):
        n=len(digits)-1
        #从后往前，依次处理
        for i in range(n,-1,-1):
            #做溢出判断
            if digits[i] is not 9:
                digits[i]+=1
                return digits
            else:
                digits[i]=0
                if digits[0] is 0:
                    digits.insert(0,1)
                    return digits

if __name__=="__main__":
    #dp=[int(n) for n in input().split()]
    dp=list(map(int,input().strip().split()))
    S=Solution()
    print(S.AddOne(dp))