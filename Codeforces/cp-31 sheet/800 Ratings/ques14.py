#Question : Sequence Game
#Link to the question: https://codeforces.com/problemset/problem/1862/B 

def solve():
    n = int(input())
    arr = list(map(int, input().split()))
    # Write your logic here
    ans = []
    ans.append(arr[0])
    for i in range(1,n):
        if arr[i]>=arr[i-1]:
            ans.append(arr[i])
        else:
            ans.append(arr[i])
            ans.append(arr[i])
    print(len(ans))
    print(*ans)

if __name__ == "__main__":
    for _ in range(int(input())):
        solve()
