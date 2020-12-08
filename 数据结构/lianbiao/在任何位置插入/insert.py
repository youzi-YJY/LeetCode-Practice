'''
在链表的任何位置插入需要考虑的是：
1.如果链表为空，那么添加在末尾。
2.如果链表不为空，插入到其中的一个部位。
由于目标索引可能会大于或等于节点的数目，在搜索中，必须小心避免超出链表结构的末尾。
'''
class Node:
    def __init__(self,data):
        self.val=data
        self.next=None

class Solution:
    def insetany(self,node,target,position):
        index=position
        if node is None or index <=0:
            node=Node(target)
        prob=node
        while index >1 and prob.next!=None:
            prob=prob.next
            index-=1
        prob.next=Node(target,prob.next)

