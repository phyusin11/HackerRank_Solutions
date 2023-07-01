import re
pattern = r"(?<=.)(#[\da-fA-F]{6}|#[\da-fA-F]{3})"
code_lines = int(input())
for i in range(code_lines):
    result = re.findall(pattern,input())
    if result:
        print(*result, sep= '\n')
