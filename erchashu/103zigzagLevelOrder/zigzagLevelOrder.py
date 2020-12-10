''''
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        cur = [root]
        sign = False   # 设置反转标识
        while cur:
            curr_res = []
            next_node_list = []
            for node in cur:
                if node:
                    curr_res.append(node.val)
                    next_node_list.extend([node.left, node.right])

            if curr_res:
                if sign:
                    curr_res=curr_res[::-1]   #将结果反转，如果为从右到左。
                res.append(curr_res)
            cur = next_node_list
            sign = False if sign else True

        return res'''
class TreeNode:
    def __init__(self,root):
        self.root=root
        self.right=None
        self.left=None

class Solution:
    def zigzagLevelOrder(self,root):
        Quenue=[]
        result=[]
        boolOrder=False
        if not root:
            return result
        Quenue.apppend(root)
        while Quenue:
            singelResult=[]
            length=len(Quenue)
            for i in range(0,length):
                currentNode=Quenue.pop(0)
                if currentNode.left:
                    Quenue.append(currentNode.left)
                if currentNode.right:
                    Quenue.append(currentNode.right)
                singelResult.append(currentNode.val)
            if singelResult:
                if boolOrder:
                    singelResult=singelResult[::-1]
                    result.append(singelResult)
                else:
                    result.append(singelResult)
            boolOrder=False if singelResult else True
        return result