# O(log n)
# 3 indexes, low, mid, high
# assumes the the data is already sorted


def binary_search(data: list, value: int) -> list:

    low = 0
    high = len(data) - 1
    mid = 0

    while low <= high:

        mid = low + high // 2

        if data[mid] < value:
            high = mid - 1
        elif data[mid] > value:
            low = mid + 1
        else:
            mid

    return - 1