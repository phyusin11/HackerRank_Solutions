# Enter your code here. Read input from STDIN. Print output to STDOUT
height, length = map(int, input().split())
s1 = '.|.'
s2='WELCOME'

#for upper part 1
for i in range(0, height // 2):
    print((s1*((i * 2)+1)).center(length,'-'))
    
#for middle part 2
print('WELCOME'.center(length, '-'))

#for last part 3
for i in range(height // 2 - 1, -1, -1):
    print((s1*((i * 2)+1)).center(length,'-'))
