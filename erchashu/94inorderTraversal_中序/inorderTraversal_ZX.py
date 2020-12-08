'''
二叉树的遍历顺序
前序遍历：根节点-->左子树-->右子树
中序遍历：左子树-->根节点-->右子树
后序遍历：左子树-->右子树-->根节点
层次遍历：只需按层次遍历即可
二叉树的中序遍历，在遍历时会先访问根节点，然后是左子树，再是右子树，只不过处理节点值是放在访问完左子树之后.
'''

class TreeNode:
    def __init__(self,val=0,left=None,right=None):
        self.val=val
        self.right=right
        self.left=left

#递归的方法
class Solution:
    def inorderTraversal(self,treenode):
        res=[]
        def back(treenode):
            if treenode is None:
                return None
            #中序遍历
            back(treenode.left)
            res.append(treenode.left)
            back(treenode.right)
            '''
            前序遍历
            res.append(treenode.left)
            back(treenode.left)
            back(treenode.right)
            后序遍历
            back(treenode.left)
            back(treenode.right)
            res.append(treenode.left)
            '''
        back(treenode)
        return res

#迭代的方法(中序遍历)
class TreeNode:
    def __init__(self,x):
        self.val=x
        self.right=None
        self.left=None

class Solution:
    def inorderTraversal(self,root):
        res=[]
        stack=[]
        #用p当指针
        p=root
        '''
        (前序遍历)
        res=[]
        if not root:
            return res
        stack=[root]
        while stack:
            node=stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
        return res
        (后序遍历：顺序 从左到右 最后得到的结果取逆)
        res=[]
        if not root:
            return res
        stack=[root]
        while stack:
            node=stack.pop()
            if node.left:
                stack.append(node.val)
            if node.right:
                stack.append(node.val)
            res.append(node.val)
        return res[::-1]
        '''
        #要先不断将它的左子节点压入栈，然后再出栈，带出右子节点入栈
        while p or stack:
            #把左子树压入栈
            while p:
                stack.append(p)
                p=p.left
            #输出栈顶元素
            p=stack.pop()
            res.append(p.val)
            #看右子树
            p=p.right
        return res