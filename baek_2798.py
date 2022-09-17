n, m = map(int, input().split())
cards = list(map(int, input().split()))

result = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            score = cards[i] + cards[j] + cards[k]
            
            if score <= m and score > result:
                result = score

print(result)
