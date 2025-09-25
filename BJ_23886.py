# 알프수 https://www.acmicpc.net/problem/23886

def getGredient(a, b):
    if a == b:
        return 0
    elif a < b:
        return 1
    return -1

def main():
    nums = [int(a) for a in input()]
    
    gred = getGredient(nums[0], nums[1])
    diff = abs(nums[0] - nums[1])

    if not (nums[0] < nums[1] and nums[-2] > nums[-1]):
        print("NON ALPSOO")
        return

    for i in range(1, len(nums) - 1):
        temp_gred = getGredient(nums[i], nums[i+1])
        temp_diff = abs(nums[i] - nums[i+1])

        if temp_gred == gred:
            if temp_diff != diff or gred == 0:
                print("NON ALPSOO")
                return
        else:
            gred = temp_gred
            diff = temp_diff
    
    print("ALPSOO")
    return

if __name__ == '__main__':
    main()
