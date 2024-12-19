#Question :  Kevin and Binary Strings
#Link to the question: https://codeforces.com/contest/2048/problem/C

z = int(input())
for _ in range(z):
    s = input()
    p = -1
    n = len(s)
    res = 0
 
    for i in range(n):
        if s[i] == '0':
            p = i
            break
        else:
            res += 1
 
    y1 = 0
    if p != -1:
        for i in range(p, n):
            if s[i] == '0':
                y1 += 1
            else:
                break
 
    if p == -1:
        print(f"1 {len(s)} 1 1")
    else:
        print(f"1 {len(s)} {max(0, p - y1) + 1} {n - min(p, y1)}")