"""
Python Data Structures - A Game-Based Approach
Priority Queue Class based on heapq.
Robin Andrews - https://compucademy.net/
"""

import heapq


class PriorityQueue:
    
    def __init__(self):

        self.elements = []

    def is_empty(self):

        return not self.elements

    def put(self, item, priority):

        heapq.heappush(self.elements, (priority, item))

    def get(self):

        # index 1 to get the value, not the priority
        return heapq.heappop(self.elements)[1]

    def __str__(self):
        return str(self.elements)

if __name__ == "__main__":
    pq = PriorityQueue()
    print(pq.is_empty())
    pq.put("eat", 2)
    pq.put("sleep", 3)
    pq.put("coding", 2)
    pq.put({"coding": 12345}, 4)
    print(pq)
    
