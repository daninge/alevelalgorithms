# Some helper functions

# Swap - swaps the items at index a and b in some_array
def swap(some_array, a, b):
    temp = some_array[b]
    some_array[b] = some_array[a]
    some_array[a] = temp

# Merge - merges two sorted lists a, b into a larger sorted
# list with all of the elements from a, b
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


# Bubble sort
# ---------------
# Best Case O(n^2)
# Average Case O(n^2)
# Worst Case O(n^2)

def bubble_sort(some_array):
    for i in range(0, len(some_array)):
        for j in range(0, len(some_array) - 1):
            if some_array[j] > some_array[j+1]:
                swap(some_array, j, j+1)     

# Insertion sort
# ---------------
# Best Case O(n)
# Average Case O(n^2)
# Worst Case O(n^2)

def insertion_sort(some_array):
    for i in range(0, len(some_array)):
        current_data = some_array[i]
        position = i
        while position > 0 and current_data < some_array[position - 1]:
            some_array[position] = some_array[position - 1]
            position -= 1
        some_array[position] = current_data

# Merge sort
# ---------------
# Best Case O(nlog(n))
# Average Case O(nlog(n))
# Worst Case O(nlog(n))
# Worst Case Space complexity O(n) + O(n) auxiliary

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

# Quicksort
# ---------------
# Best Case O(nlog(n))
# Average Case O(nlog(n))
# Worst Case O(n^2)
# Can be done in place

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

# Linear Search
# ---------------
# Best Case O(1)
# Average Case O(n)
# Worst Case O(n)

def linear_search(some_array, value):
    for i in range(0, len(some_array)):
        if some_array[i] == value:
            return i
    return False

# Binary Search
# ---------------
# Best Case O(1)
# Average Case O(log(n))
# Worst Case O(log(n))

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

if __name__ == "__main__":
    some_array = [4,2,6,4,8,9,0,2,2]
    bubble_sort(some_array)
    #insertion_sort(some_array)
    #some_array = merge_sort(some_array)
    #some_array = quicksort(some_array)
    print(some_array)

