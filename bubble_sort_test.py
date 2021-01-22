# O(n^2)
# 

def bubble_sort(data: list) -> list:
    # iterate through entire list, and switch
    # values
    swapped = True

    while swapped:
        swapped = False
        for i in range(len(data) - 1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                swapped = True
