def main():
    MAX = int(1e6) + 1
    arr = []

    def is_unique(n):
        used = 0
        while n > 0:
            digit = n % 10
            if used & (1 << digit):
                return False
            used |= (1 << digit)
            n //= 10
        return True

    i = 0
    while len(arr) < MAX:
        if is_unique(i):
            arr.append(i)
        i += 1

    while True:
        n = int(input())
        if n == 0: break
        print(arr[n])

if __name__ == '__main__':
    main()
