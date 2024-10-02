class Solution:
    def sortArray(self, nums: List[int]) -> List[int]: # type: ignore
        if len(nums) > 1:
            mid = len(nums)//2
            left = nums[:mid]
            right = nums[mid:]

            #recursion till 1 1 element
            self.sortArray(left)
            self.sortArray(right)

            #merge back
            i = j = k = 0 #i leftmost j rightmost k sortedArray
            while i<len(left) and j<len(right):
                if left[i] < right[j]:
                    nums[k] = left[i]
                    i+=1
                else:
                    nums[k] = right[j]
                    j+=1
                k+=1
            
            while i<len(left):
                nums[k] = left[i]
                i+=1
                k+=1
            while j<len(right):
                nums[k] = right[j]
                j+=1
                k+=1
        return nums
        