class Queue:

    def __init__(self):
        self.que=[]

    def enqueue(self,n):
        self.n=n
        self.que.append(n)
        print(f"The Element {n} is added into the queue")

    def dequeue(self):
        if len(self.que)==0:
            print("The queue is Empty")

        else:
            print(f"The element {self.que[0]} is removed from queue")
            self.que.pop(0)

    def peek(self):

        print(f"The first element of queue is :{self.que[0]}")
    
    def check(self):
        if len(self.que)==0:
            print("The Queue is Empty")

        else:
            print("The queue is not Empty")

    def get_queue(self):
        if len(self.que)==0:
            print("The Queue is Empty")

        else:
            print("Current Queue is:",self.que)

q=Queue()
q.check()
q.enqueue(5)
q.enqueue(10)
q.enqueue(15)
q.enqueue(20)
q.enqueue(25)
q.get_queue()
q.dequeue()
q.get_queue()
q.check()
q.peek()
q.get_queue()
