n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

def dfs(r, c):
    if r < 0 or c < 0 or r >= n or c >= m:
        return False

    if graph[r][c] == 0:
        graph[r][c] = 1

        dfs(r-1, c)
        dfs(r, c-1)
        dfs(r+1, c)
        dfs(r, c+1)
        return True
    return False

block_count = 0

for r in range(n):
    for c in range(m):
        if dfs(r, c):
            block_count += 1

print(block_count)
