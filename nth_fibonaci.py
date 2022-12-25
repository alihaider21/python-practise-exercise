def fabonacci(n):
    a,b = 0,1
    if n < 0:
        print("Incorrect input")
    elif n == a:
        return b
    elif n == b:
        return b
    else:
        for i in range(2,n):
            c = a+b
            a = b
            b = c
        return b
print(fabonacci(10))