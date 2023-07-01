# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

S = input()
pattern = r'(?<=[^aeiou])([aeiou]{2,})(?=[^aeiou])'
result = re.findall(pattern, S , re.IGNORECASE)
print(*result, sep='\n') if result else print(-1)
    
