def mergeSort(arr):
    if len(arr) > 1:
        # Finding the middle of the array
        mid = len(arr) // 2

        # Dividing the array into two halves
        left_half = arr[:mid]
        right_half = arr[mid:]

        # Sorting the first half
        mergeSort(left_half)

        # Sorting the second half
        mergeSort(right_half)

        # Merging the two halves
        i = j = k = 0

        # Copy data to the original array from the temp arrays
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # Checking if any element was left in the left half
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        # Checking if any element was left in the right half
        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

# Test the function
arr = [38, 27, 43, 3, 9, 82, 10]
print("Original array:", arr)
mergeSort(arr)
print("Sorted array:", arr)