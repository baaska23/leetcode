# Given an integer N, check whether it is prime or not. A prime number is a number 
# that is only divisible by 1 and itself and the total number of divisors is 2.
def isPrime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

res = isPrime(7)
print(res)