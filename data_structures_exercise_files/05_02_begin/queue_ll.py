"""
Python Data Structures - A Game-Based Approach
Queue class
Robin Andrews - https://compucademy.net/
"""

from collections import deque


class Queue:
    # deque double ended queue, built in to Python
    def __init__(self):
        self.items = deque()
    
    def is_empty(self):
        return not self.items

    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.popleft()

    def size(self):
        return len(self.items)

    def peek(self):
        # return the front of the queue
        return self.items[0]

    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    queue = Queue()
    print(queue)
    print(queue.is_empty)
    queue.enqueue('a')
    print(queue)
    queue.peek()
    queue.dequeue()
    print(queue)