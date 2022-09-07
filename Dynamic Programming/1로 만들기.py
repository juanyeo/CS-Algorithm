x = int(input())

d5 = dict()
d53 = dict()
d532 = dict()

s = 1
count = 0

while (s * 5) <= x:
    s *= 5
    count += 1
    
    d5[s] = count

s = 1
count = 0

while (s * 3) <= x:
    for e5 in d5:
        if (e5 * s) > x:
            break
        else:
            d53[e5 * s] = count + d5[e5]

    s *= 3
    count += 1
    d53[s] = count

s = 1
count = 0

while (s * 2) <= x:
    for e53 in d53:
        if (e53 * s) > x:
            break
        else:
            d532[e53 * s] = count + d53[e53]

    s *= 2
    count += 1
    d532[s] = count

for e532 in d532:
    d532[e532] += (x - e532)

sort_dict = sorted(d532.items(), key = lambda i: i[1])

print(sort_dict[0][1])



            
