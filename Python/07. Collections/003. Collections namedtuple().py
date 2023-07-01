# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import namedtuple

total_students = int(input())
Student = namedtuple('Student', input().split())

total_marks= sum([int(Student(*input().split()).MARKS) for i in range (total_students)])
average_marks = total_marks/total_students
print('{:.2f}'.format(average_marks))
