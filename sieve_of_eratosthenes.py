def primes_to_n(n):
    """Return a list of all primes <= n (Sieve of Eratosthenes)."""

    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    primes = []
    for i in range(2, n+1):
        if i**2 > n:
            break
        if not sieve[i]:
            continue
        for j in range(i*i, n+1, i):
            sieve[j] = False
    for i in range(2, n+1):
        if sieve[i]:
            primes.append(i)
    return primes

result_25 = primes_to_n(25)
result_49 = primes_to_n(49)
result_100 = primes_to_n(100)
print(result_25, result_49, result_100)
print(f"There are {len(result_25)} primes up to 25, {len(result_49)} up to 49 and {len(result_100)} up to 100.")
