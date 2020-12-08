class Solution(object):
    def fourSum(self,nums,target):
        '''
        :param nums: List[int]
        :param target: int
        :return: List[List[int]]
        '''
        nums.sort()
        ans=set()
        for i in range(len(nums)-3):
            for j in range(i+1,len(nums)-2):
                left=j+1
                right=len(nums)-1
                while right>left:
                    temp=nums[i]+nums[j]+nums[left]+nums[right]
                    if temp==target:
                        ans.add((nums[i],nums[j],nums[left],nums[right]))
                        left+=1
                        right-=1
                    if temp>target:right-=1
                    if temp<target:left+=1
        rec=[]
        for i in ans:
            rec.append(list(i))
        return rec
