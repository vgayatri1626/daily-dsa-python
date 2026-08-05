p= list(map(int, input("Enter stock prices: ").split()))
min_price = p[0]
max_profit = 0
for price in p:
    if price < min_price:
        min_price = price
    profit = price - min_price
    if profit > max_profit:
        max_profit = profit
print("Maximum Profit:", max_profit)