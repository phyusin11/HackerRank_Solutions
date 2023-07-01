# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import groupby

print(*[(len(list(a)), int(x)) for x,a in groupby(input())])
