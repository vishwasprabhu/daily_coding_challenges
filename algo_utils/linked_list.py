class Node:
    self.val = val
    self.next = None

class LinkedList():
    def _init__(self):
        self.head = None
    
    def reverse(self):
        """Method to reverse elements in a Linked List
        """
        prev = None
        curr = self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
