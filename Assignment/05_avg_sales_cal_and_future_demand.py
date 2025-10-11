# Given a list of past monthly sales, calculate the average sales to predict next month’s
# demand. (Supply Chain)
sales=[120,132,129,139,140,148]

average=sum(sales)/len(sales)


print("The average sales of next month is")
print(round(average,2))

