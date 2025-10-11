# Implement a function to calculate the return on investment (ROI) given an initial and final
# list of stock prices.

price=[100,150,200,250,300,350]

def roi_cal(price):
    x=price[0]
    y=price[-1]
    roi=(((y-x)/x)*100)
    return roi

print(roi_cal(price))

