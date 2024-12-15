#Question : Normal Problem
#Link to the question: https://codeforces.com/contest/2044/problem/B

for _ in range(int(input())):
    s = input() 
    ans = ""
    for i in range(len(s) - 1, -1, -1):
        if s[i] == 'p':
            ans += 'q'
        elif s[i] == 'q':
            ans += 'p'
        else:
            ans += 'w'
    print(ans)


