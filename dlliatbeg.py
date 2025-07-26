#insertion at beginning
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def iab(self, data): 
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head.prev = newnode
            self.head = newnode
    def display(self):
        temp = self.head
        print("Double Linked List:")
        while temp:
            print(temp.data, end=' <-> ')
            temp = temp.next
        print("None")
dll = DoubleLinkedList()
n = int(input("Enter the number of elements to insert at beginning: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.iab(val)
dll.display()
