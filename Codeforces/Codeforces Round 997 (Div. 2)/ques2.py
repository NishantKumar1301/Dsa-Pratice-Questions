#Question : Find the Permutation
#Link to the question:  https://codeforces.com/contest/2056/problem/B


"""Author : Nishant Kumar"""

def solve():
    n = int(input())
    adj = [input().strip() for _ in range(n)]
    ans = [0] * n
    left = [0] * n
    right = [n - 1] * n

    for i in range(n):
        cnt = 0
        for j in range(n):
            if left[j] == left[i] and right[j] == right[i] and adj[i][j] == '1':
                cnt += 1

        pos = right[i] - cnt
        ans[pos] = i + 1

        for j in range(n):
            if left[j] == left[i] and right[j] == right[i] and i != j:
                if adj[i][j] == '0':
                    right[j] = pos - 1
                else:
                    left[j] = pos + 1

        left[i] = right[i] = pos

    print(" ".join(map(str, ans)))


for _ in range(int(input())):
    solve()


"""Author : Nishant Kumar"""




