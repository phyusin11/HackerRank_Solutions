# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
n = int(input())

for i in range(n):
    line = input()
    remove_and = re.sub(r'(?<= )(&&)(?= )',"and",line)
    remove_or = re.sub(r'(?<= )(\|\|)(?= )',"or",remove_and)
    print(remove_or,sep='\n')


