notes = list(map(int, input().split()))

ascending = sorted(notes)
descending = sorted(notes, reverse=True)
isascending = True
isdescending = True

for i in range(len(notes)):
    if notes[i] != ascending[i]:
        isascending = False
    if notes[i] != descending[i]:
        isdescending = False

if isascending:
    print('ascending')
elif isdescending:
    print('descending')
else:
    print('mixed')
