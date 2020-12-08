'''
给定一个二叉树，判断它是否是有效的
1.节点的左子树只包含小于当前节点的数。
2.节点的右子树只包含大于当前节点的数。
3.所有左子树和右子树自身必须也是二叉搜索树
'''
# Definition for a binary tree node.
class TreeNode:
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None
#中序遍历是顺序递增的，我们可以加以利用。
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        res=[]
        def back(treenode):
            if treenode is None:
                return None
            back(treenode.left)
            res.append(treenode.val)
            back(treenode.right)
        back(root)
        return res==sorted(res) and len(set(res))==len(res)

class Solution:
    def isValidBST(self,root):
        self.pre=None
        def isBST(root):
            if not root:
                return True

            if not isBST(root.left):
                return False
            if self.pre and self.pre.val >= root.val:
                return False
            self.pre=root
            return isBST(root.right)
        return isBST(root)