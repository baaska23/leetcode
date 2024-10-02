class Solution:
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n):
            min = i
            for j in range(i+1, n):
                if arr[j] < arr[min]:
                    min = j
            arr[i], arr[min] = arr[min], arr[i]
        return arr

sample = Solution()
arr = [64, 25, 12, 22, 11]
print(sample.selectionSort(arr))   