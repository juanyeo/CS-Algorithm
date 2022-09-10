text = input()
targ = input()

indexs = []
result = []

for i in range(len(text)):
    a = text[i]
    if targ[0] == a:
        indexs.append(i)
    for start in indexs:
        dif = i - start
        if targ[dif] != a:
            indexs.remove(start)
            continue
        if dif == len(targ) - 1:
            result.append(start)
            indexs.clear()

print(len(result))
