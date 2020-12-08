# -*-coding:utf-8 -*-
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
        if not root:
            return True
        def tree(p,q):
            stack=[(p,q)]
            if not stack:
                return True
            while stack:
                a,b=stack.pop()
                if not a and not b:
                    continue
                if a and b and a.val == b.val:
                    stack.append((a.left,b.right))
                    stack.append((a.right,b.left))
                else:
                    return False
            return True
        return tree(root.left,root.right)