input_ = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

def selection_sort(array):
    for i in range(len(array)):
        min_i = i
        for j in range(i+1, len(array)):
            if array[j] < array[min_i]:
                min_i = j
        array[i], array[min_i] = array[min_i], array[i]
        
    return array

#print(selection_sort(input_))

def insertion_sort(array):
    for i in range(1, len(array)):
        for j in range(i, 0, -1):
            if array[j] < array[j-1]:
                array[j], array[j-1] = array[j-1], array[j]
            else:
                break
            
    return array

#print(insertion_sort(input_))

def quick_sort(array, start, end):
    if start >= end:
        return

    pivot = start
    left = start + 1
    right = end

    while right >= left:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1

        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

#quick_sort(input_, 0, len(input_)-1)
#print(input_)

def quick_sort2(array):
    if len(array) <= 1:
        return array

    pivot = array[0]
    others = array[1:]

    left_sorted = [e for e in others if e <= pivot]
    right_sorted = [e for e in others if e > pivot]

    return quick_sort2(left_sorted) + [pivot] + quick_sort2(right_sorted)

#print(quick_sort2(input_))

def count_sort(array):
    counting_list = [0] * (max(array) + 1)

    for e in array:
        counting_list[e] += 1

    for i in range(len(counting_list)):
        for _ in range(counting_list[i]):
            print(i, end=' ')

#count_sort(input_)
    
