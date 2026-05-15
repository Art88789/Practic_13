def sieve_of_eratosthenes(n):
    """Возвращает список всех простых чисел меньше n, используя решето Эратосфена и множества."""
    if n <= 2:
        return []

    numbers = set(range(2, n))
    primes = []

    while numbers:
        p = min(numbers)
        primes.append(p)
        multiples = set(range(p, n, p))
        numbers -= multiples

    return primes

n = int(input())
print(*sieve_of_eratosthenes(n))
    
