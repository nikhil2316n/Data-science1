#19/09/25

#Program to store the odd numbers from 0 to 100 in a list


a=0
lt=[]
while a<=100:

    if(a%2!=0):
        lt.append(a)
    a=a+1

print(lt)
