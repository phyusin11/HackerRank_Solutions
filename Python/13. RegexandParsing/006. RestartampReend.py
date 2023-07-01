# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
mainstring = input()
substring  = input()

pattern = re.compile(substring)
match = pattern.search(mainstring)

if not match:
    print((-1,-1))
while match:
    print((match.start(), match.end()-1))
    match= pattern.search(mainstring, match.start()+1)
