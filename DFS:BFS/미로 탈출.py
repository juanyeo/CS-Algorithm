n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

from collections import deque

def bfs(r, c):
    queue = deque()
    queue.append((r, c))

    while queue:
        loc = queue.popleft()

        for move in moves:
            nr = loc[0] + move[0]
            nc = loc[1] + move[1]

            if nr < 0 or nc < 0 or nr >= n or nc >= m:
                continue

            if graph[nr][nc] == 1:
                graph[nr][nc] = graph[loc[0]][loc[1]] + 1
                queue.append((nr, nc))

    return graph[n-1][m-1]

print(bfs(0, 0))
                
