# Input: s = "leEeetcode"
# Output: "leetcode"
# Explanation: In the first step, either you choose i = 1 or i = 2, both will result "leEeetcode" to be reduced to "leetcode".

# Input: s = "abBAcC"
# Output: ""
# Explanation: We have many possible scenarios, and all lead to the same answer. For example:
# "abBAcC" --> "aAcC" --> "cC" --> ""
# "abBAcC" --> "abBA" --> "aA" --> ""
class Solution(object):
    def makeGood(self, s):
        stack = []

        for char in s:
            if stack and abs(ord(char)-ord(stack[-1])) == 32:
                stack.pop()
            else:
                stack.append(char)
        return "".join(stack)
        