#Question : Trinity
#Link to the question: https://codeforces.com/contest/2032/problem/C


def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    ans = n
    for i in range(n-1):
        left,ind,right=i+1,i+1,n-1
        while left<=right:
            mid = left+(right-left)//2
            if arr[i]+arr[i+1]>arr[mid]:
                ind,left=mid,mid+1
            else:
                right = mid-1
        ans = min(ans,n-(ind-i+1))
    print(ans)


if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
