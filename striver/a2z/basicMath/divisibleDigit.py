#Given an integer num, return the number of digits in num that divide num.
# Input: num = 121
# Output: 2
# Explanation: 121 is divisible by 1, but not 2. Since 1 occurs twice as a digit, we return 2.

# Input: num = 1248
# Output: 4
# Explanation: 1248 is divisible by all of its digits, hence the answer is 4.
class Solution:
    def countDigits(self, num: int) -> int:
        digit = []
        temp = num
        while temp > 0:
            remaining = temp % 10
            digit.append(remaining)
            temp = temp // 10
        # now digit[] has [1,2,1]
        score = 0
        for i in range(len(digit)):
            if num % digit[i] == 0:
                score +=1
        return score
# /  floating-point division
# // integer-division
# if while temp > 1 were, it would miss the last digit if temp became 1
