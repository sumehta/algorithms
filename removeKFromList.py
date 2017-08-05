# __description__: Given a singly linked list of integers l and an integer k, remove all elements from list # l that have a value equal to k.

# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    # case when the list is empty
    if not l:
        return
    # remove all elements from the top of the list equal to k
    while l and l.value == k:
        l = l.next
    curr = l
    prev = l

    while curr:
        if curr.value == k:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr 
            curr = curr.next
            
    return l


