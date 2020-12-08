# -*-coding:utf-8 -*-
'''
class ListNode:
    def __init__(self,x):
        self.value=x
        self.next=None
'''

class Solution:
    def returnTokLast(self,head,k):
        fast=head
        slow=head
        while k>0:
            fast=fast.next
            k-=1
        while fast!=None:
            fast=fast.next
            slow=slow.next
        return slow.val
