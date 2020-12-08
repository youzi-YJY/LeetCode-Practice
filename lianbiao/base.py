# -*- coding: utf-8 -*-
class Node:
    def __init__(self,cargo=None,next=None):
        self.cargo=cargo
        self.next=next

# initilize the node
node1=Node(1)
node2=Node(2)
node3=Node(3)

node1.next=node2
node2.next=node3

#print node
def printNode(node):
    while node:
        print(node)
        node=node.next

def circleNode(node):
    if node==None:
        return None
    circleNode(node.next)
    print(node)

#calculate length of node
class LinkedList:
    def __init__(self,head=None):
        self.head=head
    def len(self):
        curr=self.head
        Counter=0
        while curr is not None:
            Counter+=1
            curr=curr.next
        return Counter

    def insertToFront(self,data):
        if data is None:
            return None
        node=Node(data,self.head)
        self.head=node
        return node

    def append(self,data):
        if data==None:
            return None
        node=Node(data)
        if self.head is None:
            self.head=node
            return node
        curr_node=self.head
        while curr_node.next is not None:
            curr_node=curr_node.next
        curr_node.next=Node
        return node
    def find(self,data):
        if data is None:
            return None
        curr_node=self.head
        while curr_node is not None:
            if curr_node.data==data:
                return curr_node
            curr_node=curr_node.next
        return None
    def deleteAlt(self,data):
        if data is None:
            return
        if self.head is None:
            return
        if self.head.data==data:
            self.head=self.head.next
            return
        curr_node=self.head
        while curr_node.next is not None:
            if curr_node.next.data==data:
                curr_node.next=curr_node.next.next
                return
            curr_node=curr_node.next
        
