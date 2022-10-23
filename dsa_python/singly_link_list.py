class Node:

    def __init__(self,data,next = None) -> None:
        self.data = data
        self.next = next

    def add_front(self,data):
        self.data = data

    def __str__(self) -> str:
        return str(self.data)

def node_traversal(head):
    if head is None:
        return
    print(head.data)
    return node_traversal(head.next)

# node1 = Node('apple')
# node2 = Node('banana')
# node3 = Node('orange')

# node1.next = node2
# node2.next = node3
# node3.next = None

node1 = Node('apple',Node('banana',Node('Orange',None)))

print(node_traversal(node1))


