# __description__:Given a singly linked list of integers, determine whether or not it's a palindrome.
# Solution is in O(1) space and O(n) time complexity.


import math

# Definition for singly-linked list:
class ListNode(object):
  def __init__(self, x):
    self.value = x
    self.next = None

def getLength(l):
    ln = 0
    while l:
        ln+=1
        l = l.next
    return ln

def isListPalindrome(l):
    ln = getLength(l)
    
    if ln==1 or ln==0:
        return True
    
    if ln==2:
        return l.value==l.next.value
    

    hmid=l
    k = math.ceil(ln/2)
    while(k > 0):
        hmid=hmid.next
        k-=1
    
    # hmid points to the midpoint of the list (or the 
    # head of the 2nd half of the list)
    print(hmid.value)
    

    # reverse the linked list from midpoint onwards inplace    
    prev = None
    curr = hmid
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
        

    # prev points to the 2nd half of the list
    k = math.floor(ln/2)
    
    # compare the two lists for diff elements.
    while k>0:
        if l.value != prev.value:
            return False  
        k-=1
    return True
        
    
    

if __name__== "__main__":

    # l = [1, 2, 2, 3]

    l = ListNode(1)
    l.next = 2
    l.next.next = 2
    l.next.next.next = 3

    isListPalindrome(l)
