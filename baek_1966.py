result = []
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    plist = list(map(int, input().split()))
    target = m
    count = 0

    while plist:
        if plist[0] < max(plist):
            # 뒤로 재배치
            a = plist.pop(0)
            plist.append(a)
        
            if target == 0:
                target = len(plist) - 1
            else:
                target -= 1
        else:
            count += 1
            # 프린팅
            if target == 0:
                result.append(count)
                break
            else:
                plist.pop(0)
                target -= 1

print(*result, sep='\n')
