# Given a list of daily stock prices, write a program to calculate the average stock price.


stock_prices = [100, 102, 104, 106, 108, 110]

sum=0
for i in range(len(stock_prices)-1):
    sum=sum+stock_prices[i]


avrage=sum/len(stock_prices)

print("Average stock price is Given below")
print(round(avrage,2))