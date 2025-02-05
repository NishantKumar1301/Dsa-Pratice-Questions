#Question : Yarik and Musical Notes
#Link to the question: https://codeforces.com/contest/1899/problem/D

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    ans , freq = 0,{}
    for num in arr:
        ans += freq.get(num,0)
        if num==1:
            ans+=freq.get(2,0)
        if num==2:
            ans += freq.get(1,0)
        freq[num]= freq.get(num,0)+1
    print(ans)

