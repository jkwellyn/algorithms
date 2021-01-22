# Recursion O(N) exponential, 
# binary heap, where the largest value is the root node

# split into a heapify array function then heapsort
# where the root node is at index i, the left node will always be left node (2 * i + 1), right n ode (2* i + 2)
# parent node is always i % 2
# heapify sorts subtrees

# heap datastructure is an array that can be viewed as a binary tree
# max heap, the root node should be the largest value

# in place sorting which means constant space


# you can only delete the first element of heaps and then the heap should restructure itself
# if a new elemented is added it should resort itself

# heapify starts with first non-leaf node index
# recursively check every parent node and place them in the right section
# n is the size of the heap

# binary trees
# full binary tree requires every node with a child to have left and right child nodes
# complete binary tree requires every level to be filled with the exception of the last leaf node which does
# not have to have a right child
# complete binary trees should also be left leaning

def heapify(arr: list, n: int, i: int) -> None:
    """
    Takes a root node, then compares which index contains
    the larger value, then moves it left or right, the does the same
    comparison throughout the array
    :param arr: the list of items to be sorted
    :param n: The size of the array given
    :param i: The index of the root to start heapify from 
    """
    
    # Set the largest node as the root node
    # If the left index is smaller than the n size and 
    # the left index is larger than the root index, set the largest as the left
    # Not check if right index is smaller than n size
    # compare the largest to the right
    # if largest changed, switch with root node
    # recursively call heapify against the largest node

    largest = i
    l = 2 * i
    r = (2 * i) + 1

    if l < n and arr[i] < arr[l]:
        largest = l

    if r < n and arr[largest] < arr[r]:
        largest = r 

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heap_sort(arr: list) -> None:
    """
    Takes an array and sorts it into a max heap
    :param arr: list of elements  
    """   
    # heapsort, take an array
    # initially heapify against n//2 because it is a parent node with 2 leaves

    # extract the element at the top of the heap
    # heapify remaining heap to ensure order
    n = len(arr)

    for i in range(n // 2, -1, -1):
        heapify(arr, n, i)

    # element extraction from the max heap to make the heap sort
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    # results in reverse order sort so the smallest displays first