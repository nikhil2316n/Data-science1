#22/09/25

number=[[10,20,30],50,[20,10],[20]]
for i in number:
    if type(i)==int:
        print(i)
    else:
        for j in i:
            print(j)



