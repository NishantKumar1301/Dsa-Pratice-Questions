#Question : Find Outside Array
#Link to the question: https://www.codechef.com/START181B/problems/FINDOUT

# cook your dish here
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))
    s = set(arr)
    ans = []
    
    if s == {0}: 
        ans.append("-1")
    else:
        maxi = max(arr)
        if maxi > 0:
            ans.append(f"{maxi} {maxi}")
        else: 
            mini = min(arr)
            ans.append(f"{mini} {mini}")
    
    print("\n".join(ans))


