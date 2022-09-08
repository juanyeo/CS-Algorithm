N, r, c = map(int, input().split())

count = 0
r += 1
c += 1

for i in reversed(range(N)):
    a = pow(2, i)
    if r > a: # i=2, 4 16, i=1, 2 4, i=0 1 1
        count += 2 * pow(4, i)
        r -= a
    if c > a:
        count += pow(4, i)
        c -= a

print(count)
