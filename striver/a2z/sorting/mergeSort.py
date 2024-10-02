def merge(arr, low, mid, high):
    temp = []  # temporary array
    left = low  # starting index of left half of arr
    right = mid + 1  # starting index of right half of arr

    # storing elements in the temporary array in a sorted manner
    while left <= mid and right <= high:
        if arr[left] <= arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1

    # if elements on the left half are still left
    while left <= mid:
        temp.append(arr[left])
        left += 1

    # if elements on the right half are still left
    while right <= high:
        temp.append(arr[right])
        right += 1

    # transferring all elements from temporary to arr
    for i in range(low, high + 1):
        arr[i] = temp[i - low]

def mergeSort(arr, low, high):
    if low >= high:
        return
    mid = (low + high) // 2
    mergeSort(arr, low, mid)  # left half
    mergeSort(arr, mid + 1, high)  # right half
    merge(arr, low, mid, high)  # merging sorted halves

# Example usage
arr = [64, 25, 12, 22, 11]
mergeSort(arr, 0, len(arr) - 1)
print(arr)