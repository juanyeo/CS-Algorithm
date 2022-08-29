n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
first, second = numbers[n-1], numbers[n-2]

result = (first * k + second) * (m // (k+1)) + (first * (m % (k+1)))

print(result)
