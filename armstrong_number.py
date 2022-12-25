def armstrong(n):
    n1 = n
    m = 0
    while n1 > 0:
        a = n1 % 10
        m += (pow(a,len(str(n))))
        n1 = n1 // 10
    if m == n:
        return True
    else:
        return False

res = armstrong(153)
print(res)