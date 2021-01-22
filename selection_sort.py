# selection sort
# O(2^n)
# take an array, find the smallest element and put it at the beginning of the array

def selection_sort(data: list) -> list:
    # traverse whole list
    for i in range(len(data)):
        # think of this index as the pivot number
        min_index = i 
        # iterate from index number to length of daa
        for j in range(i+1, len(data)):

            # everytime it finds a smaller number, min index updates, and the loop restarts until the loop has completed
            # then it goes to the next index
            if data[min_index] > data[j]:
                min_index = j
    
        data[i], data[min_index] = data[min_index], data[i]