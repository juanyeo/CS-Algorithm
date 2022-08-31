graph = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5],
         [3, 4], [7], [2, 6, 8], [1, 7]]

def dfs(graph, current, visited):
    visited.append(current)
    print(current, end=' ')

    for node in graph[current]:
        if node not in visited:
            dfs(graph, node, visited)

print('--- dfs ---')
dfs(graph, 1, [])

from collections import deque

def bfs(graph, start, visited):
    visited.append(start)
    queue = deque([start])

    while queue:
        cur = queue.popleft()
        print(cur, end=' ')

        for node in graph[cur]:
            if node not in visited:
                queue.append(node)
                visited.append(node)

print('\n--- bfs ---')
bfs(graph, 1, [])
    
    
