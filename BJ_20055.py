# 컨베이어 벨트 위의 로봇 https://www.acmicpc.net/problem/20055
from collections import deque

def main():
    n, k = map(int, input().split())
    durability = list(map(int, input().split()))

    '''
    1 올리고 N 내림. 벨트는 1~2N
    박스 모양 로봇은 1에서 올라가 N에서 내림
    벨트 위에서 스스로 이동 가능
    로봇을 올리거나 어떤 칸으로 이동하면 해당 칸 내구도 -1
    
    1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 이동
    2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한칸 이동할 수 있다면 이동
    3. 올리는 위치에 있는 칸 내구도 0이 아니면 올림
    4. 내구도가 0인 칸 K개 이상이면 과정 종료. 아니면 반복
    '''

    belt = deque(durability)
    robots = deque([False for _ in range(n)])
    
    def checkEnd():
        cnt = 0
        for d in belt:
            if d == 0:
                cnt += 1
        return cnt >= k

    answer = 0
    while not checkEnd():
        answer += 1

        # 1. 벨트가 각 칸 위에 있는 로봇과 함께 한 칸 이동
        belt.appendleft(belt.pop())
        robots.appendleft(False)
        robots.pop()
        robots[n-1] = False # n에 도달 로봇 바로 내림

        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한칸 이동할 수 있다면 이동
        for i in range(n-1, 1, -1):
            if belt[i] > 0 and not robots[i] and robots[i-1]:
                robots[i], robots[i-1] = robots[i-1], robots[i]
                belt[i] -= 1    # 수명 감소
        
        # 3. 올리는 위치에 있는 칸 내구도 0이 아니면 올림
        if belt[0] > 0:
            robots[0] = True
            belt[0] -= 1
        
    print(answer)

if __name__ == '__main__':
    main()
