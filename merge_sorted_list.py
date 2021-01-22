# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(l1: ListNode, l2: ListNode) -> ListNode:

    # assume your list node only return one value and one next
    # insert a node by setting the .next
    # that new node's .next should equal the previous .next
    # breaking conditions

    head = ListNode(0)
    tail = head.next
        
    while True:          
        # Append the new node at the end 
        # of the linked list 
        if l1 is None:
            tail.next = l2
            break
    
        if l2 is None:
            tail.next = l1
            break

        if l1.val < l2.val:
            tail.next = l1.val
            l1 = l1.next

        if l2.val < l1.val:
            tail.next = l2.val
            l2 = l2.next
    
    return head


if __name__ == '__main__':
    listA = ListNode([1,2,4])
    listB = ListNode([1,3,4])
    
    x = mergeTwoLists(listA, listB)
    print(x)