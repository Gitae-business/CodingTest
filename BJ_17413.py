# 단어 뒤집기 2 https://www.acmicpc.net/problem/17413
def main():
    s = input()
    result = []
    stack = []
    in_tag = False

    for c in s:
        if c == '<':
            while stack:
                result.append(stack.pop())
            in_tag = True
            result.append(c)
        elif c == '>':
            in_tag = False
            result.append(c)
        elif in_tag:
            result.append(c)
        elif c == ' ':
            while stack:
                result.append(stack.pop())
            result.append(' ')
        else:
            stack.append(c)

    while stack:
        result.append(stack.pop())

    print(''.join(result))

if __name__ == '__main__':
    main()
