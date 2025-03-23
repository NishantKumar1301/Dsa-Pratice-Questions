#Question : Pushing Balls
#Link to the question: https://codeforces.com/contest/2090/problem/B

def solve():
    n, m = map(int, input().split())
    grid = []
    for i in range(n):
        row = input().strip()
        grid.append(row)
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1':
                top = True
                left = True
                
                for k in range(i):
                    if grid[k][j] == '0':
                        top = False
                        break
                
                for k in range(j):
                    if grid[i][k] == '0':
                        left = False
                        break
                
                if not top and not left:
                    print("NO")
                    return
    
    print("YES")

for _ in range(int(input())):
    solve()

