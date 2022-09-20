case = int(input())
result = []

def find(x):
    if x == parent[x]:
        return x
    else:
        p = find(parent[x])
        parent[x] = p
        return p

def union(x, y):
    x = find(x)
    y = find(y)

    if x != y:
        parent[y] = x
        number[x] += number[y]

for _ in range(case):
    parent = dict()
    number = dict()
    
    f = int(input())

    for _ in range(f):
        first, second = input().split()

        if first not in parent:
            parent[first] = first
            number[first] = 1
        if second not in parent:
            parent[second] = second
            number[second] = 1

        union(first, second)
        print(number[find(first)])
