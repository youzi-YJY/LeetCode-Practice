def TwoSum(nums,target):
    lens=len(nums)
    j=-1
    for i in range(1,lens):
        #并不是每次都要从nums中查找，这里从前面进行查找。
        temp=nums[:i]
        if (target-nums[i]) in temp:
            j=temp.index(target-nums[i])
            break
    if j>0:
        return [j,i]
    else:
        return []
