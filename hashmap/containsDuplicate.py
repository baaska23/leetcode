# Input: nums = [1,2,3,1]
# Output: true
# The element 1 occurs at the indices 0 and 3.

# Input: nums = [1,2,3,4]
# Output: false

class Solution(object):
    def containsDuplicate(self, nums):
        dictionary = {}
        for num in nums:
            dictionary[num] = dictionary.get(num, 0)+1
        for key, value in dictionary.items():
            if value > 1:
                return True
        return False
        