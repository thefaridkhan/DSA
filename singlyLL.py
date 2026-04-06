class Node:
    def __init__(self, info, next=None):
        self.data = info
        self.next = next


class SinglyLL:
    def __init__(self, head=None):
        self.head = head

    def insertatend(self, value):
        temp = Node(value)
        if self.head != None:
            t1 = self.head
            while t1.next != None:
                t1 = t1.next
            t1.next = temp
        else:
            self.head = temp

    def insertatbegining(self, value):
        temp = Node(value)
        temp.next = self.head
        self.head = temp

    def insertatmiddle(self, value, x):
        temp = Node(value)
        t1 = self.head

        while t1 != None:
            if t1.data == x:
                temp.next = t1.next
                t1.next = temp
                break
            t1 = t1.next

    def deleteLL(self, value):
        t1 = self.head
        prev = None

        while t1 != None:
            if t1.data == value:
                if prev == None:
                    self.head = t1.next
                else:
                    prev.next = t1.next
                return
            prev = t1
            t1 = t1.next

    def printLL(self):
        t1 = self.head
        while t1 != None:
            print(t1.data)
            t1 = t1.next


obj = SinglyLL()
obj.insertatbegining(13)
obj.insertatbegining(31)
obj.insertatbegining(34)

obj.printLL()