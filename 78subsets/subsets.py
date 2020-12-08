#-*-coding:utf-8 -*-
'''
class Solution:
    def SubSet(self,nums):
        n=len(nums)
        res=[]
        def backtrack(index,cur_res):
            res.append(cur_res)
            for i in range(index,n):
                backtrack(i+1,cur_res+[nums[i]])
        backtrack(0,[])
        return res

S=Solution()
nums=[1,2,3]
print(S.SubSet(nums))'''

#迭代
class Solution:
    def SubSet(self,nums):
        res=[[]]
        for i in nums:
            res=res+[[i]+num for num in res]
        return res