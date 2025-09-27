#19/09/25

#write a function to print table

def table(i):
    
    a=1
    while a<=10:
        print(f"{i}X{a}={i*a}")
        a=a+1
        
print(table(5))