# 주사위 네개 https://www.acmicpc.net/problem/2484
import sys
input = sys.stdin.readline

def calculate_prize(dice):
    dice.sort()

    if dice[0] == dice[3]:
        return 50000 + dice[0] * 5000
    
    if dice[0] == dice[2] or dice[1] == dice[3]:
        return 10000 + dice[1] * 1000
    
    if dice[0] == dice[1] and dice[2] == dice[3]:
        return 2000 + dice[0] * 500 + dice[2] * 500
    
    for i in range(3):
        if dice[i] == dice[i+1]:
            return 1000 + dice[i] * 100
            
    return dice[3] * 100

def main():
    N = int(input())
    ans = 0

    for _ in range(N):
        dice = list(map(int, input().split()))
        ans = max(ans, calculate_prize(dice))
    
    print(ans)

if __name__ == '__main__':
    main()