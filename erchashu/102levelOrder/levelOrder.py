# -*-coding: utf-8 -*-
class TreeNode:
    def __init__(self,root):
        self.root=root
        self.right=None
        self.left=None

class Solution:
    def levelOrder(self,root):
        '''
        1.层序遍历：逐层的从左到右遍历二叉树的节点。
        2.存储每一层的节点值
        3.使用队列：把根节点存入队列->把根节点弹出(出队列+访问节点)->把根节点的左右孩子压入队列
        4.按层输出
        '''
        Quenue=[]
        result=[]
        if not root:
            return result
        Quenue.append(root)
        while Quenue:
            #代表单层的结果
            singelresult=[]
            quenuelength=len(Quenue)
            for i in range(0,quenuelength):
                currentNode=Quenue.pop(0)
                if currentNode.left:
                    Quenue.append(currentNode.left)
                if currentNode.right:
                    Quenue.append(currentNode.right)
                singelresult.append(currentNode.val)
            result.append(singelresult)
        return result
