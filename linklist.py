

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def input(self,data):
        new_data=node(data)
        if(self.head is None):
            self.head=new_data
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_data
    def show(self):
        temp=self.head
        while temp is not None:
            print(temp.data)
            temp=temp.next
    def count(self):
        c=0
        temp=self.head
        while temp is not None:
            c+=1
            temp=temp.next
        return c
    def position(self,val):
        pos=1
        temp=self.head
        while temp is not None:
            if(temp.data==val):
                print(f"Value {val} found at index or position {pos}")
                return 
            else:
                temp=temp.next
                pos+=1
        print("Value not found at any index ")  
    def insertstart(self,data):
        new_data=node(data)
        new_data.next=self.head
        self.head=new_data
    def insterend(self,data):
        new_data=node(data)
        if(self.head is None):
            self.head=new_data
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_data
    def Position(self,pos,data):
        new_data=node(data)
        if(pos==1):
            new_data.next=self.head
            self.head=new_data
        else:
            temp=self.head
            i=0
            while i<pos-1 and temp is not None:
                temp=temp.next
                i+=1
            if(temp is None):
                print("invalid")
            else:
                new_data.next=temp.next
                temp.next=new_data 
    def deletefisrt(self):
        if(self.head is None):
            print("Link list is Empty ")
            return
        else:
            self.head=self.head.next
    def deletelast(self):
        if(self.head is None):
            print("Invalid ")
        elif(self.head.next is None):
            print("link list contain only one node ")
            self.head=None
            return
        else:
            temp=self.head
            while temp.next.next:
                temp=temp.next
            temp.next=None
    def deltpos(self,pos):
        if(self.head is None):
            print("Invalid ")
            return
        if (pos==1):
            self.head=self.head.next
            return
        count=1
        temp=self.head
        while temp is not None and count<pos-1:
            temp=temp.next
            count+=1
        if(temp is None or temp.next is None):
            print("Invalid condition")
        else:
            temp.next=temp.next.next

l=linklist()
l.input(10)
l.input(20)
l.input(30)
l.show()
print(f"Total node are used in link list is {l.count()}")
l.position(20)

