def TwoSum(nums,target):
    lens=len(nums)
    j=-1
    for i in range(lens):
        if (target-nums[i]) in nums:
            #判断是否是自己
            if (nums.count(target-nums)==1) & (target-nums[i]==nums[i]):
                continue
            #不是的话进行搜索操作
            else:
                j=nums.index(target-nums[i],i+1)
                break
    if j>0:
        return [i,j]
    else:
        return []