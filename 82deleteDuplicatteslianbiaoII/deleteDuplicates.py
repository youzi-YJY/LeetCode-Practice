# Definition for singly-linked list.

class ListNode:
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def deleteDuplicates(self,head):
        if head==None or head.next==None:
            return head
        dummy=ListNode(-1000)
        dummy.next=head
        slow=dummy
        fast=dummy.next
        while fast:
            #需要跳过重复的元素
            if fast.next and fast.next.val==fast.val:
                tmp=fast.val
                while fast and tmp==fast.val:
                    fast=fast.next
            #上条件不满足时，进行链表拼接
            else:
                slow.next=fast
                slow=fast
                fast=fast.next
        #fast为空时，进行拼接。
        slow.next=fast
        return dummy.next