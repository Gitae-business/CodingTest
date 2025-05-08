# Just A Minim
def main():
    notes = {
        0: 2,
        1: 1,
        2: 1/2,
        4: 1/4,
        8: 1/8,
        16: 1/16
    }

    n = int(input())
    arr = list(map(int, input().split()))
    ans = sum([notes[i] for i in arr])
    print(f"{ans:.6f}")

if __name__ == '__main__':
    main()
