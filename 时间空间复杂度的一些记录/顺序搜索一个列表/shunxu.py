class Solution:
    def sequentialSearch(self,target,nums):
        '''
        :param target: target in nums
        :param nums: 数组
        :return: find return index not find return -1
        '''
        position=0
        while position < len(nums):
            if target == nums[position]:
                return position
            position+=1
        return -1
'''
顺序搜索不同于上一个求列表中的最小值
我们需要考虑算法的最好、最差、平均性能
1.最好：目标值在列表的开头，复杂度为O(1).
2.最差：目标值在列表的末尾，或者就不在列表中，对于大小为n的列表需要迭代n次，复杂度为O(n).
3.平均：把在每一个可能的位置找到目标项所需的迭代次数相加，并且除以n.
有(n+n-1+n-2+...+1)/n或(n+1)/2次迭代，总体来看，复杂度仍为O(n).
'''