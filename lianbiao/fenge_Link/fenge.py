# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def partition(self, head,x):
        # 双链表实现，小于x的组成一链表，大于x的组成另一链表，然后两链表拼接
        if not head:
            return None
        #初始化
        fnode = ListNode(-1)
        snode = ListNode(-1)
        first = fnode
        second = snode
        while head:
            if head.val < x:
                first.next = head
                first = first.next
            else:
                second.next = head
                second = second.next
            #在原始的列表中继续
            head = head.next
        #如果分配正确后，组合成一个列表并返回。
        first.next = snode.next
        #second的最后一个节点修改为节点的结束
        second.next = None

        return fnode.next

if __name__=="__main__":
    S=Solution()
    head=[1,2,2,3,5,2]
    x=3
    print(S.partition(head,x))