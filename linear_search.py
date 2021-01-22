def linear_search(data: list, value:int):

    for i in range(0, len(data)):
        if data[i] == value:
            return i
        return -1
        