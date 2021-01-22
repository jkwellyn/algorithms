# quadratic time O(n^2) 
# linear computation for linear input

def bubble_sort(data):
    swapped = True
    while swapped:
        swapped = False
        # iterate through length of list
        for i in range(len(data)-1):
            # if item in index i is bigger than the next item
            # swap the two items in the index
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True

# go through every single item in a list, starting at the first index
# swap every single one
# swapped switches to False and breaks, when it no longer satisfies the if statement
# this be hella slow