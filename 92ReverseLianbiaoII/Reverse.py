#反转从位置 m 到 n 的链表。请使用一趟扫描完成反转
#1 ≤ m ≤ n ≤ 链表长度
#Definition for singly-linked list
#三指针
class ListNode:
    def __init__(self,x):
        self.val=x
        self.next=None

class Solution:
    def reverseBetween(self,head,m,n):
        dummy=ListNode(-1)
        dummy.next=head
        pre=dummy
        #找到翻转链表部分的前一个节点 1->2->3->4->5->NULL
        for _ in range(m-1):
            pre=pre.next

        #用双指针，进行链表翻转
        node,cur=None,pre.next
        for _ in range(n-m+1):
            tmp=cur.next
            cur.next=node
            node,cur=cur,tmp

        #将翻转的部分和原链表进行拼接
        pre.next.next=cur
        pre.next=node
        return dummy.next