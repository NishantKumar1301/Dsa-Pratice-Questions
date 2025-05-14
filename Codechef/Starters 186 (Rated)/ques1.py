#Question : Approval Ratings
#Link to the question: https://www.codechef.com/START186B/problems/APPROVAL


# cook your dish here
for _ in range(int(input())):
    arr = list(map(int,input().split()))
    total = sum(arr)
    ans = 0
    if total >= 35:
        print(ans)
        continue
    arr.sort()
    for num in arr:
        if total >= 35:
            break
        total += (10 - num)
        ans += 100
    print(ans)

