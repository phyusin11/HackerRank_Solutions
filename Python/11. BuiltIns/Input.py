# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    x, k = map(int, input().strip().split())
    equation = input().strip()
    print(eval(equation) == k)
