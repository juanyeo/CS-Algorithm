n = int(input())
d = [0] * 50
d[1] = 1
d[2] = 1

def fibo(n):
    if d[n] != 0:
        return d[n]
    else:
        d[n] = fibo(n-1) + fibo(n-2)
        return d[n]
    
print(fibo(n))
