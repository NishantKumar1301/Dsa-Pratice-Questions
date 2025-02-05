#Question : 250 Thousand Tons of TNT
#Link to the question: https://codeforces.com/contest/1899/problem/B


def compute_factors(limit):
    factor = [[] for _ in range(limit)]
    for i in range(1,limit):
        for j in range(2*i,limit,i):
            factor[j].append(i)
    return factor 

def solve(n,arr,factor):
    ans = 0
    for fact in factor[n]:
        sums = [sum(arr[i:i+fact]) for i in range(0,n,fact)]
        ans = max(ans,max(sums)-min(sums))
    return ans

limit = 150001
factors = compute_factors(limit)
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    print(solve(n,arr,factors))



