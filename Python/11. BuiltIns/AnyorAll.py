# Enter your code here. Read input from STDIN. Print output to STDOUT

N = int(input())
number_list = list(input().split())

# Check if all numbers are positive and at least one is palindromic

print(all(int(i)>0 for i in number_list) and any( [i==i[::-1]for i in number_list]))
