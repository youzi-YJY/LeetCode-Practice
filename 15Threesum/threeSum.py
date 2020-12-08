class Solution(object):
    def threeSum(self,num):
        num.sort()
        res,k=[],0
        for k in range(len(num)-2):
            if num[k]>0:break #beacause of j>i>k
            if k>0 and num[k]==num[k-1]:continue #skip the same 'num[k]'
            i,j=k+1,len(num)-1#双指针设置
            while i<j:#double pointer
                s=num[k]+num[i]+num[j]
                if s<0:
                    i+=1
                    while i<j and num[i]==num[i-1]:i+=1
                elif s>0:
                    j-=1
                    while i<j and num[j]==num[j+1]:j-=1
                else:#s==0
                    res.append([num[k],num[i],num[j]])
                    i+=1
                    j-=1
                    while i<j and num[i]==num[i-1]:i+=1
                    while i<j and num[j]==num[j+1]:j-=1
            return res
