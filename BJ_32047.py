
def main():
    while 1:
        n = int(input())
        if (n == 0): return

        a = list(map(int, input().split()))
        b = list(map(int, input().split()))

        dis_a = a[0]
        dis_b = b[0]
        lead = 'a' if dis_a > dis_b else 'b' if dis_b > dis_a else 'same'

        overtakes = 0
        for i in range(1, n):
            dis_a += a[i]
            dis_b += b[i]

            if (dis_a > dis_b):
                if (lead == 'b'):
                    overtakes += 1
                lead = 'a'
            elif (dis_b > dis_a):
                if (lead == 'a'):
                    overtakes += 1
                lead = 'b'

        print(overtakes)

if __name__ == '__main__':
    main()
