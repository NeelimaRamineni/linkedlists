#insertion at beginning and del at end
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head.prev = new_node
        self.head = new_node
    def display(self):
        temp = self.head
        print("Double Linked List:")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
        print("None")
    def delete_at_end(self):
        if self.head is None:
            print("Can't perform delete in an empty list....")
            return
        temp = self.head
        if temp.next is None:  
            print(f"Deleted: {temp.data}")
            self.head = None
            return
        while temp.next:
            temp = temp.next
        print(f"Deleted: {temp.data}")
        temp.prev.next = None
    def BackTraverse(self):
        print("Double Linked List:")
        temp = self.head
        if not temp:
            print("List is empty")
            return
        while temp.next:
            temp = temp.next
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.prev
        print("None")
dll = DoubleLinkedList()
n = int(input("Enter the number of elements to insert at beginning: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.insert_at_beginning(val)
dll.display()
d = int(input("Enter how many times you want to perform delete-at-end operation: "))
for _ in range(d):
    dll.delete_at_end()
    dll.display()
dll.BackTraverse()
