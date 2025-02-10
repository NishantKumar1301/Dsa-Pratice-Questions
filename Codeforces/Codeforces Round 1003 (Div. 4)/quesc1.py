#Question : Skibidus and Fanum Tax (easy version)
#Link to the question: https://codeforces.com/contest/2065/problem/C1

from bisect import bisect_left

def min_element(arr, val):
    idx = bisect_left(arr, val)
    return arr[idx] if idx < len(arr) else -1

def solve():
    n, m = map(int, input().split())
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    
    arr2.sort()
    prev = float('-inf')

    for i in range(n):
        val = min_element(arr2, prev + arr1[i])  
        if val != -1:
            if arr1[i] < prev:
                arr1[i] = val - arr1[i]
            else:
                arr1[i] = min(arr1[i], val - arr1[i])

        if arr1[i] < prev:
            print("NO")
            return  

        prev = arr1[i]

    print("YES")

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()


