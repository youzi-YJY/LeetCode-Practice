'''
从链表的任意位置删除也需要考虑以下三种情况：
1.i<=0 使用删除第1项的代码
2.0<i<=n 搜索位于i-1位置的节点，删除其后面的节点
3.i>=n 删除最后一个节点
'''

#Assume that the linked structure has at least one item
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
class Solution:
    def DelateAny(self,position,node,target):
        if position <=0 or node.next is None:
            removeitem=node.data
            return removeitem
        else:
        #Search for node at posiotion position-1 or
        #the next to last position
            prob=node
            while position >1 and prob.next!=None:
                prob=prob.next
                position-=1
            removeitem=prob.next.data
            prob.next=prob.next.next
            return removeitem
