#Question : Serval and Final MEX
#Link to the question: https://codeforces.com/contest/2085/problem/B

def helper(arr):
    l = max(len(arr) + 2, 6000)
    p = [False] * l
    for v in arr:
        if v < l:
            p[v] = True
    for i in range(l):
        if not p[i]:
            return i
    return l
 
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    
    ans = []
    
    while len(arr) > 1:
        flag = False
        ind = -1
        for i in range(len(arr)):
            if arr[i] == 0:
                flag = True
                ind = i
                break
        if not flag:
            l, r = 0, len(arr) - 1
            ans.append((l + 1, r + 1))
            val = helper(arr)
            arr = [val]
            break
        else:
            if ind < len(arr) - 1:
                l, r = ind, ind + 1
            else:
                l, r = ind - 1, ind
            ans.append((l + 1, r + 1))
            s = arr[l:r + 1]
            val = helper(s)
            arr2 = arr[:l] + [val] + arr[r + 1:]
            arr = arr2

    print(len(ans))
    for a in ans:
        print(a[0], a[1])

