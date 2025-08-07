# 1의 개수 세기 https://www.acmicpc.net/problem/9527
# 누적합
psum = [0] * 61
for i in range(1, 61):
    psum[i] = psum[i - 1] * 2 + 2 ** (i - 1)

def count_ones(num):
    if num < 0:
        return 0
    
    count = 0
    length = num.bit_length()
    for i in reversed(range(length)):
        if num & (1 << i):
            count += psum[i] + (num - (1 << i) + 1)
            num -= (1 << i)
    return count

def main():
    a, b = map(int, input().split())
    print(count_ones(b) - count_ones(a - 1))

if __name__ == '__main__':
    main()