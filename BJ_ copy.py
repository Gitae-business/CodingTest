import sys
input = sys.stdin.readline

def is_name(word):
    if word[-1] in ".?!":
        core = word[:-1]
    else:
        core = word

    if len(core) == 0:
        return False

    if not core[0].isupper():
        return False

    for c in core[1:]:
        if not c.islower():
            return False

    return True

def main():
    N = int(input())
    words = input().split()

    result = []
    cnt = 0

    for w in words:
        if is_name(w):
            cnt += 1

        if w[-1] in ".?!":
            result.append(cnt)
            cnt = 0

    for v in result:
        print(v)

if __name__ == "__main__":
    main()
