#迭代
class Solution:
    def subsetsWithDup(self, nums):
        if not nums:
            return nums
        nums.sort()
        #最后的一个统计结果
        res=[[]]
        #中间临时的统计结果
        cur=[]
        for i in range(len(nums)):
            if i >0 and nums[i-1]==nums[i]:
                cur=[tmp+[nums[i]] for tmp in cur]
            else:
                cur=[tmp+[nums[i]] for tmp in res]
            res+=cur
        return res

#[]+[1]=[1] [1]+[2]=[1,2] [1,2]+[2]=[1,2,2]
#[[]]+[[1]]=[[],[1]] [[1,2]]+[[2]]=[[1,2],[2]]
S=Solution()
nums=[1,1,2]
print(S.subsetsWithDup(nums))

'''
#回溯
class Solution:
    def subsetWithDup(self,nums):
        if not nums:
            return nums
        nums.sort()
        n=len(nums)
        res=[]
        def helper(index,cur_res):
            res.append(cur_res)
            for i in range(index,n):
                if i > index and nums[i]==nums[i-1]:
                    continue
                helper(i+1,cur_res+[nums[i]])
        helper(0,[])
        return res

S=Solution()
nums=[1,2,2]
print(S.subsetWithDup(nums))'''