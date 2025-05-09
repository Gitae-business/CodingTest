# 소수의 연속합 https://www.acmicpc.net/problem/1644

def main():
    n = int(input())

    if n < 2:
        print(0)
        return

    # 에라토스테네스의 체로 소수 구하기
    isPrime = [True] * (n + 1)
    isPrime[0] = isPrime[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if isPrime[i]:
            for j in range(i * i, n + 1, i):
                isPrime[j] = False

    primes = [i for i, v in enumerate(isPrime) if v]

    # 투 포인터로 연속된 소수의 합 구하기
    left = right = 0    # 둘 다 0에서 출발
    total = 0           # 현재의 부분합
    ans = 0

    while True:
        if total >= n:
            if total == n:
                ans += 1
            total -= primes[left]   # total이 넘치면 왼쪽에서 덜어내기
            left += 1
        elif right == len(primes):  # right가 끝 도달 시 break
            break
        else:
            total += primes[right]  # total이 부족하면 오른쪽에서 추가
            right += 1

    print(ans)

if __name__ == '__main__':
    main()
