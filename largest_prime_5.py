# LARGEST PRIME FACTOR - 5%
def primes(n):
    factors = {1}
    while n % 2 == 0:
        factors.add(2)
        n /= 2
    for i in range(3, int(n/3), 2):
        while n % i == 0:
            factors.add(i)
            n /= i
        if i > n:
            break
    if len(factors) == 1:
        return n
    else:
        return max(factors)
            