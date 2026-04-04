# pcost.py
#
# Exercise 1.27# import gzip
# with gzip.open('Data/portfolio.csv.gz','rt') as f:
#     for line in f:
#         print(line,end='')
import sys
def portfolio_cost(filename):
    with open(filename,'rt') as f:
        import csv
        lines = csv.reader(f)
        header= next(lines)
        total_money = 0.0
        for line in lines:
            if len(line) < 3:
                continue
            try:
                 money = float(int(line[1])*float(line[2]))
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





