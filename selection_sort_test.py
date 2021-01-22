# O(n^2)
# selection sort is iterating twice
# first iteration for every number comparison
# second loops the second number after the first pivot
# compares every single number to i to determine the lowest number



def selection_sort(data: list) -> list:

    for i in range(len(data)):

        min_index = i

        for j in range(i + 1, len(data) - 1):

            if data[min_index] > data[j]:
                # the purpose of this is to track where the lowest number so far is located
                # constantly flipping the location of the index would use up more space 
                # and create more steps
                min_index = j
        
        # at the end of the inner loops, the original indexed element should switch with what is identified
        # as the lowest number which is set to min_index
        data[i], data[min_index] = data[min_index], data[i]