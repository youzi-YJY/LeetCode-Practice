'''
归并排序 突破O(n^2)的障碍
如下是一个简单描述：
1.计算一个列表的中间位置，并且递归第排序其左边和右边的子列表(分而治之)
2.将两个排好序的子列表重新合并为单个排好序的列表
3.当子列表不能够再划分的时候，停止这个过程
三个函数在这个顶层设计策略中协作
mergeSort 用户调用的函数
mergeSortHelper 一个辅助函数 它隐藏了递归调用所需要的额外参数
Merge 实现合并过程的一个函数
'''

import numpy as np
class Solution:
    def mergeSort(self,nums):
        '''
        :param nums: list being sorted
        :return:
        '''
        copyBuffer=np.array(len(nums))
        self.mergeSortHelper(nums,copyBuffer,0,len(nums)-1)

    def mergeSortHelper(self,nums,copyBuffer,low,high):
        if low < high:
            middle=(low+high)//2
            self.mergeSortHelper(nums,copyBuffer,low,middle)
            self.mergeSortHelper(nums,copyBuffer,middle+1,high)
            self.merge(nums,copyBuffer,low,middle,high)

    def merge(self,nums,copyBuffer,low,middle,high):
        '''
        :param nums: list that is being sorted
        :param copyBuffer: temp space needed during the merge process
        :param low:begining of first sorted sublist
        :param middle:end of first sorted sublist
        :param high:end of second sorted sublist
        middle+1: begining of second sorted sublist
        '''
        i1=low
        i2=middle+1

        for i in range(low,high+1):
            if i1 > middle:
                copyBuffer[i]=nums[i2]
                i2+=1
            elif i2 > middle:
                copyBuffer[i]=nums[i1]
                i1+=1
            elif nums[i1] < nums[i2]:
                copyBuffer[i]=nums[i1]
                i1+=1
            else:
                copyBuffer[i]=nums[i2]
                i2+=1
        #copy sorted items back to proper position in nums
        for i in range(low,high+1):
            nums[i]=copyBuffer[i]

'''
合并排序运行时间由两条for语句主导
在一个层所有合并花费的时间是O(n),mergeSortHelper在每一层都是尽可能平均地分割
子列表，层级数是O(logn)
在所有情况下，最大运行时间是O(nlogn)
空间方面：
支持递归调用的调用栈上，需要O(logn)
复制缓存需要使用O(n)的空间
'''