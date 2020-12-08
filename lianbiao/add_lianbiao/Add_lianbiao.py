# -*- coding:utf-8 -*-

#Definition for slingly-linked list
class ListNode:
   def __init__(self,x):
       self.val=x
       self.next=None

class Solution:
    #@param l1:the first list
    #@param l2:the second list
    #@return: the sum list of l1 and l2
    def addLists(self,l1,l2):
        cur1,cur2=l1,l2
        dummy=ListNode(-1)
        pre=dummy
        add1=0
        while cur1 or cur2:
            if cur1 and cur2:
                temp=(cur1.val+cur2.val+add1)
                cur1=cur1.next
                cur2=cur2.next
            elif cur1:
                temp=(cur1.val+add1)
                cur1=cur1.next
            else:
                temp=(cur2.val+add1)
                cur2=cur2.next
            add1=temp//10
            pre.next=ListNode(temp%10)
            pre=pre.next
        if add1==1:
            pre.next=ListNode(1)
        return dummy.next