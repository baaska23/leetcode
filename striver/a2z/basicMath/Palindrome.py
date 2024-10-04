def isPalindrome(x: int) -> bool:
    if x < 0:
        return False
    remainder = 0
    temp = x
    while temp != 0:
        remainder = remainder * 10 + temp % 10
        temp = temp // 10
    return x == remainder
sampleInput = 121
print(isPalindrome(sampleInput)) # True
