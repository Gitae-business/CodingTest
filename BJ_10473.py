# 인간 대포 https://www.acmicpc.net/problem/10473
import math
import heapq

INF = int(1e9)

def main():
    v_walk = 5  # 걷는 속도: 5 m/s
    sx, sy = map(float, input().split())
    ex, ey = map(float, input().split())
    n = int(input())
    canons = [list(map(float, input().split())) for _ in range(n)]

    # 모든 노드(시작, 대포, 도착)를 포함한 위치 리스트
    positions = [(sx, sy)] + canons + [(ex, ey)]

    # 복소수 좌표 -> 최소 시간 저장용 딕셔너리
    cost = {complex(x, y): INF for (x, y) in positions}
    cost[complex(sx, sy)] = 0

    # 거리 계산 함수
    def get_dist(x1, y1, x2, y2):
        return math.hypot(x1 - x2, y1 - y2)

    # 다익스트라 우선순위 큐 시작 (시작점에서 출발)
    pq = []
    heapq.heappush(pq, (0, (sx, sy)))

    while pq:
        cur_time, (x, y) = heapq.heappop(pq)
        cur_pos = complex(x, y)

        # 이미 최소값보다 크면 스킵
        if cur_time > cost[cur_pos]:
            continue

        for (nx, ny) in positions:
            if (x, y) == (nx, ny):
                continue

            d = get_dist(x, y, nx, ny)
            target_pos = complex(nx, ny)

            # 걷기 vs 대포 발사 후 도착 지점까지 걷기
            # 단, 현재 위치가 시작점이면 무조건 걷기만 가능
            if cur_pos == complex(sx, sy):
                next_time = cur_time + d / v_walk
            else:
                # 대포 발사는 2초 + 남은 거리 걷기, 또는 그냥 걷기
                shoot_time = abs(d - 50) / v_walk + 2
                walk_time = d / v_walk
                next_time = cur_time + min(walk_time, shoot_time)

            if next_time < cost[target_pos]:
                cost[target_pos] = next_time
                heapq.heappush(pq, (next_time, (nx, ny)))

    # 도착지까지 걸리는 최소 시간 출력
    print(cost[complex(ex, ey)])

if __name__ == '__main__':
    main()
