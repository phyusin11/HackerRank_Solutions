# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools

# Read inputs
K , M = list(map(int, input().split()))

#creating lists for K lines

List_N = []
for i in range(K):
    N = list(map(int,input().split()))
    N = N[1:]
    List_N.append(N)

# Generate all possible combinations of elements from the K lists
products_list = list(itertools.product(*List_N))

# Calculate the maximum sum modulo M among all combinations
ListMaximum_S= [sum( x ** 2 for x in lst)%M for lst in products_list] 

print(max(ListMaximum_S))