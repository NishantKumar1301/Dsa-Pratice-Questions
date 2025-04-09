#Question : The Best Matrix
#Link to the question: https://www.codechef.com/START181B/problems/GOODMATRIX?tab=ide

# cook your dish here
for _ in range(int(input())):
    n,m = map(int,input().split())
    grid =[]
    for _ in range(n):
        row = list(map(int,input().split()))
        grid.append(row)
    # grid = [list(map(int,input().split())) for _ in range(n)]
    total = n*m 
    ans = total
    for row in (1,-1):
        for col in (1,-1):
            freq={}
            for i in range(n):
                for j in range(m):
                    val = grid[i][j]-(row*i+col*j)
                    freq[val]=freq.get(val,0)+1
            ans = min(ans,total-max(freq.values()))
    print(ans)

