# Binary Search

def binary_search(array, target):
    start = 0
    end = len(array)
    pivot = (start + end) // 2

    while start <= end:
        if array[pivot] == target:
            return pivot
        elif array[pivot] < target:
            start = pivot + 1
        else:
            end = pivot - 1
    return None

# print(binary_search([1, 2, 3, 4, 5], 3))

def binary_search(array, target, start, end):
    pivot = (start + end) // 2

    while start <= end:
        if array[pivot] == target:
            return pivot
        elif array[pivot] < target:
            return binary_search(array, target, pivot + 1, end)
        else:
            return binary_search(array, target, start, pivot - 1)
    return None

# print(binary_search([1, 2, 3, 4, 5], 3, 0, 4))
