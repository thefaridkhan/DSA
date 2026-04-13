class Queue:
    def __init__(self):
        self.items=[]

    def is_empty(self):
        return len(self.items)==0

    def enqueue(self,item):
        return self.items.append(item)
    
    def dequeue(self):
        if len(self.items)==0:
            print("Queue is empty !!")
            return 
        x=self.items.pop(0)
        return x
    def front(self):
        if len(self.items)==0:
            print("can't front , queue is empty")
            return
        return self.items[0]
    
    def rear(self):
        if len(self.items)==0:
            print("can't rear , queue is empty")
            return
        return self.items[-1]


    def size(self):
        return len(self.items)

q=Queue()
q.enqueue(10)
q.enqueue(2)
q.enqueue(30)
q.dequeue()
print(q.items)


       