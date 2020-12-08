# -*-coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return None
        FirstNode = ListNode(-1)
        SecondNode = ListNode(-1)
        #前半段
        Fist = FirstNode
        #后半段
        Second = SecondNode
        while head:
            #小于x的放置在前半段
            if x > head.val:
                Fist.next = head
                Fist = Fist.next
            #大于x的放置在后半段
            else:
                Second.next = head
                Second = Second.next
            #内部循环
            head = head.next

        #放置正确的话，进行拼接.
        Fist.next = SecondNode.next
        Second.next = None
        return FirstNode.next
