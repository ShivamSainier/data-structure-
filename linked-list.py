# A linked list is represented by a pointer to the first node of the linked list. The first node is called the head. If the linked list is empty, then the value of the head is NULL.
# Each node in a list consists of at least two parts:
# 1) data
# 2) Pointer (Or Reference) to the next node

# Let us create a simple linked list with 3 nodes.
class node:
    def __init__(self,data):
        self.data=data
        self.next=None
    
    
class linkedlistt:
    def __init__(self):
        self.head=None
    def printlist(self):
        temp=self.head
        while temp:
            print(temp.data)
            temp=temp.next


n1=node("first-data")
n2=node("second-data")
n3=node("third-data")
listt=linkedlistt()
listt.head=n1
n1.next=n2
n2.next=n3
listt.printlist()
