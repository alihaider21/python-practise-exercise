def staircase(n):
    a = ' '
    b = '#'
    # Write your code here
    for i in range(1,n+1):
        m = n-i
        print(a * m,b * i,sep='')

n = 5
print(staircase(5))