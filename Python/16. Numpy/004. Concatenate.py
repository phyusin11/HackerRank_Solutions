import numpy
N,M,P= map(int,input().split())
array_N = numpy.array([input().split() for _ in range(N)],int)
array_M = numpy.array([input().split() for _ in range(M)],int)
print(numpy.concatenate((array_N,array_M)))
