# Image https://www.acmicpc.net/problem/9920
import sys
input = sys.stdin.readline

def main():
    L = int(input())
    image = [list(map(int, input().split())) for _ in range(L)]

    compressed = []

    def recursive(x, y, size):
        first_bit = image[y][x]
        is_uniform = True

        for r in range(y, y + size):
            for c in range(x, x + size):
                if image[r][c] != first_bit:
                    is_uniform = False
                    break
            if not is_uniform:
                break

        if is_uniform:
            if first_bit == 0:
                compressed.append('00')
            else:
                compressed.append('01')
            return
        
        else:
            compressed.append('1')
            new_size = size // 2
            
            recursive(x, y, new_size)
            recursive(x + new_size, y, new_size)
            recursive(x, y + new_size, new_size)
            recursive(x + new_size, y + new_size, new_size)

    recursive(0, 0, L)
    final_compressed_string = "".join(compressed)

    print(len(final_compressed_string))

if __name__ == '__main__':
    main()
