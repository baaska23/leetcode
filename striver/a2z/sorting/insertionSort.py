class Solution:
    def insertionSort(self, arr):
        n = len(arr)
        for i in range(1, n):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
        return arr
sample = Solution()
arr = [64, 215, 132, 222, 11]
print(sample.insertionSort(arr))