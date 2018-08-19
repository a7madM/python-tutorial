# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem

class RunnerUp:
    def runner_up(self, arr):
        max1 = max2 = -2147483648
        for i in range(len(arr)):
            if arr[i] > max1:
                max2 = max1
                max1 = arr[i]
            elif (arr[i] > max2 and arr[i] != max1):
                max2 = arr[i]
        return max2


if __name__ == '__main__':
    runner_up = RunnerUp()
    n = int(raw_input())
    arr = map(int, raw_input().split())
    print runner_up.runner_up(arr)