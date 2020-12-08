class Solution(object):
    def threeSumClosest(self,nums,target):
        nums.sort()
        diff=2147483647
        res=target
        for i in range(len(nums)-2):
            left=i+1
            right=len(nums)-1
            while left<right:
                s=nums[i]+nums[left]+nums[right]
                if s==target:
                    return s
                elif s<target:
                    if target-s<diff:
                        diff=target-s
                        res=s
                    left+=1
                    while left+1<right and nums[left]==nums[left-1]:left+=1
                else:
                    if s-target<diff:
                        diff=s-target
                        res=s
                    right-=1
                    while right-1>left and nums[right]==nums[right+1]:right-=1
        return res