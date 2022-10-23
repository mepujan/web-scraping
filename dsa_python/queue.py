from collections import deque

class Queue:
    def __init__(self) -> None:
        self.items = deque()

    
    def is_empty(self):
        return not self.items

    def enqueue(self,data):
        self.items.appendleft(data)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self) -> str:
        return str(self.items)