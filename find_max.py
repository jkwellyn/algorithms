# O(n) linear time, iterates through all items

def find_max(items):

    if len(items) == 1:
        return items[0]

    op1 = items[0]
    op2 = find_max(items[1:])

    if op1 > op2:
        return op1
    else:
        return op2


stuff = [99,77,99,22,33,51, 8]

print(find_max(stuff))

