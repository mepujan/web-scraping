class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        """Returns Boolean True or false based on if the items list is empty or not
        
        The time complexity is O(1) as it takes constant time to check whether the item is present in the list 
        or not
        """
        return not self.items

    def push(self,data):

        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def __repr__(self) -> str:
        return str(self.items)

    def size(self):
        return len(self.items)



if __name__ == "__main__":
    stack = Stack()
    stack.push("apple")
    stack.push("orange")
    print(stack.size())
