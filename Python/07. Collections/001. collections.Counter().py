# Enter your code here. Read input from STDIN. Print output to STDOUT 
from collections import Counter

number_of_shoes  = int(input())
instock_size = list(map(int, input().split()))

number_of_customers = int(input())

total_revenue =0
for i in range(number_of_customers):
    size, price = map(int, input().split())
    if size in instock_size:
        total_revenue += price
        instock_size.remove(size)
print(total_revenue)





