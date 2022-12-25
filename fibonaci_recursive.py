# def rec_fib(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#             return rec_fib(n-1) + rec_fib(n-2)


def Fibonacci(n):
    if n<= 0:
        print("Incorrect input")
    # First Fibonacci number is 0
    elif n == 1:
        return 0
    # Second Fibonacci number is 1
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2)

n  = 10
print(Fibonacci(n)) 
