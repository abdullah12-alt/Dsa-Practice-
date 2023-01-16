class Node:
    def __init__(self,Data=None):
        self.data= Data
        self.next=None

class LinkedList:
    def __init__(self):
          self.head=None        
    
    def InsertAtStart(self,data):
        
        if self.head ==None:
            NewNode = Node(data)
            self.head = NewNode
        else:
            NewNode = Node(data)
            NewNode.next=self.head
            self.head= NewNode

    def PrintList(self):
        temp = self.head
        while(temp):
            print(f'{temp.data}-> ',end="")
            temp=temp.next
        print("Null")



list=LinkedList()

list.InsertAtStart(11)
list.InsertAtStart(13)
list.InsertAtStart(12)
list.PrintList()
