# -*- coding: utf-8 -*-
class Solution:
    def mergesort(self,nums1,m,nums2,n):
        if m==0:
            for i in range(n):
                nums1[i]=nums2[i]
        #nums2中的元素作为外循环条件
        for number in nums2:
            for j in range(m):
                #如果2中的元素比1中j位置的小
                if number < nums1[j]:
                    #插入
                    nums1.insert(j,number)
                    #弹出非元素
                    nums1.pop()
                    #元素计数增加
                    m+=1
                    #跳过1中的该元素
                    break
                #如果2中的元素比1中m-1位置的元素大或相等
                if number >= nums1[m-1]:
                    nums1.insert(m,number)
                    nums1.pop()
                    m+=1
                    break

