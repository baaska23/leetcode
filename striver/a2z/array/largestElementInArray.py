from typing import List


class Solution:
    def largest(self, arr : List[int]) -> int:
        max = arr[0]
        for x in arr:
            if x > max:
                max = x
        return max