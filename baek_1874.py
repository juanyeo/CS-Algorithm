n = int(input())
actions = []
stack = []
count = 1

for i in range(1, n+1):
    d = int(input())
    while count <= d:
        stack.append(count)
        actions.append('+')
        count += 1
    if stack[len(stack)-1] == d:
        stack.pop()
        actions.append('-')
    else:
        print('NO')
        exit(0)

print('\n'.join(actions))
