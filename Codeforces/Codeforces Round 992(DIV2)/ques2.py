#Question : Paint a Strip
#Link to the question: https://codeforces.com/contest/2040/problem/B

for _ in range(int(input())):
    n = int(input())
    ans =0
    if n==1:
        print("1")
        continue
    if n<=4:
        print("2")
        continue 
    res = 1
    while(res<n):
        res = res*2 +2 
        ans+=1
    print(ans+1)