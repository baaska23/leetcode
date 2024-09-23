# Given a string s, find the first non-repeating character in it and return its index. 
# If it does not exist, return -1.

# Input: s = "loveleetcode"
# Output: 2

class Solution(object):
    def firstUniqChar(self, s):
        dic = {}

        for char in s:
            dic[char] = dic.get(char, 0) + 1
        
        for index, char in enumerate(s):
            if dic[char] == 1:
                return index
        return -1

# s = "abcde"
# index = 0
# for char in s:
#     print(f"Index: {index}, Character: {char}")
#     index += 1   

        