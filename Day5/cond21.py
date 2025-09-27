
#10/09/25

user_loc=(10,15)
d1_loc=(12,18)
d2_loc=(2,5)

def dist(point_1,point_2):
    total_dist=(((point_2[0]-point_1[0])**2)+((point_2[1]-point_1[1])**2))**0.5
    
    return total_dist


def driverassignment(user_loc,d1_loc,d2_loc):

    if(dist(user_loc,d1_loc)>dist(user_loc,d2_loc)):
        print("Driver D2 assigned")

    else:
        print("Driver D1 is assigned")
