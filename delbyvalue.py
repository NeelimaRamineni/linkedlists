'''Delete operation by value'''
class Node:
    def  __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def  __init__(self):
        self.head=None
    def iae(self,data):
        newnode=Node(data)
        if not self.head:
            self.head=newnode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode
    def deletevalue(self,key):
        current= self.head
        if not current:
            print("Empty LL")
            return
        if current.data==key:
            self.head= current.next
            print(f"{key} deleted from the list")
            return
        prev=None
        while current and current.data != key:
            prev=current
            current=current.next
        if not current:
            print(f"{key} not found in the LL") 
            return
        prev.next= current.next
        print(f"{key} deleted from the LL")   
    def display(self):
        current=self.head
        if not current:
            print("LL-Empty")
            return
        while current:
            print(current.data,end='----')
            current=current.next
        print("None")             
ll=LinkedList()
while True:
    print("\n LinkedList-Insert at Begin...")
    print("1.insert")
    print("2.display")
    print("3.delete by value")
    print("4.Exit")
    choice=input("enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iae(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        key=int(input("enter the value,you want to delete:"))
        ll.deletevalue(key)
    elif choice=='4':    
        print("Exit the operation...")
        break
    else:
        print("Enter only....1/2/3/4")



