# Write a function to determine if an object is undergoing uniform or non-uniform motion
# given a list of positions over time. 


position=[0, 1, 4, 8, 15]




def uniformmotion_check(lst):
    displacement=[]
    for i in range (len(position)-1):
        x=0
        x=position[i+1]-position[i]
        displacement.append(x)

    for i in range (len(displacement)-1):

        if (displacement[i]==displacement[i+1]):
            count=0
        else:
            count=-1


    if (count==0):
        print("It is a uniform motion")

    else:
        print("It is non-uniform motion")

    
uniformmotion_check(position)
