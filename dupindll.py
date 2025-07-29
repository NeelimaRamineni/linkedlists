#checking dupliacates in dll
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
        if not self.head:
            self.head = new_node
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    def display(self):
        temp = self.head
        print("Doubly Linked List:")
        while temp:
            print(temp.data, end=" <--> ")
            temp = temp.next
        print("None")
    def find_duplicates(self):
        freq = {}
        temp = self.head
        while temp:
            freq[temp.data] = freq.get(temp.data, 0) + 1
            temp = temp.next      
        duplicates_found = False
        print("Duplicate values in DLL:")
        for value, count in freq.items():
            if count > 1:
                print(f"{value} appears {count} times")
                duplicates_found = True
        if not duplicates_found:
            print("No duplicates found.")
dll = DoubleLinkedList()
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    dll.insert_at_end(val)
dll.display()
dll.find_duplicates()
