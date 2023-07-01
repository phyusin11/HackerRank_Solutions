# Enter your code here. Read input from STDIN. Print output to STDOUT

import re

regex_pattern = r'^[789]\d{9}$'
test_cases = int(input())


for i in range(test_cases):
    phone_number = input()
    if re.fullmatch(regex_pattern,phone_number):
        print('YES')
    else:
        print('NO')
