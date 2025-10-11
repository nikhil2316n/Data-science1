class Stack:

    def __init__(self):
        self.lst=[]
        

    def push(self,n):
        self.n=n
        self.lst.append(self.n)
        print(f"The element {self.n} is inserted into stack ")

    def pop(self):
        
        if len(self.lst)==0:

            print("It is a empty Stack")

        else:
            print(f'The {self.lst[-1]} is popped out from stack')
            self.lst.pop(-1)
            

    def peek(self):

        if len(self.lst)==0:
            print("It is a empty list")

        else:

            print(f"The top element of stack is :{self.lst[-1]}")


    def check(self):
        if len(self.lst)==0:
            print("The stack is Empty ")

        else:
            print("The Stack is not Empty")


    def get_stack(self):

        print(f"The current stack :{self.lst}")
    
    



s1=Stack()
s1.push(5)
s1.push(10)
s1.push(20)
s1.pop()
s1.peek()
s1.get_stack()
s1.check()

