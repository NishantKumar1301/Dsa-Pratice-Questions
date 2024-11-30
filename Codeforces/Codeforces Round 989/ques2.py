#Question : Rakhsh's Revival
#Link to the question: https://codeforces.com/contest/2034/problem/B

for _ in range(int(input())):
    n, m, k = map(int, input().split())
    s = input()
    ans = 0
    cur = 0
    i = 0
    while i < n:  
        if s[i] == '0':
            if i > 0 and s[i - 1] == '0':
                cur += 1
            else:
                cur = 1
        else:
            cur = 0

        if cur == m:
            ans += 1
            cur = 0
            i += k - 1  

        i += 1  

    print(ans)


