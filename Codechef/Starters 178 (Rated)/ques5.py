#Question : Smoothly Increasing
#Link to the question: https://www.codechef.com/START178B/problems/SMOOTHINC

# cook your dish here
def helper2(arr):
    for i in range(1, len(arr)):
        if arr[i] <= arr[i - 1]:
            return False
    return True

def helper1(arr):
    while len(arr) > 1:
        if not helper2(arr):
            return False
        diff = [arr[i] - arr[i - 1] for i in range(1, len(arr))]
        arr = diff
    return True

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    if n - 1 >= 31:
        print('0' * n)
        continue

    ans = ['0'] * n

    for i in range(n):
        t = [arr[j] for j in range(n) if j != i]
        if helper1(t):
            ans[i] = '1'

    print(''.join(ans))


