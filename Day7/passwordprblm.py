#12/09/25
#write the function which it takes the pasword as the input and check it if it is a valid password or not
#rules:
#1,it should have minimum 8 characters
#2,mix of character,numbers and atleast 1  special character 
#3,it should not have spaces
#optional role , it should have upper and lower case also

password=input("Enter your password")
length=len(password)
if(length>=8):
    if(password.isalnum()):
        if(password.isalpha()):
            if(password.isspace==False):
                if(password.isupper()):
                    if(password.islower()):
                        print("correct password")
else:
    print("wrong password")    