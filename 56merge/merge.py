class Solution:
    def merge(self,nums):
        if not nums:
            return []
        nums.sort()
        res=[nums[0]]
        for x,y in nums[1:]:
            if res[-1][1]<x:
                res.append([x,y])
            else:
                res[-1][1]=max(y,res[-1][1])
        return res