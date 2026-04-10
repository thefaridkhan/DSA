
from posixpath import curdir
class Node:
    def __init__(self, val):
        self.val=val
        self.next=None
        self.prev=None

class DoublyLL:
    def __init__(self):
        self.head=None

    # insert at head
    def Insert_at_head(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            new_node.next=self.head
            self.head.prev=new_node
            self.head=new_node

    # Append (add at last )
    def Append(self,val):
        new_node=Node(val)
        if not self.head:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node
            new_node.prev=current
        
    # insert_at position 
    def insert_at_position(self,val,position):
        new_node=Node(val)
        
        if position==0:
            self.Insert_at_head(val)
            return

        current=self.head
        count=0
        while current and count < position-1:
            current =current.next 
            count +=1
        if current is None:
            print("Positin out of bound !!")
            return
        new_node.next=current.next
        new_node.prev=current
        if current.next:
            current.next.prev=new_node
        current.next=new_node


    # print all the node:

    def printLL(self):
        current=self.head
        while current!=None:
            print(current.val, end=" <-> ")
            current=current.next

        print("None")

    # delete at last 

    def delete_at_last(self):
        if self.head==None:
            print("Empty LL")
            return
        if self.head.next==None:
            self.head=None
            return
        current = self.head
        while current.next!=None:
            current=current.next

        current.prev.next=None
        current.next=None

    # delete at posion
    def delete_at_position(self,position):
        if self.head==None:
            print("Empty LL")
            return
        if position==0:
            if self.head.next is None:
                self.head=None
            else:
                self.head=self.head.next
                self.head.prev=None
            return

        current=self.head
        count=0
        while current and count <position:
            current=current.next
            count+=1

        if current is None:
                print("Posint out of bound !!")
                return
            
        if current.next:
                current.next.prev=current.prev
        if current.prev:
                current.prev.next=current.next


            



s=DoublyLL()
s.Append(23)
s.Append(23)
s.Append(22)
s.Append(2323)
s.delete_at_last()
s.insert_at_position(13,3)
s.delete_at_position(3)
s.printLL()