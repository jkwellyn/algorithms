"""
Python Data Structures - A Game-Based Approach
Stack class
Robin Andrews - https://compucademy.net/
"""


class Stack:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        # Returns False if there is nothing
        return not self.items

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)

# Only execute this if running this file directly
if __name__ == "__main__":
    s = Stack()
    print(s)
    s.push(4)
    s.push(7)
    s.push(8)
    s.peek()
    print(s)
    print(s.pop())
