#20/09/24
#Saturday


#write a python function which takes a input of a number and calculates the sum till that point

# def sumof():
    
#     num=int(input("Enter the Number"))
#     sum=0
    
#     for i in range(num):
#         sum=sum+i
    
#     return sum

# print(sumof())

num=int(input("Enter the number"))
sum=0

for i in range(num+1):
    sum=sum+i

print(sum)
