n, m = map(int, input().split())

card_list = [[0] * m for _ in range(n)]

for i in range(n):
    card_list[i] = list(map(int, input().split()))

min_list = []
for row in card_list:
    min_list.append(min(row))

print(max(min_list))
