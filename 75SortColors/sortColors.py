# -*-coding:utf-8 -*-
#本题是经典的「荷兰国旗问题」，由计算机科学家 Edsger W. Dijkstra 首先提出。
#根据题目中的提示，我们可以统计出数组中 0, 1, 2,0,1,2 的个数，再根据它们的数量，重写整个数组
#不能使用库里的排序函数来解决
class Solution(object):
    def SortColors(self,nums):
        dp=[0]*3
        for i in nums:
            dp[i]+=1
        j=0
        for k in range(3):#元素
            for w in range(dp[k]):#个数
                nums[j]=k
                j+=1

S=Solution()
nums=[2,0,2,1,1,0]
S.SortColors(nums)
print(nums)