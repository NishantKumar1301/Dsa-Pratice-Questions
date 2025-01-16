#Question : Make K Most Frequent
#Link to the question: https://www.codechef.com/problems/P3169

# cook your dish here
def full(n, k, a):
    arr = [0] * 21
    for x in a:
        arr[x] += 1
    for v in range(1, 21):
        if v == k:
            continue
        if arr[k] < arr[v]:
            return False
    return True

def one_possible(n, k, a):
    arr = [0] * 21
    for i in range(n - 1):
        arr[a[i]] += 1
        if arr[k] == 0:
            continue
        if all(arr[k] >= arr[v] for v in range(1, 21) if v != k):
            return True
    
    arr1 = [0] * 21
    for i in range(n - 1, 0, -1):
        arr1[a[i]] += 1
        if arr1[k] == 0:
            continue
        if all(arr1[k] >= arr1[v] for v in range(1, 21) if v != k):
            return True

    return False

def helper(n, k, a):
    if full(n, k, a):
        return 0
    elif one_possible(n, k, a):
        return 1
    else:
        return 2

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    print(helper(n, k, arr))



