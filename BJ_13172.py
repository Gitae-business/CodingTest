MOD = 1000000007

def mod_inv(x):
    # x^(x-1) ≡ x^(MOD-2) mod MOD
    return pow(x, MOD - 2, MOD) # == pow(x, MOD - 2) % 

def main():
    m = int(input())
    dice = []
    for _ in range(m):
        dice.extend(map(int, input().split()))

    ans = 0
    idx = 0

    for _ in range(m):
        n = dice[idx]
        s = dice[idx+1]
        idx += 2

        inv_n = mod_inv(n)
        term = (s * inv_n) % MOD
        ans = (ans + term) % MOD

    print(ans)

if __name__ == '__main__':
    main()
