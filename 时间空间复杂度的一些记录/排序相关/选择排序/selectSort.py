#选择排序
'''
基本思想：
遍历一遍列表，找见列表中的最小项，如果它不在列表的首位，那么就进行交换，
算法回到第二个位置并且重复这个过程，有必要的话，将最小项与第二个位置的项进行交换，
当算法执行到最后一个位置的时候，列表已经排好序了。
'''
class Solution:
    def swap(self,nums,p,q):
        #记录交换
        #profiler.exchange()
        tmp=nums[p]
        nums[p]=nums[q]
        nums[q]=tmp
    def selectSort(self,nums):
        n=len(nums)
        #初始位置
        i=0
        while i < n-1:
            minIndex=i
            #遍历指针
            j=i+1
            while j < n:
                #如果更小则change
                #记录比较
                #profiler.comparision()
                if nums[j] < nums[minIndex]:
                    minIndex=j
                j+=1
                #有需要则进行交换
            if minIndex!=i:
                self.swap(nums,minIndex,i)
            i+=1
'''
对于大小为n的列表来说，外部循环执行1次，内部循环会执行n-1次，外部执行第2次时候，内部循环
会执行n-2次，从而总共会执行(n-1)+(n-2)+....+1=n(n-1)/2，复杂度为O(n^2)
数据交换是在外围循环中执行的，选择排序的额外开销都为线性。
'''


