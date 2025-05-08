# Eidam-Sand Lair
def main():
    t = int(input())
    while (t):
        t -= 1
        yp, lp, ys, ls = map(int, input().split())

        walk_cost = yp * ys
        lift_cost = (lp if lp > yp else yp + abs(yp - lp)) * ls
        mix_cost = abs(yp - lp) * ys + lp * ls

        """
        엘 > 나 > 도착 일 경우
        (lp - yp) * ys + lp * ls

        나 > 엘 > 도착 일 경우
        (yp - lp) * ys + lp * ls
        """ 
        print(min(walk_cost, lift_cost, mix_cost))

if __name__ == '__main__':
    main()
