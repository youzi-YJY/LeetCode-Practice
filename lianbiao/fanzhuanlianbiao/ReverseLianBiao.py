# -*- coding: utf-8 -*-
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

#迭代的方法
'''
#双指针
class Solution:
    def reverse(self,heads):
        if not heads:
            return heads
        pre,cur=None,heads
        while cur:
            tmp=cur.next
            cur.next=pre
            pre,cur=cur,tmp
        return pre'''

#递归的方法
class Solution:
    def reverseList(self,head):
        def reverse_lined_list(node,pre):
            if not node:
                return pre
            tmp_node=node.next
            node.next=pre
            return reverse_lined_list(tmp_node,node)

        return reverse_lined_list(head,None)