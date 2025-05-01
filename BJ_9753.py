from bisect import bisect_left

def Eratosthenes(limit):
    is_prime = [False, False] + [True] * (limit - 1)
    for i in range(2, int(limit ** 0.5) + 1):
        if is_prime[i]:
            for j in range(i * i, limit + 1, i):
                is_prime[j] = False
    return [i for i, val in enumerate(is_prime) if val] # 소수만 반환

def main():
    primes = Eratosthenes(50000)
    T = int(input())

    for _ in range(T):
        k = int(input())
        min_prod = float('inf')

        for i in range(len(primes)):
            p1 = primes[i]
            target = (k + p1 - 1) // p1

            j = bisect_left(primes, target, lo=i+1)
            if j < len(primes):
                p2 = primes[j]
                prod = p1 * p2
                if prod < min_prod:
                    min_prod = prod

        print(min_prod)

if __name__ == '__main__':
    main()
