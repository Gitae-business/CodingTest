# 조합 (Combination)
MOD = 10**9 + 7

def main():
    n, k = map(int, input().split())

    def fermat(x): # 페르마의 소정리
        return pow(x, MOD - 2, MOD)

    def comb(n, r):
        if r < 0 or r > n:
            return 0
        
        fact = [1] * (n + 1)
        for i in range(1, n + 1):
            fact[i] = fact[i - 1] * i % MOD
        a = fact[n]
        b = fermat(fact[r])
        c = fermat(fact[n - r])
        return a * b % MOD * c % MOD
    
    print(comb(n, k))
        

if __name__ == '__main__':
    main()
