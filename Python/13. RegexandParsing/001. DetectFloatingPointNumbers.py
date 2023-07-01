# Enter your code here. Read input from STDIN. Print output to STDOUT
from re import fullmatch
# identifying Floating point number


Test_cases = int(input())
for i in range(Test_cases):
    regex = r'^[+-]?\d*[.]\d+$'
    print(bool(fullmatch(regex,input())))
    
