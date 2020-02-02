#insertion in the linked list (beginning)

class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next
    def insert(self,new_data):
        new=node(new_data)
        new.next=self.head
        self.head=new

n1=node("my-first_node")
n2=node("my-second-node")
n3=node("my-thid-node")
listt=linkedlist()
listt.head=n1
n1.next=n2
n2.next=n3
listt.insert("hello")
listt.printlist()






