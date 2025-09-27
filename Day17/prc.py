
class bank:
    def  __init__(self):
        self.customers=[]
        self.account=[]

    def addCustomer(self,customer_list):
        self.customers.append(customer_list)
        print("Customer is added to the list")

    def addAccount(self,account_list):
        self.account.append(account_list)
        print("Accoount is added to the list")

class customer:

    def __init__(self,name,age,id):
        self.name=name
        self.age=age
        self.id=id

    def balacne
        
        
class account:
    def __init__(self,pastbalance,currentbalance,accountno):
        self.pastbalance=pastbalance
        self.current=currentbalance
        self.accountno=accountno

