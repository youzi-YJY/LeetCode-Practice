class Solution:
    def search(self,nums,target):
        n=len(nums)
        if n==0:
            return -1
        left=0
        right=n-1
        while left<right:
            mid=left+(right-left)//2
            if nums[mid]==target:
                return mid
            #在左半边
            elif nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            #在右半边
            else:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        #print(left,right)
        return left if nums[left]==target else -1


