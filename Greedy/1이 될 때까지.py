n, k = map(int, input().split())

iteration = 0

while n > 1:
    if n % k == 0:
        n = n // k
    else:
        n = n - 1
    iteration += 1

print(iteration)
