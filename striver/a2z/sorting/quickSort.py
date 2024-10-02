def partition(arr, low, high):
    i = low
    j = high-1
    pivot = arr[high]
    while i<j:
        if arr[i] > pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j -= 1
        else:
            i += 1
    if arr[i] > pivot:
        arr[i], arr[high] = arr[high], arr[i]
    return i

def quickSort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quickSort(arr, low, pi - 1)
        quickSort(arr, pi + 1, high)

arr = [10, 7, 8, 9, 1, 5]
n = len(arr)
quickSort(arr, 0, n - 1)
print("Sorted array:", arr)

# def quickSort2(arr):
#     if len(arr) <= 1:
#         return arr
#     pivot = arr[len(arr) // 2]
#     left = [x for x in arr if x < pivot]
#     middle = [x for x in arr if x == pivot]
#     right = [x for x in arr if x > pivot]
#     return quickSort(left) + middle + quickSort(right)

# arr = [10, 7, 8, 9, 1, 5]
# sorted_arr = quickSort2(arr)
# print("Sorted array:", sorted_arr)