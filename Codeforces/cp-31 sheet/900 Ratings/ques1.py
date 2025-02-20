#Question : Sum of Medians
#Link to the question: https://codeforces.com/problemset/problem/1440/B

def solve():
    n,k = map(int,input().split())
    arr = list(map(int, input().split()))
    # Write your logic here
    ans =0
    i=n*k
    while k>0:
        i =i-(n//2+1)
        ans +=arr[i]
        k-=1
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()


