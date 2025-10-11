#10/10/25

#Create a line class 
#method:1.if the point is on the line or above or below the line
#2,Able to modify the slope of the line 
#3,able to modify the constant
#4,visualize the line
#5,get the constant and
#  get the cooffecient(slope)


#method to check two line are parllel , (plot)
# two lines are perpendicular(plot)
#get the angle thete the line makes with x axis
#angle betweenn two lines

import math
import numpy as np
import matplotlib.pyplot as plt

class Line:
    theta=0
    def __init__(self, slope, constant):
        self.slope = slope       
        self.constant = constant
        
        

    def checkpoints(self,x,y):
        self.x=x
        self.y=y
        self.z=self.x*self.slope+self.constant

        if y==self.z:
            print("The point is on the line")

        elif y>self.z:
            print("The point is below the line")

        else:
            print("The point is above the line")

    def modify_slope(self,nslope):
        self.nslope=nslope
        self.slope=self.nslope
        print("The slope is modified successfully")

    def modify_constant(self,n_const):
        self.n_const=n_const
        self.constant=n_const
        print("The constant is modified successfully")

    def get_constant(self):
        print(f"The constant is :{self.constant}")

    def get_cooefficient(self):
        print(f"The cooefficent is {self.slope}")

    #def visualize_line(self):

    def second_line(self,slop2,constant2):
        self.slop2=slop2
        self.constant2=constant2

    def check_parallel(self):
        if self.slope==self.slop2:
            print("The two lines are parllel")

        else:
            print("The lines are not parallel")

    def check_perpendicular(self):
        if (self.slope*self.slop2 ==-1):
            print("The two lines are perpendicular")

        else:
            print("The lines are not perpendicular")

    

    def visualize_line(self):
        self.x1=np.linspace(-10,10,100)
        self.y1=self.slope*self.x1 + self.constant

        self.x2=np.linspace(-10,10,100)
        self.y2=self.slop2*self.x2 + self.constant2
        plt.plot(self.x1,self.y1)
        plt.plot(self.x2,self.y2)
        plt.grid(True)
        plt.show()


#slope,constant
l1=Line(0,0)
# l1.checkpoints(1,2)
# l1.get_constant()
# l1.get_cooefficient()
#l1.modify_constant(4)
#l1.modify_slope(4)
# l1.get_constant()
# l1.get_cooefficient()

l1.second_line(-1,0)
l1.check_parallel()
l1.check_perpendicular()
l1.visualize_line()