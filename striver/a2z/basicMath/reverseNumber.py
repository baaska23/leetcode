# Input 120
# Output 21

# Input -123
# Output -321

class Solution:
    def reverse(self, x: int) -> int:
        reverse = int(str(abs(x))[::-1])
        if reverse.bit_length()>31:
            return 0
        if x < 0:
            return -1*reverse
        else:
            return reverse