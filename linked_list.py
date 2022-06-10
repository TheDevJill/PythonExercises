class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        # make none as default value??
# here we are just putting value(num) to variable(name)
nodeA = Node(6)
nodeB = Node(3)
nodeC = Node(4)
nodeD = Node(2)
nodeE = Node(1)
# to be able to make it a linked list make set it like this:

nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeD
nodeD.next = nodeE

# to make it more convenient/simplify make a class Linkedlist

# heres a function that returns number of nodes

def count_nodes(head):
    count = 1
    current = head
    while current.next is not None:
        current = current.next
        count = count + 1
    return count
