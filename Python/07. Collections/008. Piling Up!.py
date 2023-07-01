# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import deque

test_cases = int(input())

for t in range(test_cases):
    size_block , list_block = int(input()), deque(map(int, input().split()))
    answer = True
    for i in range(len(list_block)-1):
        if list_block[0] >= list_block[1]:
            list_block.popleft()
        elif list_block[-1] >= list_block[-2]:
            list_block.pop()
        else:
            answer = False
            break
    if answer:
        print('Yes')
    else:
        print('No')
            

