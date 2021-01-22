"""
Python Data Structures - A Game-Based Approach
Stack challenge
Robin Andrews - https://compucademy.net/
"""

import stack

string = "gninraeL nIdekniL htiw tol a nraeL"
reversed_string = ""
s = stack.Stack()

# Your solution here.

for element in string:
    s.push(element)

while not s.is_empty():
    reversed_string += s.peek()
    s.pop()

if __name__ == "__main__":
    print(reversed_string)
