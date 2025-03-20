#Question : To Zero
#Link to the question: https://codeforces.com/contest/2075/problem/A
import math
for _ in range(int(input())):
    n,k = map(int,input().split())
    ans =0
    if n%2==0:
        k-=1
    else:
        n-=k
        ans+=1
        k-=1
    ans += math.ceil(n/k)
    print(ans)