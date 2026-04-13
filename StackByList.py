class Stack:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0

    def push(self,item):
        self.items.append(item)

    def pop(self):
        if len(self.items)==0:
            return "can't pop, stack is empty"

        x=self.items.pop()
        return x

    def top(self):
        if len(self.items)==0:
            return "can't top, stack is empty  "

        
        return self.items[-1]

    def sixe(self):
        return len(self.items)

    def printstack(self):

        print(self.items)

s=Stack()
s.push(5)
s.push(7)
s.push(10)
s.pop()
print(s.top())
s.printstack()

            



    
