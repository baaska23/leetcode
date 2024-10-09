# Input: arr = [1, 2, 3, 4]
# Output: [4, 3, 2, 1]
class Solution:
    def reverseArray(self, arr):
        n = len(arr)
        p1 = 0
        p2 = n-1
        while p1 < p2:
            arr[p1], arr[p2] = arr[p2], arr[p1]
            p1+=1
            p2-=1
        return arr
    
array = Solution()
print(array.reverseArray([1, 2, 3, 4, 7])) # [7, 4, 3, 2, 1]