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
n1=node("node-1")
n2=node("node-2")
n3=node("node-3")
listt=linkedlist()
listt.head=n1
n1.next=n2
n2.next=n3
listt.printlist()
