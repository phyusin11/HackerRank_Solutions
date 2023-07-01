# Enter your code here. Read input from STDIN. Print output to STDOUT

import re
S= input()
if 0< len(S) < 100:
    output = re.search(r"([a-z0-9A-Z])\1+",S)
    if output:
        print(output.group(1))
    else:
        print(-1)
 
 
