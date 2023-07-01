# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import *

s , n = list(map(str, input().split()))
n= int(n)
s= sorted(s)
for i in combinations_with_replacement(s,n):
    print(''.join(i))
