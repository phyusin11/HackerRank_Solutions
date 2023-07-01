import re, email.utils

regex_pattern =r"^([a-zA-Z][a-zA-Z0-9\_\-\.]+)\@[a-zA-Z]+\.[a-zA-Z]{1,3}$"

test_cases = int(input())
for i in range(test_cases):
    name, email_address = email.utils.parseaddr(input())
    if re.match(regex_pattern, email_address, flags = re.I):
        print(email.utils.formataddr((name,email_address)))