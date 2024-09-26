def quicksort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = [x for x in arr[1:] if x < pivot]
    right = [x for x in arr[1:] if x >= pivot]
    return quicksort(left) + [pivot] + quicksort(right)

print(quicksort([3, 6, 8, 10, 1, 2, 1]))


def quicksort2(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    left = []
    right = []
    for x in arr[1:]:
        if x < pivot:
            left.append(x)
        else:
            right.append(x)
    return quicksort2(left) + [pivot] + quicksort2(right)
print(quicksort2([3, 6, 8, 10, 1, 2, 1]))


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i+1

def quicksort3(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort3(arr, low, pi-1)
        quicksort3(arr, pi+1, high)
    return arr
print(quicksort3([3, 6, 8, 10, 1, 2, 1], 0, 6))