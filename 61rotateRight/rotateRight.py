# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def rotate(self,node,k):
        if not node or not node.next:
            return node
        num=1
        p=node
        while p.next:
            num+=1
            p=p.next

        #找前一段链表
        k=num-k%num
        p=node
        while k<1:
            p=p.next
            k-=1
        head=p.next
        if not head:
            return head
        #前一段链表最后置空
        p.next=None

        #拼接两个链表
        p=head
        while p.next:
            p=p.next
        p.next=node
        return head

