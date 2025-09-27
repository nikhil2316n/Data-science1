#16/09/25
#

db={"nikhil@gmail.com":"Nikhil2316","Sai@gmail.com":"sai2005","pranay@gmail.com":"0623pranay"}
print(db)

searchid=input("Enter the search id : ")



if(db.get("searchid")==None):
    print("User does not exist in the Data ")

    x=input("Do you want to sign up?")
    if(x=="yes"):
        newid=input("Enter new id ")
        newpwd=input("Enter the password")
        db[newid]=newpwd
        print(db)
    elif(x=="no"):
        print("exited succesfully")

    else:
        print("Input Error")

else:
    print("User present in the db!!")
    print(db.get("searchid"))
    

