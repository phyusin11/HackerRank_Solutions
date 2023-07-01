# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import OrderedDict
sales  = OrderedDict()

number_of_items = int(input())

for i in range(number_of_items):
 #reversed split for the last space.
    items, price = input().rsplit(' ', 1)
    sales[items]= sales.get(items,0) + int(price)
for items, net_price in sales.items():
    print(f'{items} {net_price}')
