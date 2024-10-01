# Input: arr = [12, 35, 1, 10, 34, 1]
# Output: 34
# Explanation: The largest element of the array is 35 and the second largest element is 34.
class Solution:
    def getSecondLargest(self, arr):
        large = float('-inf')
        secondLarge = float('-inf')

        for x in arr:
            if x > large:
                secondLarge = large
                large = x
            elif x > secondLarge and x != large:
                secondLarge = x
        return secondLarge