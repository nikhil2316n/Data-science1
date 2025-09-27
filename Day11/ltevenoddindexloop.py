#19/09/25
#input a[A,B,C,D,E,F,G,H]
#OUTPUT:
#l1=[A,C,E,G]
#l2=[B,D,F,H]

leters=["A","B","C","D","E","F",'G',"H"]
l1=[]
l2=[]
i=0
while i<8:
    if(i%2==0):
        l1.append(leters[i])
    else:
        l2.append(leters[i])
    i+=1

print("Even index list :",l1)
print("Odd index list  :",l2)