data_store = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1

    if data_store[x] != 0:
        return data_store[x]

    data_store[x] = fibo(x-1) + fibo(x-2)
    return data_store[x]

def fibo2(x):
    data_store[1] = 1
    data_store[2] = 1

    for i in range(3, x + 1):
        data_store[i] = data_store[i-1] + data_store[i-2]

    return data_store[x]

print(fibo2(12))
