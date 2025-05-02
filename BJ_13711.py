from bisect import bisect_left

def main():
    n = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    pos = {val: idx for idx, val in enumerate(B)}   # B 원소들의 위치
    mapped = [pos[a] for a in A]                    # A의 원소들을 B 인덱스 기준으로 정렬

    dp = []
    for x in mapped:
        idx = bisect_left(dp, x)
        if idx == len(dp):
            dp.append(x)
        else:
            dp[idx] = x
    
    print(len(dp))

if __name__ == '__main__':
    main()
