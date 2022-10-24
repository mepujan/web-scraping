class Node:

    def __init__(self,data,next = None) -> None:
        self.data = data
        self.next = next

    def get_data(self):
        return self.data
    
    def get_next(self):
        return self.next
    
    def set_data(self,new_data):
        self.data = new_data
    
    def set_next(self,new_next):
        self.next = new_next

    def __str__(self) -> str:
        return str(self.data)

class SLL:
    def __init__(self) -> None:
        self.head = None
    
    def is_empty(self):
        return not self.head

    def add(self,item):
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        count = 0
        current = self.head
        while current is not None:
            count += 1
            current = current.get_next()
        return count

    def search(self,target_item):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == target_item:
                found = True
                break
            current = current.get_next()
        return found

    def remove(self,target_item):
        current = self.head
        previous = None
        found = False

        while current is not None and not found:
            if current.get_data() == target_item:
                found = True
                break
            previous = current
            current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
        return found


# def node_traversal(head):
#     if head is None:
#         return
#     print(head.data)
#     return node_traversal(head.next)

# node1 = Node('apple')
# node2 = Node('banana')
# node3 = Node('orange')

# node1.next = node2
# node2.next = node3
# node3.next = None

# node1 = Node('apple',Node('banana',Node('Orange',None)))

# print(node_traversal(node1))


