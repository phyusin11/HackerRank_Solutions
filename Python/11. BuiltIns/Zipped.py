# Enter your code here. Read input from STDIN. Print output to STDOUT


StudentID , Subject = map(int,(input().split()))
marks =[]

for i in range(Subject):
    marks.append(list(map(float,input().split())))
for j in zip(*marks):
    print( sum(j)/Subject)

