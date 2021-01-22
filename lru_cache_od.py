from collections import OrderedDict
"""
1. create lrucache class with capacity=int
2. create a get method with key=int param, return value or -1 if not found
3. create put method (key=int, value=int)
4. create update method  if key exists, update the value
5. if key doesn't exist, put key into cache
6. if key doesn't exist and cache is over capacity, evict lru

# determine how to track lru
# double linked list, OrderedDict()
"""

# next(iter(dict))

class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0
        self.map = OrderedDict() # tracking the cache key values
    
    # get
    def get(self, key: int):
    # checks to see if the key passed is in the map
    # if it's in the map, get the key
    # delete the from the dict
    # readd it to the end of the dict
    # return the value

        if key in self.map:
            print(key)
            value = self.map[key]
            del self.map[key]
            self.map[key] = value
            return self.map[key]
        else:
            - 1


    # put
    # update value of the key if the key is in the map
    # insert value if the key doesn't exist
    # if the capacity is full, delete lru, then add new key/value to map
    # return nothing
    def put(self, key:int, value: int) -> None:
        # if they key is already in the map, delete the old record, and reinsert with new value to the end
        if key in self.map:
            del self.map[key]
            self.map[key] = value

        if self.size < self.capacity:
            if not key in self.map:
                self.map[key] = value
                self.size += 1
        else:
            head = next(iter(self.map))
            del head
            self.map[key] = value


if __name__ == "__main__":

    cache = LRUCache(capacity=5)
    cache.get(key=123)
    cache.put(key=123, value=890)
    cache.put(key=789, value=890)
    cache.put(key=999, value=2783)
    cache.put(key=999, value=2783)
    print(cache.map)
    print(cache.get(key=123))
    cache.put(key=999, value=2783)
    cache.put(key=769, value=2783)
    cache.put(key=119, value=25683)
    print(cache.map)