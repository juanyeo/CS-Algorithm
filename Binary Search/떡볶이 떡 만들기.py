n, m = map(int, input().split())

cakes = list(map(int, input().split()))
cakes.sort()

max_h = cakes[len(cakes) - 1]

for h in range(max_h, 0, -1):
    start = 0
    end = len(cakes) - 1

    while start <= end:
        pivot = (start + end) // 2
        
        if cakes[pivot] == h:
            break
        elif cakes[pivot] > h:
            end = pivot - 1
        else:
            start = pivot + 1

    extra = 0
    
    for i in range(pivot, len(cakes)):
        extra += cakes[i] - h

    if extra >= m:
        max_h = h
        break

print(max_h)
