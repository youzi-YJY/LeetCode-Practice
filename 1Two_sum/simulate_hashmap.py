def TwoSum(nums,target):
    hashmap={}
    #id是下标，num是数值。
    #一个来记录位置
    for i,num in enumerate(nums):
        hashmap[num]=i
    #一个来进行搜索
    for j,num in enumerate(nums):
        k=hashmap.get(target-num)#获取对应值的键
        if k is not None and j!=k:
            return [j,k]
