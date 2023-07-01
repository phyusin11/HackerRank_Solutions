# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
country_name= set()
for i in range(n):
    country_name.add(input())
print(len(country_name))
