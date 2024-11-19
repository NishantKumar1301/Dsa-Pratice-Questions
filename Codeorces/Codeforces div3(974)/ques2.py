#Link to the problem : https://codeforces.com/contest/2014/problem/B

for _ in range(int(input())):
    n,k = map(int,input().split())
    start = n-k+1
    end =n
    length =end-start+1
    if start %2 ==0:
        if length ==1 or (length//2)%2==0:
            print("YES")
        else:
            print("NO")
    else:
        if (length >1 and ((length+1)//2)%2==0):
            print("YES")
        else:
            print("NO")