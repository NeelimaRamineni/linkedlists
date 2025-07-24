'''Delete operation at end'''
class Node:
    def  __init__(self, data):
        self.data = data
        self.next = None
class LinkedList:
    def  __init__(self):
        self.head = None
    def iae(self, data):
        newnode = Node(data)
        if not self.head:
            self.head = newnode
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = newnode
    def deleteend(self):
        if self.head is None:
            print("Empty LL")
        elif self.head.next is None:
            print("Deleted node from end:", self.head.data)
            self.head = None
        else:
            current = self.head
            while current.next.next:
                current = current.next
            print("Deleted node from end:", current.next.data)
            current.next = None
    def display(self):
        current = self.head
        if not current:
            print("LL is Empty")
            return
        while current:
            print(current.data, end=' ---- ')
            current = current.next
        print("None")
ll = LinkedList()
while True:
    print("\nLinkedList - Delete At End...")
    print("1. Insert")
    print("2. Display")
    print("3. Delete at End")
    print("4. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        data = int(input("Enter a value to insert: "))
        ll.iae(data)
    elif choice == '2':
        ll.display()
    elif choice == '3':
        ll.deleteend()
    elif choice == '4':    
        print("Exiting the operation...")
        break
    else:
        print("Enter only 1 / 2 / 3 / 4")
