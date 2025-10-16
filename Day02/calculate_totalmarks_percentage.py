# 04/09/25

#Take 5 subjects marks as input and claculate total marks stored and percentage scored
maths=int(input("Enter no of marks scored in Maths : "))
java=int(input("Enter no of marks scored in JAVA : "))
dwbi=int(input("Enter no of marks scored in DWBI : "))
os=int(input("Enter no of marks scored in OS : "))
dbms=int(input("Enter no of marks scored in DBMS : "))

print("Total Marks : 500")

total=maths+java+dwbi+os+dbms
percentage=(total/500)*100
print("Maths marks")
print("Total marks Scored : ",total)
print("--------------------")
print("Overall Percentage : ",percentage)

