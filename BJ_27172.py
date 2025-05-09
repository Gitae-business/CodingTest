# 수 나누기 게임 https://www.acmicpc.net/problem/27172
def main():
    n = int(input())
    arr = list(map(int, input().split()))

    mx = max(arr)
    cnt = [0] * (mx + 1)        # 등장 횟수
    score = {i:0 for i in arr}  # 내가 나누면 +1, 나눠지면 -1

    for i in arr:
        cnt[i] += 1     # 초기화

    # 브루트포스
    for x in range(1, mx + 1):
        if cnt[x] == 0:                     # 미등장시 스킵
            continue
        for mul in range(x * 2, mx + 1, x): # 배수들 확인
            if cnt[mul]:                    # 배수인 카드가 존재
                score[x] += 1               # 내 점수 추가
                score[mul] -= 1             # 상대 점수 감소
    
    ans = [score[i] for i in arr]
    print(*ans)
    

if __name__ == '__main__':
    main()
