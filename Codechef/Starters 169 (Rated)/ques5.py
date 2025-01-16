#Question : Constant Subsequence
#Link to the question: https://www.codechef.com/problems/P5169

# cook your dish here
def helper_ques2(arr1, arr2, t):
    p, n, s, m = 0, 0, 0, 0
    while p < len(arr1) or n < len(arr2):
        while s + (arr1[p] if p < len(arr1) else 0) > t:
            if n < len(arr2):
                s += arr2[n]
                m = max(m, s)
                n += 1
            else:
                return False
            s = max(0, s)
        if p < len(arr1):
            s += arr1[p]
            m = max(m, s)
            p += 1
        elif n < len(arr2):
            s += arr2[n]
            m = max(m, s)
            n += 1
            s = max(0, s)
    return m <= t

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    arr1 = [x for x in arr if x >= 0]
    arr2 = [x for x in arr if x < 0]
    
    if not arr1:
        print(0)
        continue
    
    left, right, ans = max(arr1), sum(arr1), sum(arr1)
    
    while left <= right:
        mid = (left + right) // 2
        if helper_ques2(arr1, arr2, mid):
            ans = mid
            right = mid - 1
        else:
            left = mid + 1
    
    print(ans)



