def compute_feedback(secret, guess):
    feedback = [''] * 5
    used_in_secret = [False] * 5

    # Step 1: Green '*'
    for i in range(5):
        if guess[i] == secret[i]:
            feedback[i] = '*'
            used_in_secret[i] = True

    # Step 2: Yellow '!'
    for i in range(5):
        if feedback[i] == '':
            found = False
            for j in range(5):
                if not used_in_secret[j] and guess[i] == secret[j]:
                    found = True
                    used_in_secret[j] = True
                    break
            feedback[i] = '!' if found else 'X'

    return ''.join(feedback)

def main():
    n = int(input())
    words = [input().strip() for _ in range(n)]
    secret = words[0]

    g = int(input())
    feedbacks = [input().strip() for _ in range(g)]

    for fb in feedbacks:
        count = 0
        for word in words:
            if compute_feedback(secret, word) == fb:
                count += 1
        print(count)

if __name__ == '__main__':
    main()
