# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left
'''
不失一般性，有以下两步，我们选取3为根节点。
1.利用二叉树的搜索性质，比根节点小的值都在根节点的左边，比根节点大的值都在根节点的右边。
2.左边就变成{1,2}组成的二叉树，右边就是{4}。
'''
#+采用回溯的方法
import functools
class Solution:
    def generate(self,n):
        if n==0 : return []
        #lru_cache主要是用来做缓存，把相对耗时的函数结果进行保存
        #避免传入相同的参数重复计算
        #缓存不会无限增长，不用的缓存会被释放
        @functools.lru_cache(None)
        def helper(start,end):
            res=[]
            if start > end:
                res.append(None)
            #这里找根节点 取遍 [start,end]中的节点
            for val in range(start,end+1):
                #寻找左子树，注意左边的范围设置。
                for left in helper(start,val-1):
                    #寻找右子树，同样注意右边的范围设置。
                    for right in helper(val+1,end):
                        root=TreeNode(val)
                        root.left=left
                        root.right=right
                        #保存一种{左子树|根节点|右子树}组合
                        res.append(root)
            return res
        return helper(1,n)
