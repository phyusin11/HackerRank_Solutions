cube = lambda x: x ** 3
# complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    fib = list()
    x,y = 0,1
    for i in range(n):
        fib.append(x)
        x,y = y, x+y
    return fib

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
