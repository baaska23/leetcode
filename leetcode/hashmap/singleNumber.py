# Given a non-empty array of integers nums, every element 
# appears twice except for one. Find that single one.

# Input: nums = [2,2,1]
# Output: 1
# Example 2:

# Input: nums = [4,1,2,1,2]
# Output: 4

class Solution:
    def singleNumber(self, nums):
        freq_map = {}    
        for num in nums:
            freq_map[num] = freq_map.get(num, 0) + 1
        
        for key, value in freq_map.items():
            if value == 1:
                return key
        return result
#   First iteration (num = 3):
# 	•	freq_map.get(3, 0) returns 0 (because 3 isn’t in freq_map yet).
# 	•	So freq_map[3] = 0 + 1, making freq_map = {3: 1}.
# 	2.	Second iteration (num = 1):
# 	•	freq_map.get(1, 0) returns 0 (because 1 isn’t in freq_map yet).
# 	•	So freq_map[1] = 0 + 1, making freq_map = {3: 1, 1: 1}.
# 	3.	Third iteration (num = 3):
# 	•	freq_map.get(3, 0) returns 1 (because 3 is already in freq_map with value 1).
# 	•	So freq_map[3] = 1 + 1, making freq_map = {3: 2, 1: 1}.
# 	4.	Fourth iteration (num = 2):
# 	•	freq_map.get(2, 0) returns 0 (because 2 isn’t in freq_map yet).
# 	•	So freq_map[2] = 0 + 1, making freq_map = {3: 2, 1: 1, 2: 1}.
# 	5.	Fifth iteration (num = 1):
# 	•	freq_map.get(1, 0) returns 1 (because 1 is already in freq_map with value 1).
# 	•	So freq_map[1] = 1 + 1, making freq_map = {3: 2, 1: 2, 2: 1}.
# 	6.	Sixth iteration (num = 3):
# 	•	freq_map.get(3, 0) returns 2 (because 3 is already in freq_map with value 2).
# 	•	So freq_map[3] = 2 + 1, making freq_map = {3: 3, 1: 2, 2: 1}.