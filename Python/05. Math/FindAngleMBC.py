# Enter your code here. Read input from STDIN. Print output to STDOUT

import math

AB = float(input())
BC = float(input())

#Calculate Hypotenue
AC = math.hypot(AB,BC)
MC= BM = AC/2

# calculating the angle
MBC=round(math.degrees(math.acos(BC/AC))) 

# the 176 represents the degree symbol
degree=chr(176)                          
print(MBC,degree, sep='')
