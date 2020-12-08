
class Solution:
    def spiralOrder(self,matrix):
        if not matrix:return []
        res=[]
        while matrix:
            res.extend(matrix.pop(0))
            next_matrix=[]
            for x in zip(*matrix):
                next_matrix.append(x)
            matrix=next_matrix[::-1]
        return res