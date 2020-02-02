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
    def insert(self,prev,new_node):
        new=node(new_node)
        new.next=prev.next
        prev.next=new


n1=node("1st node")
n2=node("2nd node")
n3=node("3rd node")
listt=linkedlist()
listt.head=n1
n1.next=n2
n2.next=n3
listt.insert(n2,"4th node")
listt.printlist()