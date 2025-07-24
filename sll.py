'''consider a single linked list with insert at end nodes after insertion reverse the node to print 
input - 11-22-33-44-55-null
output - 55-44-33-22-11-null'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end='-')
            current = current.next
        print("null")
ll = LinkedList()
i= input("Enter values separated by '-': ")  
values = i.split('-')
for val in values:
    if val.strip().isdigit():
        ll.insert_at_end(int(val.strip()))
print("Original list:")
ll.print_list()
ll.reverse()
print("Reversed list:")
ll.print_list()