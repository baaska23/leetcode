# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by 
# using the letters from magazine and false otherwise. Each letter in magazine can only be used once in ransomNote.

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        char_count = {}
        for char in magazine:
            char_count[char] = char_count.get(char, 0) + 1
        
        for char in ransomNote:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char]-=1
        return True
        