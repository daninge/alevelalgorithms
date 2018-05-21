def bubble_sort_1(some_array):
    for i in range(0, len(some_array)):
        for j in range(0, len(some_array) - 1):
            if some_array[j] > some_array[j+1]:
                temp = some_array[j+1]
                some_array[j+1] = some_array[j]
                some_array[j] = temp      

def bubble_sort_2(some_array):
    for i in range(0, len(some_array)):
        j = 0
        while j < len(some_array) - i - 1:
            if some_array[j] > some_array[j+1]:
                temp = some_array[j+1]
                some_array[j+1] = some_array[j]
                some_array[j] = temp
            j += 1

def insertion_sort(some_array):
    for i in range(0, len(some_array)):
        current_data = some_array[i]
        position = i
        while position > 0 and current_data < some_array[position - 1]:
            some_array[position] = some_array[position - 1]
            position -= 1
        some_array[position] = current_data

def merge(a, b):
    to_return = []
    while len(a) !=0 or len(b) != 0:
        if len(a) == 0:
            return to_return + b
        elif len(b) == 0:
            return to_return + a
        else:
            if a[0] > b[0]:
                to_return += [b.pop(0)]
            else:
                to_return += [a.pop(0)]



def merge_sort(some_array):
    l = len(some_array)
    if l == 1:
        return some_array
    elif l == 2:
        if some_array[0] > some_array[1]:
            return [some_array[1], some_array[0]]
        else:
            return some_array
    else:
        return merge(merge_sort(some_array[:l/2]), merge_sort(some_array[l/2:]))


def quicksort(some_array, pivot_index=0):

    #the list is already sorted
    if len(some_array) <= 1:
        return some_array

    pivot = some_array[pivot_index]
    less = []
    equal = []
    greater = []

    for item in some_array:
        if item < pivot:
            less.append(item)
        elif item == pivot:
            equal.append(item)
        else:
            greater.append(item)

    return quicksort(less)+equal+quicksort(greater)


def binary_search(some_ordered_array, value):
    left = 0
    right = len(some_ordered_array) - 1
    while left <= right:
        middle = (left + right) / 2
        if some_ordered_array[middle] == value:
            return middle
        elif some_ordered_array[middle] < value:
            left = middle + 1
        else:
            right = middle - 1
    return False


some_array = [4,2,6,4,8,9,0,2,2]
#bubble_sort_1(some_array)
#insertion_sort(some_array)
#some_array = merge_sort(some_array)
some_array = quicksort(some_array)
print(some_array)

print(binary_search(some_array, 3))
