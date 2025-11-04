

class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def input(self,data):
        new_node=node(data)
        if(self.head is None):
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
    def showe(self):
        temp=self.head
        while temp!=None:
            print(temp.data)
            temp=temp.next
l=linklist()
l.input(10)
l.input(22)
l.input(33)
l.showe()
