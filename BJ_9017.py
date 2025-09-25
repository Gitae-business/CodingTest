# 크로스 컨트리 https://www.acmicpc.net/problem/9017
import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    T = int(input())
    while T:
        T -= 1
        N = int(input())
        arr = list(map(int, input().split()))
        
        team = defaultdict(int)
        team_score = defaultdict(list)

        for i in arr:
            team[i] += 1
        
        score = 1
        keys = set()
        for i in arr:
            if team[i] >= 6:
                team_score[i].append(score)
                keys.add(i)
                score += 1

        mn, team_name, fifth_score = int(1e9), "", int(1e9)
        for i in keys:
            scores = team_score[i]
            s = sum(scores[:4])

            if s < mn:
                mn = s
                team_name = i
                fifth_score = scores[4]
            elif s == mn:
                if scores[4] < fifth_score:
                    mn = s
                    team_name = i
                    fifth_score = scores[4]

        print(team_name)

if __name__ == '__main__':
    main()
