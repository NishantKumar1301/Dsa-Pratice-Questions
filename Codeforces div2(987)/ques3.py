#Link to the problem : https://codeforces.com/problemset/problem/2031/C

for _ in range(int(input())):
    n = int(input())
    
    if n % 2 == 0:
        result = []
        for i in range(1, n // 2 + 1):
            result.extend([i, i])
        print(" ".join(map(str, result)))
    elif n < 26:
        print(-1)
    else:
        j = 3
        flag = 1
        result = []
        for i in range(1, n + 1):
            if i == 1 or i == 10 or i == 26:
                result.append(1)
            elif i == 11 or i == 27:
                result.append(2)
            else:
                result.append(j)
                if flag % 2 == 0:
                    j += 1
                flag += 1
        print(" ".join(map(str, result)))
