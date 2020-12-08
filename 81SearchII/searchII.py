class Solution:
    def search(self,nums,target):
        n=len(nums)
        left=0
        right=n-1
        while left <= right:
            mid=left+(right-left)//2
            if target==nums[mid]:
                return True
            #重复的情况
            if nums[left]==nums[mid]==nums[right]:
                left+=1
                right-=1
            elif nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]< target <=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return False
