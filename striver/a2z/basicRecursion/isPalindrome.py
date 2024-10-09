class Solution:
    def isPalindrome(self, s: str) -> bool:
        # Remove spaces and convert to lowercase
        s = s.replace(" ", "").lower()
        
        # Check if the string is empty after removing spaces
        if s == "":
            return True
        
        # Initialize two pointers
        p1 = 0
        p2 = len(s) - 1
        
        # Check if the string is a palindrome
        while p1 < p2:
            if s[p1] != s[p2]:
                return False
            p1 += 1
            p2 -= 1
        
        return True

# Example usage
solution = Solution()
print(solution.isPalindrome("A man a plan a canal Panama"))  # True
print(solution.isPalindrome("race a car"))  # False