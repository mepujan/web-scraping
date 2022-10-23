import heapq
from multiprocessing import heap
class PriorityQueue:
    def __init__(self,priority = 1) -> None:
        self.items = []
        self.priority = priority

    def put(self,data,priority):
        heapq.heappush(self.items,(data,priority))

    def pop(self):
        return heapq.heappop(self.items)
    
