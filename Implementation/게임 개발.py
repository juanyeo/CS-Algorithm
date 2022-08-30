n, m = map(int, input().split())

x, y, direc = map(int, input().split())

game_map = [[0] * m for _ in range(n)]

left_dir = [(0, -1), (-1, 0), (0, 1), (1, 0)]
back_dir = [(1, 0), (0, -1), (-1, 0), (0, 1)]

for i in range(n):
    game_map[i] = list(map(int, input().split()))

while True:
    four_dir = []
    for j in range(len(left_dir)):
        nx = x + left_dir[j][1]
        ny = y + left_dir[j][0]

        four_dir.append(game_map[ny][nx])

    if min(four_dir) > 0:
        game_map[y][x] = 2
        x = x + back_dir[direc][1]
        y = y + back_dir[direc][0]

        if game_map[y][x] == 1:
            break
    else:
        if four_dir[direc] == 0:
            game_map[y][x] = 2
            x = x + left_dir[direc][1]
            y = y + left_dir[direc][0]
        direc = (direc + 3) % 4
    
print(sum(row.count(2) for row in game_map))
