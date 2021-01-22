class ListNode:
    """
    :param val: cache key
    :param prev: previous ListNode
    :param next: next ListNode
    """
    def __init__(self, val: str) -> None:
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.size = 0
        self.map = {} # tracking cached values
        self.dummy = ListNode("#") # DummyNode to indicate the head of the linked list
        self.current = self.dummy # current marker to track the tail of the linked list

    # get
    # checks to see if the key is in the cache map
    # if the key is in the map, get the node
    # see if the node is the current node
    # if it's not the end of the linked list, delete it from the linked list, readd to the end, to make it current

    def get(self, key: int) -> int:
        """
        :param key: cache key
        """
        if key in self.map:
            node = self.map[key][1] # gets the node for the given key from the map
            if node != self.current:
                self.delete_node(node) # if the node isn't the last in the linkedlist, we're going to want to move it to the end for recency
                self.insert_node(node) # reinsert the node so that it reflects that it was used recently
            return self.map[key][0] # return the value of the key

    # delete
    # delete the node from the linked list but changing the pointer references
    # previous node's next, should reference the node's next
    # node's next previous should reference node's previous
    def delete_node(self, node: ListNode) -> None:
        """
        :param node: ListNode
        """
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        node.next, node.prev = None, None

    # insert
    # update the current node to be equal to the node being added
    # current node's next becomes equal to node
    # node previous equal current node
    # current node becomes current node
    def insert_node(self, node: ListNode):
        self.current.next = node
        node.prev = self.current
        self.current = node


    # put
    # check capacity is the size smaller than the capacity
    # hurrah it is
    # if the key is not in the map
    # create a new node, with the key ListNode(key)
    # insert the node
    # add it to the map, map[key] = [value, node]

    # if the key is in the map
    # get the node
    # check to see if the node is the current node
    # delete the node if it isn't and reinsert to make it the end
    # set the current node to equal the node
    # set the value  map[key][0] = value

    # at capacity???
    # check to see if the key is already in the map
    # get the node
    # compare it to see if it's the current node
    # if its not, delete it, reinsert it
    # set the current node to equal the current node
    # udpate the value map[key][0] value

    # not in the map?
    # get the head node but grabbing the next value from the dummy (thank lord for the dummy)
    # head = dummy.next
    # del map[head.val] removes the cached value
    # self.deleteNode(head)
    # self.insertNode(node)
    # reset the current node to equal the new node
    # map[key] = [value, node]

    def put(self, key: int, value: int) -> None:
        if self.size < self.capacity:
            if key not in self.map:
                node = ListNode(key)
                self.insert_node(node)
                self.map[key] = [value, node]
                self.size += 1
            else:
                node = self.map[key][1]
                if node != self.current:
                    self.delete_node(node)
                    self.insert_node(node)
                self.map[key][0] = value
        else:
            if key in self.map:
                node = self.map[key][1]
                if node != self.current:
                    self.delete_node(node)
                    self.insert_node(node)
                self.map[key][0] = value
            else:
                head = self.dummy.next
                del self.map[head.val]
                self.delete_node(head)
                node = ListNode(key)
                self.insert_node(node)
                self.map[key] = [value, node]


if __name__ == "__main__":
    pass