# -*-coding:utf-8 -*-
#递归
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left


class Solution:
    def isSameTree(self,treeNode1,treeNode2):
        if not treeNode1 and not treeNode2:
            return True
        if treeNode1 and treeNode2 and treeNode1.val == treeNode2.val:
            return self.isSameTree(treeNode1.left,treeNode2.left) and self.isSameTree(treeNode1.right,treeNode2.right)
        return False

#迭代
class Solution:
    def isSameTree(self,treenode1,treenode2):
        stack=[(treenode2,treenode1)]
        while stack:
            a,b=stack.pop()
            if not a and not b:
                continue
            if a and b and a.val==b.val:
                #栈，后入先出
                stack.append((a.left,b.left))
                stack.append((a.right,b.right))
            else:
                return False
        return True