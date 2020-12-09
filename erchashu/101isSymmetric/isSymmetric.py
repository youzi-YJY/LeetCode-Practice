# -*-coding:utf-8 -*-
#判断一个二叉树是否是镜像二叉树
class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

#递归
class Solution:
    def isSymmetric(self,root):
        if not root:
            return True
        def tree(p,q):
            if not p and not q:
                return True
            if p and q and p.val==q.val:
                return tree(p.right,q.left) and tree(p.left,q.right)
            return False
        return tree(root.left,root.right)

#迭代
class Solution:
    def isSymmetric(self,root):
        '''
        1.首先根节点的左右树入栈
        2.根节点左右树出栈，比较两个数是否互为镜像。
        3.若左右节点值相等，将左子树的left，右子树的right。左子树的right，右子树的left入栈。
        4.继续弹出检查，直到检查完所有节点。
        '''
        if not root:
            return True
        def tree(p,q):
            stack=[(p,q)]
            if not stack:
                return True
            while stack:
                #从栈中一次性取出两个节点a,b。
                a,b=stack.pop()
                if not a and not b:
                    continue
                #判断这两个节点，之是否相等，若相等，则按照(left,right)一组，(right,left)一组放入栈中。
                if a and b and a.val == b.val:
                    stack.append((a.left,b.right))
                    stack.append((a.right,b.left))
                #提前遇到不相等的节点返回False
                else:
                    return False
            #检查完所有的节点后返回True.
            return True
        return tree(root.left,root.right)




'''
给定一个数组，检查它是否是镜像堆成的，例如：数组nums=[1,2,2,3,2,2,1]是对称的
利用哈希表来操作的话大概是：
seen=dict()
for i,num in enumerate(nums):
    seen[i]=num
for i,num in enumerate(nums):
    if seen[len(nums)-1-i]!=num:
        return False
return True

而同时遍历的话大概是这样的：
i=0
l=len(nums)-1
while i < l:
    if nums[i]!=nums[r]:return False
    i+=1
    l-=1
return True
'''