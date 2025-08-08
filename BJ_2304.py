# 창고 다각형 https://www.acmicpc.net/problem/2304
def main():
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    arr.sort()

    max_height = max(h[1] for h in arr)
    answer = 0

    left_idx = 0
    left_height = arr[0][1]
    
    while arr[left_idx][1] != max_height:
        next_left = arr[left_idx + 1]
        answer += left_height * (next_left[0] - arr[left_idx][0])
        left_idx += 1
        if left_height < next_left[1]:
            left_height = next_left[1]

    right_idx = N - 1
    right_height = arr[-1][1]
    
    while arr[right_idx][1] != max_height:
        past_right = arr[right_idx - 1]
        answer += right_height * (arr[right_idx][0] - past_right[0])
        right_idx -= 1
        if right_height < past_right[1]:
            right_height = past_right[1]

    first_max_x = arr[left_idx][0]
    last_max_x = arr[right_idx][0]
    answer += max_height * (last_max_x - first_max_x + 1)

    print(answer)

if __name__ == '__main__':
    main()
