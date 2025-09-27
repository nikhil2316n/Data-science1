#23/09/25
#withdraw 
#return avaliable balance if a user enter negative value it should give a error

balance=1000
def withdraw(y):
    if y<0:
        raise ValueError("you cannot enter a negative value")
    else:
        b=balance-y
        print("Available Balance")

        return b

print(withdraw(10))
