# quasilinear O(n log n) linear search with logarithmic input
# uses extra memory 

def merge_sort(data: list):

    # breaking condition for data length
    if len(data) <= 1:
        return

    mid = len(data) // 2

    left_data = data[:mid]
    right_data = data[mid:]

    # splits the entire array into left and right pieces
    # each split is correcting a different left/right object in memory until there is nothing left to split
    # left keeps computing until there is nothing left to compute on the left
    merge_sort(left_data)
    # then right side keeps computing until there's nothing left to compute
    merge_sort(right_data)

    # above recursion generates a group left/right pieces to be processes below

    left_index = 0
    right_index = 0
    # used to append the new sorted list
    data_index = 0

    # this iterates through all the left_data/right_data splits made above
    while left_index < len(left_data) and right_index < len(right_data):
        # if/else statements are ignored if the left/rights are already sorted
        # and goes to the next set of left/rights
        # keeps iterating until there is no left/right sets out of order
        if left_data[left_index] < right_data[right_index]:
            data[data_index] = left_data[left_index]
            left_index += 1
        else:
            data[data_index] = right_data[right_index]
            right_index +=1
        #  each time this is run, a new sorted data list is created
        data_index += 1

    # when left or right has ints left
    if left_index < len(left_data):
        del data[data_index:]
        data += left_data[left_index:]
    elif right_index < len(right_data):
        del data[data_index:]
        data += right_data[right_index:]

    # partial sorts, then recursively does it again, until everything is completely sorted
    # creates new data set, splits it left and right again, and sorts until there's nothing left to sort

