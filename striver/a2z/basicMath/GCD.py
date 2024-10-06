def greatestCommonDivisor(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return a

def leastCommonMultiple(a: int, b: int) -> int:
    return a * b // greatestCommonDivisor(a, b)