# Given two integer arrays nums1 and nums2, return an array of their 
# intersection.Each element in the result must be unique and you may return the result in any order.

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]
# Explanation: [4,9] is also accepted.

class Solution(object):
    def intersection(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        return (set1 & set2)

# set is unordered and not duplicated pair of elements
# cannot access set elements set[0] -> not possible