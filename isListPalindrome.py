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
    
    if not l:
        return False
    
    ln = getLength(l)
    print(ln)
    
    hmid=l
    k = math.ceil(ln/2)
    while(k > 0):
        hmid=hmid.next
        k-=1
        
    print(hmid.value)
        
    # reverse the linked list from midpoint onwards inplace    
    


if __name__=="__main__":

    # l = [1, 2, 2, 3]

    v

    isListPalindrome(l)
