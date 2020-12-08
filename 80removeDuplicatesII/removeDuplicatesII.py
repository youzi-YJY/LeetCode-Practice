#给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素最多出现两次，返回移除后数组的新长度。
def removeDuplicates(nums) -> int:
    l = len(nums)
    if l <= 2:
        return l
    #双指针：索引指针&位置指针
    i = 2 # 指向当前要拷贝覆盖的索引位置
    for j in range(2, len(nums)):
        #覆盖规则是，等不同则覆盖，相同则暂停更新索引指针但更新位置指针。
        if nums[j] != nums[i - 2]:
            nums[i] = nums[j]
            i += 1 # 指向下一个要覆盖的索引位置
    return i

