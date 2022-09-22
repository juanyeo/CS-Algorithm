n = int(input())
result = []

for _ in range(n):
    keyset = input()

    head = []
    tail = [] # reversed

    for s in keyset:
        if s == '<':
            if head:
                tail.append(head.pop())
        elif s == '>':
            if tail:
                head.append(tail.pop())
        elif s == '-':
            if head:
                head.pop()
        else:
            head.append(s)
    
    result.append(''.join(head + tail[::-1]))

print(*result, sep='\n')
