#Question : Showering
#Link to the question: https://codeforces.com/contest/1999/problem/C

for _ in range(int(input())):
    n,s,m = map(int,input().split())
    intervals =[]
    for _ in range(n):
        l,r = map(int,input().split())
        intervals.append([l,r])
    gaps =[]
    gaps.append(intervals[0][0])
    for i in range(1,n):
        gap=intervals[i][0]-intervals[i-1][1]
        gaps.append(gap)
    gaps.append(m-intervals[n-1][1])
    maxi = max(gaps)
    if maxi>=s:
        print("YES")
    else:
        print("NO")

