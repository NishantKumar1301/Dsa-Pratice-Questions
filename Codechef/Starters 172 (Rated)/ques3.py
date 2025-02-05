#Question : Streak Star
#Link to the question: https://www.codechef.com/problems/STKSTR

# Cook your dish here
for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    def solve(arr):
        maxi, curr = 1, 1
        for i in range(1, n):
            if arr[i] >= arr[i - 1]:
                curr += 1
            else:
                maxi = max(maxi, curr)
                curr = 1
        return max(maxi, curr)
    ans = solve(arr)
    for i in range(n):
        val = arr[i]
        arr[i] *= x  
        ans = max(ans, solve(arr))
        arr[i] = val  
    print(ans)


