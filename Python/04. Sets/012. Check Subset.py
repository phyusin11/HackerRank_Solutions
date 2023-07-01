# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())

for i in range(t):
    a, set_a =int(input()), set(input().split())
    b, set_b =int(input()), set(input().split())
    print(set_a.issubset(set_b))
