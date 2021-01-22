# O(n^2)
# recursion
# pivot number and requires partitioning first into two pieces

def partition(data: list, start: int, end: int) -> list:

    pivot = data[start]
    low = pivot + 1
    high = end

    while True:
        while low <= high and data[low] <= pivot:
            low = low + 1

        while low <= high and data[high] >= pivot:
            high = high - 1


        if low <= high:
            data[low], data[high] = data[low], data[high]
        else:
            break

    data[start], data[high] = data[high], data[start]

    # return the position of the pivot number
    return high


def quick_sort(data: list, start: int, end: int) -> list:
    # immediately kill the process if the start index is larger than the end.
    if start >= end:
        return

    # sets the position of the pivot number after initial sort
    p = partition(data, start, end)

    quick_sort(data, start, p-1)
    quick_sort(data, p + 1, end)