#-*- coding:utf-8 -*-
#链表没有排序，是随机的
'''
class ListNode:
    def __init__(self,x):
        self.x=x
        self.next=None'''

class Solution:
    def deleteDuplicates(self,head):
        '''
        :param head: ListNode
        :return: After deleteDuplicates ListNode
        '''
        cur=head
        while cur and cur.next:
            if cur.val==cur.next.val:
                cur.next=cur.next.next
        return head

if __name__=="__main__":
    S=Solution()
    head=[1,2,2,1]
    print(S.deleteDuplicates(head))