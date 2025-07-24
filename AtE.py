class Node:
    def  _init_(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def  _init_(self):
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
    def search(self,key):
        pos=1
        current=self.head
        while current:
            if current.data==key:
                print(f"{key} found in the LL") 
                return True
            current=current.next
            pos+=1
        print(f"{key} not found in the LL")
        return False           
    
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
    print("3.search")
    print("4.Exit")
    choice=input("enter your choice:")
    if choice=='1':
        data=int(input("enter a value to insert:"))
        ll.iae(data)
    elif choice=='2':
        ll.display()
    elif choice=='3':
        val=int(input("enter the value,you want to search:"))
        ll.search(val)
    elif choice=='4':    
        print("Exit the operation...")
        break
    else:
        print("Enter only....1/2/3/4")


