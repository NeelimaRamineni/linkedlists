# at the position insertion at DLL
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoubleLinkedList:
    def __init__(self):
        self.head = None
    def iap(self,pos, data): 
        newnode = Node(data)
        if pos<=0:
            print("invalid position")
            return
        if pos==1:
            newnode.next=self.head
            if self.head:
                self.head.prev=newnode
            self.head=newnode
            return
        temp=self.head
        for _ in range(pos-2):
            if temp is None:
                print("position off range")
                return
            temp=temp.next
        if temp is None:
            print("no elements....")
            return
        newnode.next=temp.next
        newnode.prev=temp
        if temp.next:
            temp.next.prev=newnode
        temp.next=newnode    
    def display(self):
        temp = self.head
        print("Double Linked List:")
        while temp:
            print(temp.data, end="<->")
            temp = temp.next
        print("None")
dll = DoubleLinkedList()
dll.iap(1,100)
n = int(input("Enter number of elements: "))
for i in range(n):
    val = int(input(f"Enter element {i+1}: "))
    pos=int(input(f"enter the position to insert {val}:"))
    dll.iap(pos,val)  
dll.display()
