n = int(input())
base = set(map(int, input().split()))
m = int(input())
targets = list(map(int, input().split()))

for t in targets:
    if t in base:
        print(1)
    else:
        print(0)
