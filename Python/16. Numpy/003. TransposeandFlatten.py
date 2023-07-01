import numpy 

N , M = map(int, input().split())

my_array = numpy.array([input().split() for _ in range(N)], int)
print(my_array.transpose())
print(my_array.flatten())