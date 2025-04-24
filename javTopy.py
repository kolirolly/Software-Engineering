import math

class GeneratePrime:
    def generate_primes(self, max_value):
        if max_value < 1:
            return []

        s = max_value + 1
        f = [True] * s

        # Initialize array
        for i in range(len(f)):
            f[i] = True

        # Get rid of known non-primes
        f[0] = f[1] = False

        # Sieve of Eratosthenes
        for i in range(2, int(math.sqrt(s)) + 1):
            if f[i]:  # Cross out its multiples
                for j in range(2 * i, s, i):
                    f[j] = False

        # Count the number of primes
        count = 0
        for i in range(s):
            if f[i]:
                count += 1

        primes = [0] * count

        # Copy sieve into result array
        k = 0
        for l in range(s):
            if f[l]:
                primes[k] = l
                k += 1

        return primes

# Example Usage
gp = GeneratePrime()
print(gp.generate_primes(50))
