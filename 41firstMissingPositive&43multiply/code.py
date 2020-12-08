'''
#Solution 1
class Solution:
    def firstMissingPositive(self,nums):
        n=len(nums)
        for i in range(n):
            while 1<=nums[i] and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        i=0
        while i<n and i+1==nums[i]:
            i+=1
        return i+1

#Solution 2
class Solution:
    def firstMissingPositive(self,nums):
        n=len(nums)
        for i in range(n):
            while 1<=nums[i]<=n and nums[i]!=nums[nums[i]-1]:
                self.__swap(nums,i,nums[i]-1)
        for i in range(n):
            if i+1!=nums[i]:
                return i+1
        return n+1

    def __swap(self,nums,index1,index2):
        nums[index1],nums[index2]=nums[index2],nums[index1]'''