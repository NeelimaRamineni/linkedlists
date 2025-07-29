#insertion at end and del by val
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def display(self):
        temp = self.head
        print("Double Linked List (Forward):")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
        print("None")
    def Delete_by_value(self, value):
        temp = self.head
        while temp:
            if temp.data == value:
                print(f"Deleted: {temp.data}")
                if temp.prev:
                    temp.prev.next = temp.next
                else:
                    self.head = temp.next
                if temp.next:
                    temp.next.prev = temp.prev
                return
            temp = temp.next
        print(f"{value} not found in the list")
    def BackTraverse(self):
        print("Double Linked List (Backward):")
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
n = int(input("Enter the number of elements to insert at end: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.insert_at_end(val)
dll.display()
d = int(input("Enter how many times you want to perform delete operation: "))
for _ in range(d):
    val = int(input("Enter value to delete: "))
    dll.Delete_by_value(val)
    dll.display()
dll.BackTraverse()
