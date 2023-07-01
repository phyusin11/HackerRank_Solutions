# Enter your code here. Read input from STDIN. Print output to STDOUT
n,set_n = input(),set(input().split())
b,set_b = input(),set(input().split())
print(len(set_n.difference(set_b)))
