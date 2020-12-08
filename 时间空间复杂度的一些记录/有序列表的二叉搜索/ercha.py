class Solution:
    def binarySearch(self,target,sortednums):
        '''
        :param target: taret in or not in sortednums
        :param sortednums:
        :return: taget_index
        '''
        left=0
        right=len(sortednums)-1
        while left < right:
            mid=(left+right)//2
            if target == sortednums[mid]:
                return mid
            elif target > sortednums[mid]:
                left=mid+1
            else:
                right=mid-1
        return -1
'''
二分法搜索会牺牲列表的一个整体性，需要列表是有序的。
在上面的算法中，我们考虑最坏的情况，目标值不在列表中，
最坏情况下，循环执行的次数等于列表的大小除以2知道结果为1，
也就是求得K，使得n/2^k=1，那么n=2^k，也就是k=log2n
从而二叉搜索的最坏情况复杂度为O(log2n)
选择何种搜索算法，取决于列表中的数据的组织方式。
'''