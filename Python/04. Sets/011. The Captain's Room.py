# Enter your code here. Read input from STDIN. Print output to STDOUT
groupSize_K = int(input())
room_numberList = list(map(int,input().split()))
actual_roomList = list(set(room_numberList))* groupSize_K
difference = sum(actual_roomList)-sum(room_numberList)
print(int(difference/(groupSize_K-1)))
