# average O(n log n), worst case O(n**2)
# Worst case scenario is caused by the randomness of the pivot number, it could be the highest or the lowest input
# take the last element as the pivot
# don't use when stable sorting is necessary. quick sort evaluates the value and doesn't care about the order
# space complexity O(log n)

# partition function

def partition(data: list, start: int, end: int) -> list:

    # take the first element as the pivot point
    pivot = data[start]

    # start the low index as the second element after the pivot
    low = pivot + 1

    # high index is the length of the array - 1
    high = end

    while True:
    # while the lower index is smaller than high
    # check to see if the low index is smaller than the pivot
    # increment the low index unless conditions are not met
        while low <= high and data[low] <= pivot:
            low = low + 1

        # decrease the index pointer if number is higher than pivot
        while low <= high and data[high] >= pivot:
            high = high - 1

        # switch the indices because they are on the wrong side of the pivot
        if low <= high:
            data[high], data[low] = data[low], data[high]
        else:
            break

    # this gives us a new pivot point
    # The last number that was higher than the pivot has now become the pivot
    # while the previous pivot number is switched to the position of the previous high index
    data[start], data[high] = data[high], data[start]

    # returning the high index, tells the user where the last pivot number is currently located
    # in the array
    return high


# quicksort function

def quicksort(data: list, start: int, end: int) -> list:
    # checks that the indexes are not crossed
    if start >= end:
        return
    
    # return the position of the pivot number
    p = partition(data, start, end)

    # this recursively puts all the numbers in order based on the pivot
    # until there are no numbers to turn into a pivot
    # updates everything on the leftside first and then cleans up the right side
    # end array is completely sorted
    quicksort(data, start, p-1)
    quicksort(data, p+1, end)