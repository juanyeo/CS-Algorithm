n = int(input())
part_n = list(map(int, input().split()))

m = int(input())
part_m = list(map(int, input().split()))

def binary_search(target):
    array = part_n
    
    start = 0
    end = len(array) - 1
    pivot = (start + end) // 2

    while start < end:
        if array[pivot] == target:
            return True
        elif array[pivot] > target:
            end = pivot - 1
        else:
            start = pivot + 1
        pivot = (start + end) // 2
    return False

result = list(map(binary_search, part_m))

print(result)
