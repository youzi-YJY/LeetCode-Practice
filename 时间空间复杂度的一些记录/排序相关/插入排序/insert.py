'''
如果你按照顺序放好了前i-1张牌，抓取了第i张牌，并且将其与手中的这些牌
进行比较，直到找到其合适的位置。
'''
class Solution:
    def insertSort(self,nums):
        i=1
        while i < len(nums):
            insertTonums=nums[i]
            j=i-1
            while j >=0:
                if insertTonums < nums[j]:
                    #往后推一个
                    nums[j+1]=nums[j]
                    j-=1
                else:
                    break
            #往后推以后，要补上。
            nums[j+1]=insertTonums
            i=+1


'''
列表中排好序的项越多，插入排序的效果越好，最好的情况下是线性的，平均
情况下插入排序的复杂度仍然是二次方阶O(n^2)的。
'''