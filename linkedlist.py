class LinkedListNode(object):
    def __init__(self, value, nn=None):
        """
        Args:
            nn: The next node
        """
        self.value = value
        self.next = nn

    def __str__(self):
        return str(self.value)


class LinkedList(object):
    def __init__(self, values=None):
        """
        Args:
            values: A list of integers
        Returns:
            A reference to the head of the list
        """
        self.head = None
        if values:
            self.head = LinkedListNode(values[0])

        self.add_multiple(values[1:])

    def get_next(self):
        """A generator for getting the next element of the list.
        """
        if not self.head:
            raise StopIteration
        else:
            curr = self.head
            while curr:
                yield curr
                curr = curr.next
            raise StopIteration()


    def add(self, value):
        """ Add a single node to the end of the list

        Args:
            value: The node to be added
        """
        if not self.head:
            self.head = LinkedListNode(value)
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = LinkedListNode(value)

    def add_multiple(self, values=None):
        """Add multiple values at once to the list

        Args:
            values: A list of integers to add to the list, can be empty

        Returns:
            Pointer to the head of the list
        """
        if not values:
            return

        if not self.head:
            self.head = LinkedListNode(values[0])
            del values[0]

        curr = self.head
        while curr.next:
            curr = curr.next

        for value in values:
            curr.next = LinkedListNode(value)
            curr = curr.next

        curr.next = None

        return self.head

    def exists(self, value):
        """ Whether a node with a particular value exists
        Args:
            value: The value to check

        Returns:
            True/False depending on the whether the value exists
        """
        if not self.head:
            return False

        curr = self.head
        if curr.value == value:
            return True

        while curr.next:
            if curr.value == value:
                return True
            curr = curr.next
        return False

    def delete_by_value(self, value):
        """ Deletes a node by value
        Args:
            The value of the node to be deleted
        """
        if not self.head:
            print('Linked list empty!')
            return

        if self.head.value == value:
            new_head = self.head.next
            del self.head
            self.head = new_head
            return

        curr = self.head
        prev = curr
        while curr.next:
            if curr.next.value == value:
                prev.next = curr.next.next
                del curr.next
            else:
                prev = curr
                curr = curr.next

    def delete_by_reference(self, node):
        """Deletes a node in the list only given its reference
        Args:
            node: The reference to the node to be deleted
        """
        if not self.head:
            print('Linked list empty!')
            return

        if self.head==node:
            self.head = self.head.next
            del self.head

        curr = self.head
        prev = curr

        while curr.next:
            if curr==node:
                prev.next = curr.next
                del curr
            else:
                prev = curr
                curr = curr.next

    def removeDuplicates(l=None):
        """Remove duplicates from unsorted linked list with temporary
        buffer allowed. """
        if l.length == 1:
            return l
        curr = self.head
        seen = set([curr.value])
        while curr.next:
            if curr.next.value in seen: # duplicate encountered
                curr.next = curr.next.next
            else:
                seen.add(curr.next.value)
                curr = curr.next
                 # add to the dict

    def reverse(self):
        if not (self.head or self.head.next):
            print('List not reversible!')
            return

        curr = self.head
        next_to_reverse = curr.next
        self.head.next = None

        while next_to_reverse.next:
            curr = curr.next.next
            curr = next_to_reverse
            next_to_reverse = curr.next


def print_list(l):
    """A general utility for printing a linked list
    Args:
        l: A list or a reference to the head of the list
    """
    if not l.head:
        print("List Empty!")

    print(' -> '.join([str(curr.value) for curr in l.get_next()]))

def removeDuplicatesFollowUp(l=None):
    if l.length == 1:
        return

    check = self.head
    while check:
        curr = check.next
        while curr.next:
            #duplicate encountered
            if curr.value == check.value :
                curr.next = curr.next.next
            curr = curr.next

def addLists(l1, l2):
    if l1.length == 0:
        return l2
    if l2.length == 0:
        return l1

    head = None
    curr = head
    result = 0
    carry = 0
    while(l1 or l2):
        if l1:
            result += l1.value
            l1 = l1.next
        if l2:
            result += l2.value
            l2 = l2.next

        result = (result+carry) % 10
        carry = (result+carry) // 10

        curr = LinkedListNode(result)
        curr = curr.next

    return head

if __name__ == "__main__":
    l = LinkedList([1,2,4,5,6,8])
    # l.reverse()
    print_list(l)
