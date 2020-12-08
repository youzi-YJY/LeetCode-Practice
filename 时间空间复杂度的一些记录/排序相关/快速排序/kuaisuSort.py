'''
快速排序
1.选择基准点
2.将列表中的项分区
3.分而治之
4.每次遇到少于2个项的一个子列表，就结束
复杂度分析：
1.从二叉搜索的算法中，我们知道，当你居中分割一个列表的时候，大概经过log2n步之后，
会得到一个单个元素，快速排序在最好情况下的性能为O(nlog2n)
2.列表是有序的情况下，尽管没有交换，但是总的分割次数是n-1次，并且执行比较的总次数和
冒泡和选择排序是相同的，在最坏情况下的性能为O(n^2)
内存使用分析：
将快速排序实现为一个递归算法
每一次递归都需要调用一个固定大小的内存用于栈，并且在每一次分割之后有两次递归调用，
在最好的情况下，内存使用时O(log2n)
在最坏情况下，内存使用时O(n)
'''

class Solution:
    def swap(self,nums,p,q):
        tmp=nums[p]
        nums[p]=nums[q]
        nums[q]=tmp

    def partitoion(self,nums,left,right):
        #Find the pivot and exchange it with the last item
        middle = (left+right) //2
        pivot=nums[middle]
        nums[middle]=nums[right]
        nums[right]=pivot
        #Set boundary point to first position
        boundary=left
        #Move items less than pivot to the left
        for index in range(left,right):
            if nums[index] < pivot:
                #小于基准点的项，要和边界之后的第一项进行交换。
                self.swap(nums,index,boundary)
                #边界往后推动
                boundary+=1
        #Exchange the pivot item and the boundary item
        self.swap(nums,right,boundary)
        return boundary
    def quicksortHelper(self,nums,left,right):
        if left < right:
            pivotLocation=self.partition(nums,left,right)
            #每次分割后有两次递归调用
            self.quicksortHelper(nums,left,pivotLocation-1)
            self.quicksortHelper(nums,pivotLocation-1,right)
    def quickSort(self,nums):
        self.quicksortHelper(nums,0,len(nums)-1)
