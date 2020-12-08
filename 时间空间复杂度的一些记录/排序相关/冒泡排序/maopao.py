class Solution:
    def swap(self,nums,p,q):
        tmp=nums[p]
        nums[p]=nums[q]
        nums[q]=tmp

    def bubbleSort(self,nums):
        n=len(nums)
        while n > 1:
            swap=False
            i=1
            while i < n:
                if nums[i] < nums[i-1]:
                    self.swap(nums,i,i-1)
                    swap=True
                i+=1
            if not swap: return
            n-=1
'''
冒泡排序和选择排序很类似，复杂度也是O(n^2)，最好的情况就是列表已经排好序了，不需要进行
交换，最坏的情况也会超线性的。
'''
