class Node(object):
    def __init__(self,data,next=None):
        self.data=data
        self.next=next

class TwoNode(Node):
    def __init__(self,data,previous=None,next=None):
        Node.__init__(self,data,next)
        self.previous=previous

'''
from node import TwoNode

#Create a doubly linked structure with one node

head=TwoNode(1)
tail=head

for data in range(2,6):
    tail.next=TwoNode(data,tail)
    tail=tail.next

prob=tail
while prob!=None:
    print(prob.data)
    prob=prob.previous

新节点的previous指针必须指向当前的尾节点，通过将tail当做该节点的构造方法的第二个参数传递
当前尾节点的next指针必须指向新节点
tail指针必须指向新的节点
'''