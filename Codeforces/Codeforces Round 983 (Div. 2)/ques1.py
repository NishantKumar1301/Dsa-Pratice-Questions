#Question : Circuit
#Link to the question: https://codeforces.com/contest/2032/problem/B

for _ in range(int(input())):
    n = int(input())
    arr= list(map(int,input().split()))
    zero,one = arr.count(0),arr.count(1)
    mini = one%2 
    maxi = min(zero,one)
    print(mini,maxi)