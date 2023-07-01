# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath

z = complex(input())
r,o = cmath.polar(z)
print(r , o, sep='\n')
