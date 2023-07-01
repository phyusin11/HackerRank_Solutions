# Enter your code here. Read input from STDIN. Print output to STDOUT

m,set_m = input(),set(map(int, input().split()))
n,set_n = input(),set(map(int, input().split()))
diff =sorted(set_m.difference(set_n).union(set_n.difference(set_m)))
for i in diff:
    print(i)
