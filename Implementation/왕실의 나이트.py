import re

location = input()

columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

row = int(re.sub('[a-z]', '', location))
col = columns.index(re.sub('[1-9]', '', location)) + 1

valid_move_count = 0
for move in moves:
    des_row = row + move[0]
    des_col = col + move[1]

    if des_row < 1 or des_row > 8:
        continue
    if des_col < 1 or des_col > 8:
        continue

    valid_move_count += 1

print(valid_move_count)


