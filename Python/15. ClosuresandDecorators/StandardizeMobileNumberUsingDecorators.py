
# Enter your code here. Read input from STDIN. Print output to STDOUT
# n=int(input())
# ar=[]
# for i in range(0,n):
#     tmp_str=input()
#     tmp_str=tmp_str[len(tmp_str)-10:]
#     ar.append(tmp_str)
    
# ar.sort()
# for i in range(0,len(ar)):
#     print "+91 "+ar[i][:5]+" "+ar[i][5:]

def wrapper(f):
    def fun(l):
        # complete the function
            fun= f([f'+91 {i[-10:-5]} {i[-5:]}' for i in l])
    return fun

@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 


