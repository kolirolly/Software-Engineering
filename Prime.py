import math


def initialize_sieve(limit):
    """Initialize a boolean list for the sieve of Eratosthenes."""
    sieve = [True] * (limit + 1)
    sieve[0] = sieve[1] = False  # 0 and 1 are not prime
    return sieve


def apply_sieve(sieve):
    """Mark non-prime numbers in the sieve."""
    for num in range(2, int(math.sqrt(len(sieve))) + 1):
        if sieve[num]:  # If prime, mark its multiples as non-prime
            for multiple in range(num * 2, len(sieve), num):
                sieve[multiple] = False


def extract_primes(sieve):
    """Extract prime numbers from the sieve."""
    return [index for index, is_prime in enumerate(sieve) if is_prime]


def generate_primes(max_value):
    """Generate prime numbers up to max_value using the Sieve of Eratosthenes."""
    if max_value < 1:
        return []

    sieve = initialize_sieve(max_value)
    apply_sieve(sieve)
    return extract_primes(sieve)


# Example Usage
max_value = 50
print(generate_primes(max_value))
