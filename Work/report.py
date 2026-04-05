# report.py
#
# Exercise 2.4
import csv
def read_portfolio(filename):
    with  open(filename,'rt') as f:
        portfolio = []
        lines = csv.reader(f)
        header = next(lines)
        for line in lines:
            if len(line) < 3:
                continue
            try:
                row = {'name':line[0],'shares':int(line[1]),'price':float(line[2])}
                portfolio.append(row)
            except ValueError:
                print('warning!!!')
                continue
    return portfolio
def read_price(filename):
    with open(filename,'rt') as f:
        prices = {}
        lines = csv.reader(f)
        for line in lines:
            if len(line) < 2:
                print('warning!!!')
                continue
            try:
                prices[line[0]] = float(line[1]) 
            except ValueError:
                continue
    return prices
portfolio = read_portfolio('Data/portfolio.csv')
prices = read_price('Data/prices.csv')
total_profit = 0.0
profit = 0.0
for row in portfolio:
    name = row['name']
    shares = row['shares']
    xprice = row['price']
    price = prices[name]
    profit = shares*(xprice-price)
    print(f'name:{name},profit:{profit:.2f}')
    total_profit += profit
print('total_profit:',total_profit)
total_cost = 0.0
cost = 0.0
for row in portfolio:
    cost = row['shares']*row['price']
    total_cost += cost;
print(f'total_cost:{total_cost:.2f}')






