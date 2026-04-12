# pcost.py
#
# Exercise 1.27# import gzip
# with gzip.open('Data/portfolio.csv.gz','rt') as f:
#     for line in f:
#         print(line,end='')
import sys
from report import read_portfolio
def portfolio_cost(filename):
        lines = read_portfolio(filename)
        total_money = 0.0
        for line in lines:
            if len(line) < 3:
                continue
            try:
                 money = line['shares']*line['price']
                 total_money += money
            except ValueError:
                print('warning!!')
                continue
        return total_money
if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv'
try:
    cost = portfolio_cost(filename)
    print ('Total cost:',cost)
except ValueError:
    print('warning!!')





