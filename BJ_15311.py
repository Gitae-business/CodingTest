from bisect import bisect_left, bisect_right
from itertools import combinations

def main():
    n, s = map(int, input().split())
    arr = list(map(int, input().split()))
    
    left = arr[:n//2]
    right = arr[n//2:]

    def getSubs(li):
        subs = []
        n = len(li)
        for i in range(n + 1):
            for comb in combinations(li, i):
                subs.append(sum(comb))
        return subs

    left_sums = getSubs(left)
    right_sums = getSubs(right)
    right_sums.sort()

    ans = 0
    for val in left_sums:
        target = s - val
        lo = bisect_left(right_sums, target)
        hi = bisect_right(right_sums, target)
        ans += (hi - lo)

    if s == 0:  # 공집합 제외 0 - 0
        ans -= 1
    
    print(ans)

if __name__ == '__main__':
    main()
