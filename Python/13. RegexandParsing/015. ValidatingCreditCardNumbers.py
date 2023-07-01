# Enter your code here. Read input from STDIN. Print output to STDOUT

import re 
test_cases= int(input())
for i in range(test_cases):
    card_numbers =input()
    pattern1 = r'^[456]\d{3}-?\d{4}-?\d{4}-?\d{4}$'
    pattern2 = r'(.)\1{3}'
    x2 = re.sub('-','',card_numbers)
    if re.fullmatch(pattern1,card_numbers) and not re.findall(pattern2,x2):
        print('Valid')
    else:
        print('Invalid')