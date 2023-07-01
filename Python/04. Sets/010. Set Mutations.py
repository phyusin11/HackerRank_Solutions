# Enter your code here. Read input from STDIN. Print output to STDOUT
#a= no. of elements in set A, n= number of other sets
a,set_a= int(input()), set(map(int,input().split()))
n=  int(input())
for i in range(n):
    cmd = input().split()[0]
    new_set = set(map(int,input().split()))
    if cmd == 'update':
        set_a.update(new_set)
    elif cmd=='intersection_update':
        set_a.intersection_update(new_set)
    elif cmd=='difference_update':
        set_a.difference_update(new_set)
    elif cmd=='symmetric_difference_update':
        set_a.symmetric_difference_update(new_set)
        
print(sum(set_a))
    
    
