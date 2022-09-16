n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))
    
print(*sorted(array), sep='\n')
