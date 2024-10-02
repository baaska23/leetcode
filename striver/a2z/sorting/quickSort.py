class Solution:
    #in-place
    def partition(self, arr, low, high):
        pivot = arr[high]
        i = low - 1
        for j in range(low, high):
            if arr[j] < pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1

    def quickSort(self, arr, low, high):
        if low < high:
            pi = self.partition(arr, low, high)
            self.quickSort(arr, low, pi - 1)
            self.quickSort(arr, pi + 1, high)
        return arr
    
    #not in-place
    def quickSort2(self, arr):
        pivot = arr[0]
        left = []
        right = []
        for x in arr[1:]:
            if x < pivot:
                left.append(x)
            else:
                right.append(x)
        return self.quickSort2(left) + [pivot] + self.quickSort2(right)