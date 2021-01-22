# O(n log n)
# take the input of a list, and recursively break it down
# compare the elements, sort and merge


def merge_sort(data: list) -> list:

    mid = len(data) // 2

    left = data[:mid]
    right = data[mid:]

    merge_sort(left)
    merge_sort(right)

    left_idx = 0
    right_idx = 0
    data_idx = 0

    while left_idx < len(left) and right_idx < len(right):

        if left[left_idx] < right[right_idx]:
            data[data_idx] = left[left_idx]
            left_idx += 1

        if right[right_idx] < left[left_idx]:
            data[data_idx] = right(right_idx)
            right_idx += 1
        
        data_idx = data_idx + 1
        
    while left_idx < len(left):
        data[data_idx] = left[left_idx]
        left_idx += 1
        data_idx += 1

    while right_idx < len(right):
        data[data_idx] = right[right_idx]
        right_idx += 1
        data_idx += 1