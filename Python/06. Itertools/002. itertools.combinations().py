# Enter your code here. Read input from STDIN. Print output to STDOUT

import itertools
s = input().split()
s, n = sorted(s[0]), int(s[1])
for i in range(1, n + 1):
    print(*list(map(''.join, itertools.combinations(s, i))), sep='\n')
