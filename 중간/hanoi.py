def move(n, a, b, c, cnt):
    if n == 1:
        print(a,'->', b)
        print("cnt ==",cnt)
        return
    move(n-1, a, c, b, cnt+1)
    print(a,'->', b)
    move(n-1, c, b, a, cnt+1)

def fib(n, cnt):
    if n == 1 or n == 2:
        return 1
    return fib(n-2, cnt+1) + fib(n-1, cnt+1)

a = fib(7, 0)
print(a)