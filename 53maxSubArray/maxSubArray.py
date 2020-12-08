'''
#动态规划
class Solution:
    def maxSubArray(self,nums):
        cur_sum=0
        res=nums[0]
        n=len(nums)
        for i in range(n):
            if (cur_sum>0):
                cur_sum+=nums[i]
            else:
                cur_sum=nums[i]
            res=max(res,cur_sum)
        return res'''
#贪心算法
#每一步选择都是最佳选择，可以在线性时间复杂度内找到数组中的最大值或者最小值以及和的最值的问题。
class Solution:
    def maxSubArray(self,nums):
        cur_sum=max_sum=nums[0]
        n=len(nums)
        for i in range(1,n):
            cur_sum=max(cur_sum+nums[i],nums[i])
            max_sum=max(cur_sum,max_sum)
        return max_sum

