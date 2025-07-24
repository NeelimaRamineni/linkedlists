class Node:
    def  __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def  __init__(self):
        self.head=None
    def iap(self,data,pos):
        newnode=Node(data)
    if pos<=0:
        print("position min>=1")
        return
    if pos==1:
        newnode.next==self.head
        self.head=newnode
        print(f"{data} inserted at pos-1")
        return
    current=self.head
    c=1
    while current and c < pos-1:
        current=current.next
        c+=1
    if not current:
        print("not in range...")
        return 
    newnode.next=current.next
    current.next=newnode
    print("f{data} inserted at position{pos}.")    
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
    print("3.Exit")
    choice=input("enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        pos=int(input("enter position starting from 1:"))
        ll.iap(data,pos)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        print("Exit the operation...")
        break
    else:
        print("Enter only....1/2/3")