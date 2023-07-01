# Enter your code here. Read input from STDIN. Print output to STDOUT


import re

test_cases = int(input())
uppercase_check = r'^(.*[A-Z]){2,}.*$'
digit_check = r'.*\d.*\d.*\d.*'
alphanumeric_and_length_check = r'^[a-zA-Z0-9]{10}$'
repeat_check = r'.*(.).*\1.*'

for i in range(test_cases):
    UIDstring = input().strip()
    uppercase_check_result = bool(re.match(uppercase_check, UIDstring))
    digit_check_result = bool(re.match(digit_check, UIDstring))
    alphanumeric_and_length_check_result = bool(re.match(alphanumeric_and_length_check, UIDstring))
    repeat_check_result = bool(re.match(repeat_check, UIDstring))
    if uppercase_check_result and digit_check_result and alphanumeric_and_length_check_result and not repeat_check_result:
        print('Valid')
    else:
        print('Invalid')
