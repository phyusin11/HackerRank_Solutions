# Enter your code here. Read input from STDIN. Print output to STDOUT

set_a= set(input().split())
n= int(input())
strict_superset= True

for i in range(n):
    set_n =set(input().split())
    if not set_a.issuperset(set_n):
        strict_superset=False
print(strict_superset)